import requests
import json

def export_matomo_data(
    url: str,
    token_auth: str,
    id_site: int,
    period: str = 'day',
    date: str = 'yesterday',
    format: str = 'json',
    filter_limit: int = -1,
    filter_offset: int = 0
) -> str:
    """
    Export Matomo data from the Live.getLastVisitsDetails endpoint.
    API reference : https://developer.matomo.org/api-reference/reporting-api

    Parameters:
        url (str): The URL of the Matomo server.
        token_auth (str): The authentication token.
        id_site (int): The ID of the site.
        period (str, optional): The period of the data. Defaults to 'day'.
        date (str, optional): The date of the data. Defaults to 'yesterday'.
        format (str, optional): The format of the data. Defaults to 'json'.
        filter_limit (int, optional): The limit of filtered data. Defaults to -1.
        filter_offset (int, optional): The offset of filtered data. Defaults to 0.

    Returns:
        str or None: The response text if the request is successful, otherwise None.
    """

    api_endpoint = f"{url}/index.php?module=API&method=Live.getLastVisitsDetails"

    params = {
        "idSite": id_site,
        "period": period,
        "date": date,
        "format": format,
        "token_auth": token_auth,
        "filter_limit": filter_limit,
        "filter_offset": filter_offset
    }

    print(f"Query running with params : {params}")
    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
