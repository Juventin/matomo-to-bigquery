from typing import List, Dict, Tuple

import uuid
import json
from json_normalize import json_normalize


def clean_keys(data: List[Dict]) -> List[Dict]:
    """Clean json keys"""
    # replace all "." in json keys by "_"
    data = [{k.replace(".", "_"): v for k, v in row.items()} for row in data]

    # lower all keys in data
    data = [{k.lower(): v for k, v in row.items()} for row in data]

    return data


def transform_matomo_data(raw_data: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """Transforms raw matomo data in "visit" and "visit_detail" tables."""

    # # Visits # #

    visit = list(json_normalize(
        raw_data,
        drop_nodes=["pluginsIcons", "customVariables",
                    "idSite", "actionDetails"]
    ))
    visit = clean_keys(visit)

    # # Visit Detail # #

    visit_detail = list(json_normalize(
        raw_data,
        drop_nodes=["pluginsIcons", "customVariables", "idSite"]
    ))
    visit_detail = clean_keys(visit_detail)

    # Keep only keys from elements in visit_detail that starts with actionDetails
    visit_detail = [{k: v for k, v in row.items() if (k.startswith(
        "actiondetails_") or k == "idvisit")} for row in visit_detail]

    # add an "id" key with a uuid
    visit_detail = [{"id": str(uuid.uuid4()), **row} for row in visit_detail]

    return visit, visit_detail
