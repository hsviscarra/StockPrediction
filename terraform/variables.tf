variable "resource_group_name" {
  type        = string
  description = "The name of the resource group"
}

variable "location" {
  type        = string
  description = "Azure location to deploy the resources"
  default     = "East US"
}

variable "app_name" {
  type        = string
  description = "Name of the Azure App Service"
}