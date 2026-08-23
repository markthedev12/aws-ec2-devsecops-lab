# AWS EC2 Web Server Automation & Security Audit ☁️🔒

## Project Overview
This project demonstrates Infrastructure as Code (IaC) and automated cloud security auditing. It provisions a web server on AWS using **Terraform** and validates the compliance of the deployed Security Groups using a custom **Python (Boto3)** script.

This repository proves the ability to:
- Translate cloud architecture into declarative HashiCorp Configuration Language (HCL).
- Bootstrap EC2 instances automatically without manual SSH intervention using \`user_data\`.
- Interact with AWS APIs using Python to enforce DevSecOps security baselines.

---

## 🏗️ Architecture & Tech Stack
- **Cloud Provider:** Amazon Web Services (AWS)
- **Infrastructure as Code:** Terraform (aws_instance, aws_security_group, aws_ami)
- **Configuration Management:** Bash (user_data bootstrapping)
- **Security Auditing:** Python 3.12, AWS SDK for Python (Boto3)
- **Compute:** Amazon Linux 2023 (t3.micro)

---

## 📸 Proof of Execution

### 1. Terraform Deployment Success
![Terraform Apply Output](docs/terraform-apply.png) 
*Outputs showing the public IP and active state resources.*

### 2. Live Web Server
![Apache Web Server](docs/web-server-live.png)
*Browser successfully accessing the Apache web server provisioned via user_data.*

### 3. Boto3 Security Audit
![Python Audit Script](docs/python-audit.png)
*Python script querying security group permissions and auditing open ports.*

---

## 🚀 How to Run the Project

### 1. Prerequisites
- AWS CLI configured with administrator access (\`aws configure\`)
- Terraform installed
- Python 3.12+ and Boto3 installed (\`pip install boto3\`)

### 2. Deploy Infrastructure
\`\`\`bash
terraform init
terraform plan
terraform apply --auto-approve
\`\`\`

### 3. Run Security Audit
\`\`\`bash
python audit_ec2.py
\`\`\`

### 4. Clean Up
\`\`\`bash
terraform destroy --auto-approve
\`\`\`
"@
