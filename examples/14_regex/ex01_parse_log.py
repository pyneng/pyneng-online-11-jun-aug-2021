from pprint import pprint
import re

regex = r"Host (\S+) .+ port (\S+) and port (\S+)"

ports = set()

with open("log.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            print(match.groups())
            print(match.group(2, 3))
            ports.update(match.group(2, 3))
print(ports)

