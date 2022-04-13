terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.13.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.1.0"
    }
  }

  required_version = ">= 0.14"
}