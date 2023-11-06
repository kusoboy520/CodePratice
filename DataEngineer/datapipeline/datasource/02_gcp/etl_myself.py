import pandas as pd
from prefect import task, flow
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

from pathlib import Path

@task(retries=3)
def fetch(dataset_url: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_url, )
    return df

@task(log_prints=True)
def clean(df: pd.DataFrame,) -> pd.DataFrame:
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    print(f"rows, columns: {df.shape}")
    
    return df


@task(log_prints=True)
def write_local(df: pd.DataFrame, color: str, dataset_file: str) -> Path:
    path = Path(f"data/{color}/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")

    return path

@task()
def write_gcs(path: Path) -> None:
    gcs_block = GcsBucket.load("localgcsblock")
    gcs_block.upload_from_path(
        from_path = path,
        to_path = path
    )

@flow()
def etl_web_to_gcs() -> None:
    color = "yellow"
    year = 2019
    month = 12
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"
    Path(f"data/{color}/").mkdir(parents=True, exist_ok=True)
    df = fetch(dataset_url)
    df_clean = clean(df)
    path = write_local(df_clean, color, dataset_file)
    write_gcs(path)


if __name__ == '__main__':
    etl_web_to_gcs()