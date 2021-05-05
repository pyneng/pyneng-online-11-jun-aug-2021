from pprint import pprint
import re


def parse_cdp_file(filename):
    regex = re.compile(
        r"Device ID: (?P<hostname>.+)\n"
        r".+\n"
        r" +IP address: (?P<ip>\S+)\n"
        r"Platform: (?P<platform>.+?), .+\n"
        r"Interface: (?P<local_port>\S+), .+: (?P<remote_port>\S+)\n"
        r"(.*\n)+?"
        r"Cisco IOS Software, (?P<ios>.+), RELEASE .+\n"
        r"(.*\n)+?"
        r"advertisement version: (?P<vtp_version>\d+)"
    )
    result_dict = {}
    with open(filename) as f:
        match_all = regex.finditer(f.read())
        for match in match_all:
            n_dict = match.groupdict()
            hostname = n_dict.pop("hostname")
            result_dict[hostname] = n_dict
    return result_dict




if __name__ == "__main__":
    result = parse_cdp_file("sh_cdp_neighbors_sw1.txt")
    pprint(result)
