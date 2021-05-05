import re
import csv

regex = (
    r"Host (\S+) "
    r"in vlan (\d+) "
    r"is flapping between port "
    r"(\S+) and port (\S+)"
)

with open("log.txt") as log, open("result.csv", "w") as dst:
    wr = csv.writer(dst)
    headers = "mac vlan port1 port2".split()
    wr.writerow(headers)
    for line in log:
        match = re.search(regex, line)
        if match:
            wr.writerow(match.groups())
