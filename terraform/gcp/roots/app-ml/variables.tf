variable "gcp_credentials" {
    type = string
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

variable "gke_num_nodes" {
  default     = 1
  description = "number of gke nodes"
}