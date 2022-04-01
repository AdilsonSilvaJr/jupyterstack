resource "google_storage_bucket" "bucket-state" {
  name = "bucket-diabetes"
  location = var.gcp_region
}

resource "google_storage_bucket" "bucket-diabetes-ml" {
  name = "bucket-diabetes-ml"
  location = var.gcp_region
}

resource "google_storage_bucket" "bucket-diabetes-analytics" {
  name = "bucket-diabetes-analytics"
  location = var.gcp_region
}