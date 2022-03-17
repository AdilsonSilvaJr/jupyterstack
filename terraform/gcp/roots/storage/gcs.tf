resource "google_storage_bucket" "bucket-state" {
  name = "bucket-diabetes"
  location = "US-CENTRAL1"
}

resource "google_storage_bucket" "bucket-diabetes-ml" {
  name = "bucket-diabetes-ml"
  location = "US-CENTRAL1"
}