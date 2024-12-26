variable "project" {
  description = "The GCP project id"
  default     = "demo-cicd"
  type        = string
}

variable "region" {
  description = "The GCP region for this project"
  default     = "asia-south1"
  type        = string
}
