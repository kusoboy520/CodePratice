from pathlib import Path

import pandas as pd
from prefect import flow, task
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket


@task()
def extract_from_gcs(color: str, year: int, month: int) ->Path:
    """Download trip data from GCS"""
    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../data/")

    return Path(f"../data/{gcs_path}")



@flow()
def etl_gcs_to_bq():
    """Main ETL to load data into Big Query"""
    color="yellow"
    year=2021
    month=1
    path = extract_from_gcs(color, year, month)

if __name__ == "__main__":
    etl_gcs_to_bq()