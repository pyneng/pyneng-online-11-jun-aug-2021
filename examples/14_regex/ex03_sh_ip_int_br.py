import re
from pprint import pprint


def parse_sh_ip_int_br(output):
    regex = r"^(\S+) +([\d.]+|unassigned)"

    result_dict = {}

    for line in output.split("\n"):
        m = re.search(regex, line)
        if m:
            intf = m.group(1)
            ip = m.group(2)
            if ip == "unassigned":
                ip = None
            result_dict[intf] = ip
    return result_dict


if __name__ == "__main__":
    with open("sh_ip_int_br.txt", "r") as f:
        content = f.read()
    pprint(parse_sh_ip_int_br(content))
