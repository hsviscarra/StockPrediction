# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags     = var.default_tags
}

# Log Analytics (required for Container App Environment)
resource "azurerm_log_analytics_workspace" "logs" {
  name                = "${var.prefix}-logs"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
  tags                = var.default_tags
}

# Container App Environment
resource "azurerm_container_app_environment" "env" {
  name                       = "${var.prefix}-env"
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.logs.id
  tags                       = var.default_tags
}

# API container app
resource "azurerm_container_app" "api" {
  name                         = "${var.prefix}-api"
  container_app_environment_id = azurerm_container_app_environment.env.id
  resource_group_name          = azurerm_resource_group.rg.name
  revision_mode                = "Single"

  secret {
    name  = "dockerhub-password"
    value = var.dockerhub_password
    }

  registry {
    server   = "index.docker.io"
    username = var.dockerhub_username
    password_secret_name = "dockerhub-password"
    }
    
  template {
    container {
      name   = "api"
      image  = "${var.dockerhub_username}/api:latest"
      cpu    = var.container_cpu
      memory = var.container_memory
    }
  }

  ingress {
    external_enabled = true
    target_port      = 8000
    transport        = "auto"
    traffic_weight {
    latest_revision = true
    percentage      = 100
    }
  }
  tags = var.default_tags
}

# Streamlit container app
resource "azurerm_container_app" "streamlit" {
  name                         = "${var.prefix}-streamlit"
  container_app_environment_id = azurerm_container_app_environment.env.id
  resource_group_name          = azurerm_resource_group.rg.name
  revision_mode                = "Single"

  secret {
    name  = "dockerhub-password"
    value = var.dockerhub_password
    }
  registry {
    server   = "index.docker.io"
    username = var.dockerhub_username
    password_secret_name = "dockerhub-password"
    }

  template {
    container {
      name   = "streamlit"
      image  = "${var.dockerhub_username}/streamlit:latest"
      cpu    = var.container_cpu
      memory = var.container_memory

      env {
        name  = "API_URL"
        value = "http://${azurerm_container_app.api.name}.${azurerm_container_app_environment.env.name}.internal:8000"
      }
    }
  }

  ingress {
    external_enabled = true
    target_port      = 8501
    transport        = "auto"
    traffic_weight {
    latest_revision = true
    percentage      = 100
    }
  }
  tags = {
    environment = "dev"
    project     = "stock-advisor"
  }
}