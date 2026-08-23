terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

# 1. Fetch the latest official Amazon Linux 2023 AMI dynamically
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

# 2. Security Group: Allow HTTP (Port 80) from anywhere, and all outbound
resource "aws_security_group" "web_sg" {
  name        = "mark-web-server-sg"
  description = "Allow HTTP inbound traffic"

  ingress {
    description = "HTTP from Internet"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "mark-web-server-sg"
  }
}

# 3. Provision Free-Tier EC2 Instance with User Data Web Server
resource "aws_instance" "web_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro" # Free Tier eligible in us-east-2
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # User Data Script: Runs automatically on first boot
  user_data = <<-EOF
              #!/bin/bash
              dnf update -y
              dnf install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Cloud Engineering Lab: Deployed via Terraform</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name        = "Mark-Lab-WebServer"
    Environment = "Dev"
  }
}

# 4. Terraform Outputs: Prints the public URL right in your terminal
output "server_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web_server.public_ip
}

output "web_url" {
  description = "URL to access the web server"
  value       = "http://${aws_instance.web_server.public_ip}"
}