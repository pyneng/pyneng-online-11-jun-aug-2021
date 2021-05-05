from pprint import pprint
import re


def parse_cdp_file(filename):
    regex = (
        r"Device ID: (?P<hostname>.+)"
        r"|IP address: (?P<ip>\S+)"
        r"|Platform: (?P<platform>.+?),"
        r"|Interface: (?P<local_port>\S+), .+: (?P<remote_port>\S+)"
        r"|Cisco IOS Software, (?P<ios>.+), RELEASE"
        r"|advertisement version: (?P<vtp_version>\d+)"
    )
    result_dict = {}
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                last_group = match.lastgroup
                if last_group == "hostname":
                    hostname = match.group("hostname")
                    result_dict[hostname] = {}
                elif last_group == "remote_port":
                    result_dict[hostname]["remote_port"] = match.group("remote_port")
                    result_dict[hostname]["local_port"] = match.group("local_port")
                else:
                    group_value = match.group(last_group)
                    result_dict[hostname][last_group] = group_value
    return result_dict




if __name__ == "__main__":
    result = parse_cdp_file("sh_cdp_neighbors_sw1.txt")
    pprint(result)
