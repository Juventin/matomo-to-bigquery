import os
import functions_framework

from extract import export_matomo_data
from transform import transform_matomo_data
from load import load_matomo_to_bigquery

MATOMO_URL = os.environ.get('MATOMO_URL')
MATOMO_TOKEN = os.environ.get('MATOMO_TOKEN')
PROJECT_ID = os.environ.get('PROJECT_ID')


@functions_framework.http
def etl(request):
    """Cloud function entrypoint."""
    offset = 0
    chunk_size = 5000
    continue_loop = True

    while continue_loop:

        # Extract
        matomo_data = export_matomo_data(
            MATOMO_URL, MATOMO_TOKEN, id_site=1,
            period="day", date="yesterday", format="json",
            filter_limit=chunk_size, filter_offset=offset
        )

        if len(matomo_data) > 0:

            # Transform
            visit, visit_detail = transform_matomo_data(matomo_data)

            # Load
            load_matomo_to_bigquery(visit, "visit")
            load_matomo_to_bigquery(visit_detail, "visit_detail")

            if len(matomo_data) < chunk_size:
                continue_loop = False
            else:
                offset += chunk_size

        else:
            continue_loop = False

    return '200'
