provider "google" {
  credentials = var.gcp_credentials
  project     = var.gcp_project_id
  region      = var.gcp_region
}

provider "azurerm" {
  subscription_id = var.subscription_id
  client_id       = var.serviceprinciple_id
  client_secret   = var.serviceprinciple_key
  tenant_id       = var.tenant_id
  features {}
}

terraform {
  backend "gcs" {
    credentials = "../../../../credentials/gcp-terraform-config.json"
    bucket      = "remote-terraform-state-files"
    prefix      = "tf-state-azure-app-ml"
  }
}