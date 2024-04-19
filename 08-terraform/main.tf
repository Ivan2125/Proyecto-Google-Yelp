terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  # Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  #  credentials = 
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "data-lake-bucket_new" {
  name     = var.datalake-bucket
  location = var.location

  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  force_destroy               = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_storage_bucket_object" "load_files" {
  for_each = fileset("${path.module}/01-data-cleaned", "**/*")

  name   = each.value
  bucket = google_storage_bucket.data-lake-bucket_new.name
  source = "${path.module}/01-data-cleaned/${each.value}"
}
resource "google_bigquery_dataset" "dataset" {
  dataset_id                 = var.bq_dataset_name
  project                    = var.project
  location                   = var.location
  delete_contents_on_destroy = true
}

data "archive_file" "function_code" {
  type        = "zip"
  source_dir  = "${path.module}/function_code"
  output_path = "${path.module}/function_code.zip"
}

resource "google_storage_bucket_object" "function_code" {
  name   = "function_code.zip"
  bucket = google_storage_bucket.data-lake-bucket_new.name
  source = data.archive_file.function_code.output_path
}

resource "google_cloudfunctions_function" "function" {
  name                  = "streaming"
  description           = "Function to load data from GCS to BigQuery"
  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.data-lake-bucket_new.name
  source_archive_object = google_storage_bucket_object.function_code.name
  entry_point           = "streaming"
  runtime               = "python310"

  environment_variables = {
    PROJECT_ID = var.project
    BQ_DATASET = "datawarehouse_ye_go_cs_419123"
    BQ_TABLE   = "reviews_unified"
  }

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.data-lake-bucket_new.name
  }
}


/*
data "archive_file" "function_code" {
  type        = "zip"
  source_dir  = "${path.module}/function_code"
  output_path = "${path.module}/function_code.zip"
}

resource "google_storage_bucket_object" "function_code" {
  name   = "function_code.zip"
  bucket = google_storage_bucket.data-lake-bucket_new.name
  source = data.archive_file.function_code.output_path
}

resource "google_cloudfunctions_function" "function" {
  name                  = "streaming"
  description           = "Function to load data from GCS to BigQuery"
  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.data-lake-bucket_new.name
  source_archive_object = google_storage_bucket_object.function_code.name
  trigger_http          = true
  entry_point           = "streaming"
  runtime               = "python310"

  environment_variables = {
    PROJECT_ID  = var.project
    BQ_DATASET  = "your_bigquery_dataset"
    BQ_TABLE    = "your_bigquery_table"
  }
}
*/