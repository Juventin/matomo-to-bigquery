from google.cloud import bigquery
from google.api_core.exceptions import Conflict
from typing import Optional, List


def create_dataset(dataset_name: str, project_id: str, region: str = "EU") -> None:
    """
    Creates a BigQuery dataset in the specified project and region.

    Args:
        dataset_name (str): The name of the dataset to create.
        project_id (str): The ID of the Google Cloud project.
        region (str, optional): The region where the dataset will be created. Defaults to "EU".

    Returns:
        None

    Raises:
        google.api_core.exceptions.Conflict: If the dataset already exists.
    """
    client = bigquery.Client(project=project_id)
    dataset = bigquery.Dataset(f"{project_id}.{dataset_name}")

    dataset.location = region

    try:
        dataset = client.create_dataset(dataset, timeout=30)
        print("Created dataset {}.{}".format(
            client.project, dataset.dataset_id))
    except Conflict:
        print("Dataset {}.{} already exists.".format(
            client.project, dataset.dataset_id))


class Table:
    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id
        self.dataset_id: str = ""
        self.table_name: str = ""
        self.schema: List[bigquery.SchemaField] = []
        self.date_partition: Optional[str] = None
        self.partition_expiration_days: Optional[int] = None


def create_table(table_object: Table) -> None:
    """
    Creates a BigQuery table based on the provided table object.

    Args:
        table_object (Table): An object containing the necessary information to create the table.
            - project_id (str): The ID of the Google Cloud project.
            - dataset_id (str): The ID of the BigQuery dataset.
            - table_name (str): The name of the table to be created.
            - schema (List[SchemaField]): The schema of the table.
            - date_partition (Optional[str]): The field to use for date partitioning, if any.
            - partition_expiration_days (Optional[int]): The number of days before partitions expire, if any.

    Raises:
        google.api_core.exceptions.Conflict: If the table already exists.

    Returns:
        None
    """
    client = bigquery.Client(project=table_object.project_id)

    table_id = f"{table_object.project_id}.{table_object.dataset_id}.{table_object.table_name}"

    table = bigquery.Table(table_id, schema=table_object.schema)

    if table_object.date_partition is not None:
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field=table_object.date_partition
        )

    if table_object.partition_expiration_days is not None:
        table.partition_expiration = table_object.partition_expiration_days

    try:
        table = client.create_table(table)
        print(
            "Created table {}.{}.{}".format(
                table.project, table.dataset_id, table.table_id)
        )
    except Conflict:
        print("Table {}.{}.{} already exists.".format(
            table.project, table.dataset_id, table.table_id))
