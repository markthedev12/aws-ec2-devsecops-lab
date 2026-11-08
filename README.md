# AWS EC2 DevSecOps Lab

Terraform provisions an Amazon Linux/Apache web server; a Python CLI checks
security groups for internet-wide SSH and RDP exposure. A focused cloud lab,
not a production web hosting architecture.

## Architecture

`Terraform -> EC2 + security group -> Apache on HTTP/80`

`AWS EC2 API -> paginated collector -> pure rule evaluator -> JSON findings`

The web server uses user data rather than SSH for setup. Terraform currently
relies on the account's default VPC and an automatically selected Amazon Linux
2023 AMI. HTTP is deliberate lab scope; TLS, explicit networking, IMDS settings,
and operating-system hardening remain future work.

## Test without AWS

Python 3.12+ is sufficient for unit tests; they use a fake client.

```sh
python -m unittest discover -s tests -v
```

Coverage includes IPv4/IPv6, all-protocol ingress, TCP port ranges, RDP, private
CIDRs, expected HTTP traffic, and findings on later result pages. CI runs the
same suite. These tests do not prove a live instance is reachable or secure.

## Deploy and audit

Requires Terraform, AWS credentials authorized to provision the lab, a default
VPC in us-east-2, Python, and Boto3. Review costs before creating resources;
instance type eligibility does not guarantee a free deployment.

```sh
terraform init
terraform fmt -check
terraform validate
terraform plan -out=lab.tfplan
terraform apply lab.tfplan
python -m pip install -r requirements.txt
python audit_ec2.py --region us-east-2
```

The auditor needs `ec2:DescribeSecurityGroups`; it does not modify AWS resources.
It uses the standard AWS credential chain. It emits JSON and exits 0 with no
management exposure, 1 with findings, or 2 if collection fails. Rules covering
TCP/22 or TCP/3389 from `0.0.0.0/0` or `::/0`, including all-protocol rules,
produce critical findings. HTTP/80 is not a management finding.

## Verify and clean up

Visit the `web_url` Terraform output and confirm Apache responds. Compare JSON
findings with the security-group configuration. Absence of findings is limited
to these two ports; network routes, NACLs, prefix lists, credentials, and every
other service are outside this checker.

```sh
terraform plan -destroy
terraform destroy
```

Confirm the instance is terminated after cleanup. Do not commit plans, state,
credentials, or real account reports. `main.tf` contains infrastructure;
`audit_ec2.py` contains collection/evaluation; `tests/` documents expected rules.

Next: explicit VPC/subnets, HTTPS, broader configurable checks, and policy scans.
Contributions should add a failing rule fixture before changing audit behavior.
