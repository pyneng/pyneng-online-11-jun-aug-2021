import re
from pprint import pprint


def parse_cdp(filename):
    result = []
    regex = (
        r"^(\S+) +(\S+ [\d/]+) +\d+.+ +(\S+ [\d/]+)$"
    )
    with open(filename) as f:
        for line in f:
            match_host = re.search(r"^(\S+)[>#]", line)
            match_n = re.search(regex, line)
            if match_host:
                hostname = match_host.group(1)
            elif match_n:
                #result.append((hostname, *match_n.group(2, 1, 3)))
                l_intf, remote_d, remote_int = match_n.group(2, 1, 3)
                result.append((hostname, l_intf, remote_d, remote_int))
    return result


if __name__ == "__main__":
    output = parse_cdp("sh_cdp_n_sw1.txt")
    pprint(output)
