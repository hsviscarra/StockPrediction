output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.mlops_vpc.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public_subnets[*].id
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = aws_subnet.private_subnets[*].id
}

output "rds_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.mlops_db.endpoint
}

output "rds_port" {
  description = "RDS instance port"
  value       = aws_db_instance.mlops_db.port
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket for MLflow artifacts"
  value       = aws_s3_bucket.mlflow_artifacts.bucket
}

output "s3_bucket_arn" {
  description = "ARN of the S3 bucket for MLflow artifacts"
  value       = aws_s3_bucket.mlflow_artifacts.arn
}

output "mlflow_server_ip" {
  description = "Public IP of the MLflow server"
  value       = aws_instance.mlflow_server.public_ip
}

output "streamlit_app_ip" {
  description = "Public IP of the Streamlit app"
  value       = aws_instance.streamlit_app.public_ip
}

output "mlflow_tracking_uri" {
  description = "MLflow tracking URI"
  value       = "http://${aws_instance.mlflow_server.public_ip}:5000"
}

output "streamlit_app_url" {
  description = "Streamlit app URL"
  value       = "http://${aws_instance.streamlit_app.public_ip}:8501"
}

output "security_group_id" {
  description = "ID of the main security group"
  value       = aws_security_group.mlops_sg.id
}

output "iam_role_arn" {
  description = "ARN of the IAM role for EC2 instances"
  value       = aws_iam_role.ec2_role.arn
}

output "cloudwatch_log_group_name" {
  description = "Name of the CloudWatch log group"
  value       = aws_cloudwatch_log_group.mlops_logs.name
}