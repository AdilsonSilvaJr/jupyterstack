provider "google" {
  credentials = "../../credentials/terraform-config.json"
  project     = var.project
  region      = var.region
}

terraform {
  backend "gcs" {
    credentials = "../../credentials/terraform-config.json"
    bucket      = "remote-terraform-state-files"
    prefix      = "tf-state-storage"
  }
}