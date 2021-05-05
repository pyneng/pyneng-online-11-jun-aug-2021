import re

regex = (
    r"Host (\S+) "
    r"in vlan (\d+) .+"
    r"port (\S+) and port (\S+)"
)

ports = set()

with open("log.txt") as f:
    all_match = re.finditer(regex, f.read())
    for m in all_match:
        host, vlan, port1, port2 = m.groups()
        ports.update((port1, port2))

print(ports)
