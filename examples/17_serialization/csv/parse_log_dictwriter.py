import re
import csv

regex = (
    r"Host (?P<mac>\S+) "
    r"in vlan (?P<vlan>\d+) "
    r"is flapping between port "
    r"(?P<port1>\S+) and port (?P<port2>\S+)"
)

with open("log.txt") as log, open("result.csv", "w") as dst:
    wr = csv.DictWriter(dst, fieldnames="mac vlan port1 port2".split())
    wr.writeheader()
    for line in log:
        match = re.search(regex, line)
        if match:
            wr.writerow(match.groupdict())

