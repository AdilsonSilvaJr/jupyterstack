variable "serviceprinciple_id" {}

variable "serviceprinciple_key" {}

variable "tenant_id" {}

variable "subscription_id" {}

variable "ssh_key" {}

variable "location" {
  default = "centralus"
}

variable "kubernetes_version" {
  default = "1.22.2"
}

variable "gcp_credentials" {
  type        = string
  description = "Location GCP credentials"
}

variable "gcp_project_id" {
  type        = string
  description = "Project name"
}

variable "gcp_region" {
  type        = string
  description = "Region name"
}