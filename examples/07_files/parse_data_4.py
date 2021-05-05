from pprint import pprint


files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

result = {}

for filename in files:
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
                print(hostname)
                result[hostname] = {}
            elif line.startswith("interface"):
                intf = line.split()[-1]
                print(intf)
                result[hostname][intf] = None
            elif line.strip().startswith("description"):
                desc = line.strip().lstrip("description ")
                # result[hostname][intf] = desc
                del result[hostname][intf]


pprint(result)

{
    "PE_r1": {
        "Ethernet0/2": "To P_r9 Ethernet0/2",
        "Tunnel0": None,
        }
}
