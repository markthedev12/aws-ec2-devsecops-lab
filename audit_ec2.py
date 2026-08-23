import boto3

ec2 = boto3.client('ec2', region_name='us-east-2')

def audit_security_groups():
    print("=== RUNNING EC2 SECURITY GROUP AUDIT ===")
    response = ec2.describe_security_groups()

    for sg in response['SecurityGroups']:
        sg_name = sg['GroupName']
        sg_id = sg['GroupId']
        
        for rule in sg.get('IpPermissions', []):
            from_port = rule.get('FromPort', 'All')
            to_port = rule.get('ToPort', 'All')
            ip_ranges = [ip['CidrIp'] for ip in rule.get('IpRanges', [])]

            if "0.0.0.0/0" in ip_ranges:
                if from_port == 22 or to_port == 22:
                    print(f"[CRITICAL] SSH (Port 22) exposed to 0.0.0.0/0 in SG: {sg_name} ({sg_id})")
                elif from_port == 80:
                    print(f"[INFO] HTTP (Port 80) open to Internet in SG: {sg_name} ({sg_id}) - Expected for Web")

if __name__ == "__main__":
    audit_security_groups()