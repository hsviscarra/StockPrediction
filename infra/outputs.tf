output "streamlit_fqdn" {
  value = azurerm_container_app.streamlit.latest_revision_fqdn
}