terraform {
  backend "gcs" {
    bucket = "cicd-dilun-demo"
    prefix = "terraform/edge"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.14.1"
    }

    google-beta = {
      source  = "hashicorp/google-beta"
      version = "6.14.1"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

provider "google-beta" {
  project = var.project
  region  = var.region
}

data "google_project" "project" {

}

data "google_client_config" "default" {
  depends_on = [data.google_project.project]
}

resource "google_project_service" "enable_api" {
  for_each = toset(
    [
      "logging.googleapis.com",
      "artifactregistry.googleapis.com",
      "run.googleapis.com",
      "iamcredentials.googleapis.com",
    ]
  )

  service = each.key

  timeouts {
    create = "30m"
    update = "40m"
  }

  disable_on_destroy = false
  depends_on         = [data.google_client_config.default]
}
