from typing import List, Dict, Tuple

import os
import pandas
import numpy as np
from google.cloud import bigquery

from data_model import VISIT_DETAIL_SCHEMA, VISIT_SCHEMA

PROJECT_ID = os.environ.get('PROJECT_ID')


def get_table_schema(table_name: str) -> List[bigquery.SchemaField]:
    """
    Get the schema for the specified table.

    Parameters:
        table_name (str): The name of the table.

    Returns:
        List[bigquery.SchemaField]: The schema of the table.

    Raises:
        ValueError: If an invalid table name is provided.
    """
    if table_name == 'visit':
        return VISIT_SCHEMA
    if table_name == 'visit_detail':
        return VISIT_DETAIL_SCHEMA

    raise ValueError(f"Invalid table name: {table_name}")


def apply_schema_format(dataframe: pandas.DataFrame, table_schema: List[bigquery.SchemaField]) -> pandas.DataFrame:
    """
    Apply the specified BigQuery schema format to given dataframe.

    Args:
        dataframe (pandas.DataFrame): The dataframe to apply the schema format to.
        table_schema (List[bigquery.SchemaField]): The schema fields to apply to the dataframe.

    Returns:
        pandas.DataFrame: The dataframe with the schema format applied.
    """
    for col in table_schema:
        try:
            if col.field_type == "STRING":
                dataframe[col.name] = dataframe[col.name].astype(str)
            elif col.field_type == "FLOAT":
                dataframe[col.name] = dataframe[col.name].astype(float)
            elif col.field_type == "INTEGER":
                dataframe[col.name] = np.floor(pandas.to_numeric(
                    dataframe[col.name], errors='coerce')).astype('Int64')
            elif col.field_type == "DATE":
                dataframe[col.name] = pandas.to_datetime(
                    dataframe[col.name], format='%Y-%m-%d')
            elif col.field_type == "DATETIME":
                dataframe[col.name] = pandas.to_datetime(
                    dataframe[col.name], format='%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(f"Failed to apply schema format for column {col.name}: {e}")

    return dataframe


def load_matomo_to_bigquery(data: List[Dict], table_name: str, project_id: str = PROJECT_ID) -> None:
    """
    Load Matomo data into BigQuery table : {PROJECT_ID}.matomo.{table_name}.

    Args:
        data (List[Dict]): The data to be loaded into BigQuery.
        table_name (str): The name of the BigQuery table to load the data into.

    Returns:
        None: This function does not return anything.
    """

    table_id = f"{project_id}.matomo.{table_name}"
    table_schema = get_table_schema(table_name)

    # Prepare data
    dataframe = pandas.DataFrame(
        data,
        columns=[col.name for col in table_schema]
    )

    dataframe = apply_schema_format(dataframe, table_schema)

    # Load data
    client = bigquery.Client(project=project_id)

    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        write_disposition="WRITE_APPEND",
    )

    print("Loading rows...", end="\r")
    job = client.load_table_from_dataframe(
        dataframe, table_id, job_config=job_config
    )
    job.result()

    table = client.get_table(table_id)
    print("Loaded {} rows to {}".format(len(dataframe), table_id))

    return
