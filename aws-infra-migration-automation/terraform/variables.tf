variable "region" {
  description = "AWS region for resource deployment"
  default     = "us-east-1"
}

variable "ami_id" {
  description = "Amazon Machine Image ID for EC2 instance"
  default     = "ami-xxxxxxxxxxxx"
}

variable "db_user" {
  description = "Database username"
  default     = "admin"
}

variable "db_pass" {
  description = "Database password"
  default     = "admin1234"
}
