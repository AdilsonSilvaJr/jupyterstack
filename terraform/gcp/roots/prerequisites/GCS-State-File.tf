resource "google_storage_bucket" "bucket-state" {
  name = "remote-terraform-state-files"
  location = "US"
}