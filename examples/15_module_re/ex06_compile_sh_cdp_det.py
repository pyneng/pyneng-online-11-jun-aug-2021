import re
from pprint import pprint


def parse_cdp(output):
    regex = re.compile(
        r"Device ID: (?P<device>\S+)"
        r".*?"
        r"IP address: (?P<ip>\S+)\s+"
        r"Platform: (?P<platform>.+?),"
        r".*?"
        r"^Cisco IOS Software, (?P<ios>.+?), RELEASE",
        re.DOTALL | re.MULTILINE | re.ASCII,
    )
    result = {}
    m_all = regex.finditer(output)
    for m in m_all:
        m_dict = m.groupdict()
        device = m_dict.pop("device")
        result[device] = m_dict
    return result


if __name__ == "__main__":
    with open("sh_cdp_neighbors_sw1.txt") as f:
        content = f.read()

    pprint(parse_cdp(content))
