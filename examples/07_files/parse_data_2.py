result = {}

with open("sh_ip_interface.txt") as f:
    for line in f:
        if "line protocol" in line:
            intf = line.split()[0]
        elif "MTU is" in line:
            mtu = line.split()[-2]
            print(intf, mtu)
            result[intf] = mtu

print(result)

{'Ethernet0/0': '1500',
 'Ethernet0/1': '1500',
 'Ethernet0/2': '1500',
 'Ethernet0/3': '1500',
 'Loopback0': '1514'}

