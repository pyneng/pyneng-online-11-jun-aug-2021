from tabulate import tabulate
from pprint import pprint
import re

result = []
regex = (
    r"(\S+) +([\d.]+) +" # interface and IP
    r"\w+ +\w+ +" # trash
    r"(up|down) +(up|down)" # status, protocol
)
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            result.append(match.groups())

pprint(result)


result = {}
regex = (
    r"^(\S+) +([\d.]+) +" # interface and IP
)
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            intf, ip = match.group(1, 2)
            result[intf] = ip

pprint(result)
