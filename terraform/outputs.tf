output "app_service_url" {
  description = "The default URL for the Azure App Service"
  value       = "https://${azurerm_app_service.app.default_site_hostname}"
}