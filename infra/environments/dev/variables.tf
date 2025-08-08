variable "resource_group_name" {
  type        = string
  default     = "stockanalytics-rg"
  description = "Name of the resource group"
}

variable "create_resource_group" {
  type        = bool
  default     = false
  description = "Whether to create the resource group or use existing one"
}

variable "location" {
  type        = string
  default     = "eastus"
  description = "Azure region for resources"
}

variable "prefix" {
  type        = string
  default     = "stockanalytics"
  description = "Prefix for resource names"
}

variable "dockerhub_username" {
  type        = string
  description = "Docker Hub username"
}

variable "dockerhub_password" {
  type        = string
  description = "Docker Hub password"
  sensitive   = true
}

variable "container_cpu" {
  type        = number
  default     = 0.25
  description = "CPU allocation for containers"
}

variable "container_memory" {
  type        = string
  default     = "0.5Gi"
  description = "Memory allocation for containers"
}

variable "default_tags" {
  type        = map(string)
  description = "Default tags to apply to all resources"
  default = {
    environment = "dev"
    project     = "stock-advisor"
    managed_by  = "terraform"
  }
}
