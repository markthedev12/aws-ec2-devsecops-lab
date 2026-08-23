# AWS EC2 Web Server Automation & Security Audit ☁️🔒

## Project Overview
This project demonstrates Infrastructure as Code (IaC) and automated cloud security auditing. It provisions an automated web server on AWS using **Terraform** and validates the compliance of the deployed Security Groups using a custom **Python (Boto3)** script.

This repository proves the ability to:
- Translate cloud architecture into declarative HashiCorp Configuration Language (HCL).
- Bootstrap EC2 instances automatically without manual SSH intervention using `user_data`.
- Interact with AWS APIs using Python to enforce DevSecOps security baselines.

---

## 🏗️ Architecture & Tech Stack
- **Cloud Provider:** Amazon Web Services (AWS)
- **Infrastructure as Code:** Terraform (`aws_instance`, `aws_security_group`, `data.aws_ami`)
- **Configuration Management:** Bash (`user_data` bootstrapping)
- **Security Auditing:** Python 3.12, AWS SDK for Python (`boto3`)
- **Compute:** Amazon Linux 2023 (`t3.micro`)

---

## 📸 Proof of Execution

### 1. Terraform Deployment & State Output
<img width="775" height="271" alt="terraform-apply" src="https://github.com/user-attachments/assets/0f6ba5c5-cc97-46a3-9dc4-e7824636f00b" />

*Terraform output displaying dynamic public IP assignment and tracked state resources.*

### 2. Live Web Server Verification
<img width="735" height="116" alt="web-server-live" src="https://github.com/user-attachments/assets/dff3a7ef-8315-409f-9be8-04a50e5a420b" />

*Browser confirmation reaching the Apache web server provisioned dynamically via user_data.*

### 3. Automated Security Group Audit
<img width="784" height="152" alt="python-audit" src="https://github.com/user-attachments/assets/33bbfcfa-65c0-4c84-baf4-0f85dc048a75" />

*Custom Python script auditing AWS Security Groups to identify and report public internet exposures.*

---

## 🚀 How to Run the Project

### 1. Prerequisites
- AWS CLI configured with active credentials (`aws configure`)
- Terraform installed
- Python 3.12+ and Boto3 installed (`pip install boto3`)

### 2. Deploy the Infrastructure
```bash
terraform init
terraform plan
terraform apply --auto-approve
