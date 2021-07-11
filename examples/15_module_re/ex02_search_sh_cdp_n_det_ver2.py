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

regex = (
    r"Device ID: (?P<device>\S+)"
    r"|IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+?),"
    r"|Cisco IOS Software, (?P<ios>.+),"
    r"|Duplex: (?P<duplex>\S+)"
    r"|Interface: (?P<local_port>\S+), .+: (?P<remote_port>\S+)"
)


result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            group = match.lastgroup
            value = match.group(group)
            if group == "device":
                result[value] = {}
                device = value
            elif group == "remote_port":
                result[device][group] = value
                result[device]["local_port"] = match.group("local_port")
            else:
                result[device][group] = value
            # elif group == "ip":
            #     result[device]["ip"] = value
            # elif group == "platform":
            #     result[device]["platform"] = value
            # elif group == "ios":
            #     result[device]["ios"] = value

pprint(result)
