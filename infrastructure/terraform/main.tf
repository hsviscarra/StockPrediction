terraform {
  backend "s3" {
    bucket = "mlops-stock-advisor-terraform-state"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}

module "mlops_infrastructure" {
  source = "../.."

  project_name = "mlops-stock-advisor"
  environment  = "dev"
  aws_region   = "us-east-1"

  vpc_cidr               = "10.0.0.0/16"
  public_subnet_cidrs    = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs   = ["10.0.10.0/24", "10.0.20.0/24"]

  db_username    = "mlops_user"
  db_password    = var.db_password
  key_pair_name  = "mlops-dev-key"

  instance_type       = "t3.micro"
  db_instance_class   = "db.t3.micro"
  enable_monitoring   = false
  enable_deletion_protection = false

  tags = {
    Environment = "dev"
    Project     = "mlops-stock-advisor"
    ManagedBy   = "terraform"
  }
}

---
# terraform/environments/dev/variables.tf
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

---
# terraform/environments/dev/outputs.tf
output "vpc_id" {
  description = "ID of the VPC"
  value       = module.mlops_infrastructure.vpc_id
}

output "mlflow_tracking_uri" {
  description = "MLflow tracking URI"
  value       = module.mlops_infrastructure.mlflow_tracking_uri
}

output "streamlit_app_url" {
  description = "Streamlit app URL"
  value       = module.mlops_infrastructure.streamlit_app_url
}

output "rds_endpoint" {
  description = "RDS instance endpoint"
  value       = module.mlops_infrastructure.rds_endpoint
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket for MLflow artifacts"
  value       = module.mlops_infrastructure.s3_bucket_name
}
