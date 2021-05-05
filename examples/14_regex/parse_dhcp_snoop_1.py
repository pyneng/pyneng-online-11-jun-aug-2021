import re
from pprint import pprint


def parse_dhcp_snooping(filename):
    result = []
    regex = (
        r"(?P<mac>\S+) +(?P<ip>\S+) +"
        r"\d+ +\S+ +"
        r"(?P<vlan>\d+) +(?P<intf>\S+)"
    )
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groupdict())
    return result


if __name__ == "__main__":
    output = parse_dhcp_snooping("dhcp_snooping.txt")
    pprint(output)
    for data_dict in output:
        print(data_dict["ip"])
