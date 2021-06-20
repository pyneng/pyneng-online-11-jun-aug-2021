from pprint import pprint

result = {}

with open("sh_ip_interface.txt") as f:
    for line in f:
        words = line.split()
        if "line protocol is" in line:
            intf = words[0]
        elif "MTU is" in line:
            mtu = words[2]
            result[intf] = mtu

pprint(result)
