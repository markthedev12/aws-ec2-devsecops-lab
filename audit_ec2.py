"""Read-only security-group audit; exit 1 for public management access."""
import argparse
import json

MANAGEMENT_PORTS = (22, 3389)

def evaluate_security_group(group):
    findings = []
    for rule in group.get("IpPermissions", []):
        public = [entry.get("CidrIp") for entry in rule.get("IpRanges", [])
                  if entry.get("CidrIp") == "0.0.0.0/0"]
        public += [entry.get("CidrIpv6") for entry in rule.get("Ipv6Ranges", [])
                   if entry.get("CidrIpv6") == "::/0"]
        protocol = rule.get("IpProtocol")
        ports = MANAGEMENT_PORTS if protocol == "-1" else (
            [port for port in MANAGEMENT_PORTS
             if rule.get("FromPort", -1) <= port <= rule.get("ToPort", -1)]
            if protocol in ("tcp", "6") else []
        )
        for cidr in public:
            for port in ports:
                findings.append({"group_id": group["GroupId"],
                                 "group_name": group.get("GroupName", ""),
                                 "port": port, "cidr": cidr,
                                 "severity": "critical"})
    return findings

def audit_security_groups(client):
    return [finding
            for page in client.get_paginator("describe_security_groups").paginate()
            for group in page.get("SecurityGroups", [])
            for finding in evaluate_security_group(group)]

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", default="us-east-2")
    args = parser.parse_args(argv)
    import boto3
    from botocore.exceptions import BotoCoreError, ClientError
    try:
        findings = audit_security_groups(boto3.client("ec2", region_name=args.region))
    except (BotoCoreError, ClientError) as error:
        parser.exit(2, f"Audit could not complete: {error}\n")
    print(json.dumps({"region": args.region, "findings": findings}, indent=2))
    return 1 if findings else 0

if __name__ == "__main__":
    raise SystemExit(main())
