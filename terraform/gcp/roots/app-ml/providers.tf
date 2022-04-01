provider "google" {
  credentials = var.gcp_credentials
  project     = var.gcp_project_id
  region      = var.gcp_region
}

terraform {
  backend "gcs" {
    credentials = "../../credentials/terraform-config.json"
    bucket      = "remote-terraform-state-files"
    prefix      = "tf-state-app-ml"
  }
}