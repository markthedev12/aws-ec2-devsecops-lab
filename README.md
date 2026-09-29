# AWS EC2 DevSecOps Lab

Terraform provisions an EC2 web server on AWS, then a Python (boto3) script audits the deployed security groups and flags public internet exposure.

> Personal lab project.

## What it does

1. **Provision.** Terraform creates an Amazon Linux 2023 instance and its security group. A `user_data` script bootstraps the Apache web server automatically, so no manual SSH is needed.
2. **Audit.** `audit_ec2.py` uses boto3 to inspect the deployed security groups and report rules that expose resources to the public internet.

## Skills demonstrated

* Translating cloud architecture into declarative HashiCorp Configuration Language (HCL)
* Bootstrapping EC2 instances without manual SSH using `user_data`
* Using the AWS API from Python to enforce a security baseline

## Tech stack

* **Cloud provider:** Amazon Web Services
* **Infrastructure as code:** Terraform (`aws_instance`, `aws_security_group`, `data.aws_ami`)
* **Bootstrapping:** Bash in `user_data`
* **Security auditing:** Python 3.12, AWS SDK for Python (`boto3`)
* **Compute:** Amazon Linux 2023 (`t3.micro`)

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
```

### 3. Run the audit
```bash
pip install boto3
python audit_ec2.py
```

### 4. Clean up
```bash
terraform destroy
```
Run this when you are finished so the instance does not keep running and incurring charges.

---

## What the audit reports

Security group rules that expose resources to the public internet (`0.0.0.0/0`). Port 80 open to the world is expected for a public web server. Management ports such as SSH (22) and RDP (3389) open to the world are the findings that matter.

## What I would do next

- [ ] Run `terraform fmt`, `validate` and Checkov in GitHub Actions
- [ ] Output audit results as JSON and Markdown
- [ ] Exit with a failing status when risky rules are found, so CI can block on it
- [ ] Add variables and outputs files so the configuration is reusable

## Author

Mark Schwinn · [Website](https://markschwinn.com) · [LinkedIn](https://www.linkedin.com/in/mark-schwinn-994625362/)
