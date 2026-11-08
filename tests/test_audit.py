import unittest
from unittest.mock import Mock
from audit_ec2 import evaluate_security_group, audit_security_groups

def group(rule):
    return {"GroupId": "sg-demo", "IpPermissions": [rule]}

class AuditTests(unittest.TestCase):
    def test_range_contains_ssh_and_ipv6(self):
        rule = {"IpProtocol": "tcp", "FromPort": 1, "ToPort": 100,
                "Ipv6Ranges": [{"CidrIpv6": "::/0"}]}
        self.assertEqual([f["port"] for f in evaluate_security_group(group(rule))], [22])

    def test_all_protocols_include_both_management_ports(self):
        rule = {"IpProtocol": "-1", "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}
        self.assertEqual({f["port"] for f in evaluate_security_group(group(rule))}, {22, 3389})

    def test_http_private_and_udp_are_not_tcp_management_findings(self):
        for protocol, port, cidr in [("tcp", 80, "0.0.0.0/0"),
                                     ("tcp", 22, "10.0.0.0/8"),
                                     ("udp", 22, "0.0.0.0/0")]:
            rule = {"IpProtocol": protocol, "FromPort": port, "ToPort": port,
                    "IpRanges": [{"CidrIp": cidr}]}
            self.assertEqual(evaluate_security_group(group(rule)), [])

    def test_pagination_includes_later_pages(self):
        client = Mock()
        rule = {"IpProtocol": "6", "FromPort": 3389, "ToPort": 3389,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}
        client.get_paginator.return_value.paginate.return_value = [
            {"SecurityGroups": []}, {"SecurityGroups": [group(rule)]}]
        self.assertEqual(len(audit_security_groups(client)), 1)
        client.get_paginator.assert_called_once_with("describe_security_groups")
