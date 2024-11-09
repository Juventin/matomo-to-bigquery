import datetime
import sys
import os
import json
from dotenv import load_dotenv


def load_environment_variables():
    load_dotenv()
    return {
        'MATOMO_URL': os.environ.get('MATOMO_URL'),
        'MATOMO_TOKEN': os.environ.get('MATOMO_TOKEN'),
        'PROJECT_ID': os.environ.get('PROJECT_ID'),
        'GOOGLE_APPLICATION_CREDENTIALS': os.getenv("APPLICATION_CREDENTIALS")
    }


def set_google_credentials(credentials_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def process_data(matomo_url, matomo_token, last_date, last_offset, chunk_size=5000):
    continue_dates = True
    while continue_dates:
        offset = last_offset
        continue_loop = True
        while continue_loop:
            matomo_data = export_matomo_data(
                matomo_url, matomo_token, id_site=1,
                period="day", date=str(last_date), format="json",
                filter_limit=chunk_size, filter_offset=offset
            )

            if len(matomo_data) > 0:
                visit, visit_detail = transform_matomo_data(matomo_data)
                load_matomo_to_bigquery(
                    visit, "visit", project_id=env_vars['PROJECT_ID'])
                load_matomo_to_bigquery(
                    visit_detail, "visit_detail", project_id=env_vars['PROJECT_ID'])

                if len(matomo_data) < chunk_size:
                    continue_loop = False
                else:
                    offset += chunk_size
            else:
                continue_loop = False
                if offset == 0:
                    continue_dates = False

        last_date = last_date - datetime.timedelta(days=1)


if __name__ == "__main__":
    # TODO: make it dynamic
    here = os.path.dirname(__file__)
    sys.path.append(os.path.join(here, '../daily_etl/cloud-function'))
    from load import load_matomo_to_bigquery
    from transform import transform_matomo_data
    from extract import export_matomo_data

    env_vars = load_environment_variables()
    set_google_credentials(env_vars['GOOGLE_APPLICATION_CREDENTIALS'])

    last_date = datetime.datetime.now().date() - datetime.timedelta(days=1)
    last_offset = 0

    process_data(env_vars['MATOMO_URL'],
                 env_vars['MATOMO_TOKEN'], last_date, last_offset)
