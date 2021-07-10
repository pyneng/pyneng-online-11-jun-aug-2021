from pprint import pprint
import re


regex = r"^(\S+) *([A-Z]\S+ \S+) +\d+ .+ (\S+ \S+)$"

with open("sh_cdp_n_sw1.txt") as f:
    for line in f:
        m = re.search(regex, line)
        if m:
            print(m.groups())
