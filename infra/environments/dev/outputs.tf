output "streamlit_url" {
  value = "https://${data.azurerm_container_app.existing_streamlit.latest_revision_fqdn}"
  description = "URL of the Streamlit application"
}

output "api_url" {
  value = "https://${data.azurerm_container_app.existing_api.latest_revision_fqdn}"
  description = "URL of the API"
}

output "resource_group_name" {
  value = local.resource_group_name
  description = "Name of the resource group"
}

output "container_app_environment_id" {
  value = data.azurerm_container_app_environment.existing.id
  description = "ID of the Container App Environment"
}
