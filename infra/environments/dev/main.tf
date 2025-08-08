terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.81.0"
    }
  }
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

# Handle existing resource group gracefully
data "azurerm_resource_group" "existing" {
  count = var.create_resource_group ? 0 : 1
  name  = var.resource_group_name
}

resource "azurerm_resource_group" "new" {
  count    = var.create_resource_group ? 1 : 0
  name     = var.resource_group_name
  location = var.location
  tags     = var.default_tags
}

locals {
  resource_group_name     = var.create_resource_group ? azurerm_resource_group.new[0].name : data.azurerm_resource_group.existing[0].name
  resource_group_location = var.create_resource_group ? azurerm_resource_group.new[0].location : data.azurerm_resource_group.existing[0].location
}

# PURE DATA SOURCES - NO RESOURCES AT ALL
data "azurerm_log_analytics_workspace" "existing" {
  name                = "${var.prefix}-logs"
  resource_group_name = local.resource_group_name
}

data "azurerm_container_app_environment" "existing" {
  name                = "${var.prefix}-env"
  resource_group_name = local.resource_group_name
}

data "azurerm_container_app" "existing_api" {
  name                = "${var.prefix}-api"
  resource_group_name = local.resource_group_name
}

data "azurerm_container_app" "existing_streamlit" {
  name                = "${var.prefix}-streamlit"
  resource_group_name = local.resource_group_name
}
