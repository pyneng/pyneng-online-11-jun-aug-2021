import re
from pprint import pprint


def parse_cdp(output):
    regex = (
        r"Device ID: (?P<device>\S+)\n"
        r".*\n"
        r" +IP address: (?P<ip>\S+)\n"
        r"Platform: (?P<platform>.+?),.*\n"
        r"(?:.*\n)+?"
        r"Cisco IOS Software, (?P<ios>.+),"
    )
    result = {}
    m_all = re.finditer(regex, output)
    for m in m_all:
        m_dict = m.groupdict()
        device = m_dict.pop("device")
        result[device] = m_dict
    return result


if __name__ == "__main__":
    with open("sh_cdp_neighbors_sw1.txt") as f:
        content = f.read()

    pprint(parse_cdp(content))
