import re
from pprint import pprint

{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825'},
 'R2': {'ios': '2900 Software (C2911-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L'}}

result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = re.search(r"Device ID: (\S+)", line).group(1)
            result[device] = {}
        elif "IP address" in line:
            ip = re.search(r"IP address: (\S+)", line).group(1)
            result[device]["ip"] = ip
        elif line.startswith("Platform"):
            platform = re.search(r"Platform: (.+?),", line).group(1)
            result[device]["platform"] = platform
        elif line.startswith("Cisco IOS"):
            ios = re.search(r"Cisco IOS Software, (.+),", line).group(1)
            result[device]["ios"] = ios
        elif line.startswith("Duplex"):
            duplex = re.search(r"Duplex:: (\S+)", line).group(1)
            result[device]["duplex"] = duplex


pprint(result)
