from pprint import pprint
import re

{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825'},
 'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L'}}


def parse_cdp_file(filename):
    result_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("Device ID"):
                hostname = re.search(r"Device ID: (.+)", line).group(1)
                result_dict[hostname] = {}
            elif "IP address:" in line:
                ip_address = re.search(r"IP address: (\S+)", line).group(1)
                result_dict[hostname]["ip"] = ip_address
            elif line.startswith("Platform:"):
                platform = re.search(r"Platform: (.+?),", line).group(1)
                result_dict[hostname]["platform"] = platform
            elif line.startswith("Cisco IOS Software"):
                ios = re.search(r"Cisco IOS Software, (.+), RELEASE", line).group(1)
                result_dict[hostname]["ios"] = ios

    return result_dict




if __name__ == "__main__":
    result = parse_cdp_file("sh_cdp_neighbors_sw1.txt")
    pprint(result)
