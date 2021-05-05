from pprint import pprint

result = {}

with open("sh_ip_interface.txt") as f:
    for line in f:
        line_list = line.split()
        if "line protocol" in line:
            intf = line_list[0]
            print(intf)
            result[intf] = {}
        elif "Internet address" in line:
            ip = line_list[-1]
            print(ip)
            result[intf]["ip"] = ip

        elif "MTU is" in line:
            mtu = line_list[-2]
            print(mtu)
            result[intf]["mtu"] = mtu


pprint(result)

{'Ethernet0/0': {'ip': '192.168.100.1/24', 'mtu': '1500'},
 'Ethernet0/1': {'ip': '192.168.200.1/24', 'mtu': '1500'},
 'Ethernet0/2': {'ip': '19.1.1.1/24', 'mtu': '1500'},
 'Ethernet0/3': {'ip': '192.168.230.1/24', 'mtu': '1500'},
 'Loopback0': {'ip': '4.4.4.4/32', 'mtu': '1514'}}
