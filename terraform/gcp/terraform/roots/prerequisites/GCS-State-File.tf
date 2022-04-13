resource "google_storage_bucket" "bucket-state" {
  name          = "remote-terraform-state-files"
  location      = var.gcp_region
  force_destroy = false
}