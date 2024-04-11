from google.cloud import bigquery
from google.cloud import storage

def load_parquet_data(data, context):
    """Cloud Function to be triggered by Cloud Storage event."""
    bucketname = data['datalake_ye_go_cs_419123']
    filename = data['reviews_unified']

    storage_client = storage.Client()
    bigquery_client = bigquery.Client()

    # Define BigQuery dataset and table
    dataset_id = 'perfect-garden-419123.datawarehouse_ye_go_cs_419123'
    table_id = 'perfect-garden-419123.datawarehouse_ye_go_cs_419123.reviews_unified'

    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Define job configuration
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.source_format = bigquery.SourceFormat.PARQUET
    job_config.autodetect = True

    # Define GCS blob
    blob = storage_client.get_bucket(bucketname).blob(filename)
    uri = f'gs://{bucketname}/{blob.name}'

    # Create load job
    load_job = bigquery_client.load_table_from_uri(
        uri,
        table_ref,
        job_config=job_config
    )

    load_job.result()  # Wait for job to complete

    print(f'Loaded {load_job.output_rows} rows into {dataset_id}:{table_id} from {uri}.')