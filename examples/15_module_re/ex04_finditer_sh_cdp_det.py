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

regex_without_dotall = (
    r"Device ID: (?P<device>\S+)\n"
    r".*\n"
    r" +IP address: (?P<ip>\S+)\n"
    r"Platform: (?P<platform>.+?),.*\n"
    r"(?:.*\n)+?"
    r"Cisco IOS Software, (?P<ios>.+),"
)

regex = (
    r"Device ID: (?P<device>\S+)"
    r".*?"
    r"IP address: (?P<ip>\S+)\s+"
    r"Platform: (?P<platform>.+?),"
    r".*?"
    r"^Cisco IOS Software, (?P<ios>.+?), RELEASE"
)
result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    content = f.read()
    m_all = re.finditer(
        regex, content, re.DOTALL | re.MULTILINE | re.ASCII
    )
    for m in m_all:
        m_dict = m.groupdict()
        device = m_dict.pop("device")
        result[device] = m_dict


pprint(result)
('SW1#show cdp neighbors detail\n'
 '-------------------------\n'
 'Device ID: SW2\n'
 'Entry address(es):\n'
 '  IP address: 10.1.1.2\n'
 'Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP\n'
 'Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1\n'
 'Holdtime : 164 sec\n'
 '\n'
 'Version :\n'
 'Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)\n'
)
