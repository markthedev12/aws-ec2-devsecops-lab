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
![Terraform Apply Output](<img width="775" height="271" alt="terraform-apply" src="https://github.com/user-attachments/assets/4423c3bc-d99b-4e57-b98a-70d007d7b7c0" />)


### 2. Live Web Server
![Apache Web Server](your-exact-screenshot-name-2.png)

### 3. Boto3 Security Audit
![Python Audit Script](your-exact-screenshot-name-3.png)

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
