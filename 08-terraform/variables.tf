variable "credentials" {
  description = "My Credentials"
  default     = "secrets/my-creds.json"

}


variable "project" {
  description = "Walgreens-Data-Project"
  default     = "perfect-garden-419123"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "US"
}

variable "bq_dataset_name" {
  description = "Datawarehouse"
  #Update the below to what you want your dataset to be called
  default = "datawarehouse_ye_go_cs_419123"
}

variable "datalake-bucket" {
  description = "Datalake"
  #Update the below to a unique bucket name
  default = "datalake_ye_go_cs_419123"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
} 