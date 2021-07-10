from pprint import pprint
{
    "Ethernet0/0": {"mtu": 1500, "ip": "192.168.100.1/24"},
    "Ethernet0/1": {"mtu": 1500, "ip": "192.168.200.1/24"},
}

result = {}

with open("sh_ip_interface2.txt") as f:
    for line in f:
        line = line.rstrip()
        if "line protocol" in line:
            #print(line)
            intf = line.split()[0]
        elif "Internet address" in line:
            ip_address = line.split()[-1]
            result[intf] = {}
            result[intf]["ip"] = ip_address
        elif "MTU" in line:
            mtu = line.split()[2]
            result[intf]["mtu"] = mtu

pprint(result)
print("="*50)
for intf, params in result.items():
    if params:
        print(intf)
        pprint(params)
