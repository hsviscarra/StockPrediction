variable "resource_group_name" {
  type    = string
  default = "stockanalytics-rg"
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "prefix" {
  type    = string
  default = "stockanalytics"
}

variable "dockerhub_username" {
  type = string
}

variable "dockerhub_password" {
  type = string
}

variable "container_cpu" {
  type    = number
  default = 0.25
}

variable "container_memory" {
  type    = string
  default = "0.5Gi"
}

variable "default_tags" {
  type = map(string)
  default = {
    environment = "dev"
    project     = "stock-advisor"
  }
}