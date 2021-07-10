from pprint import pprint


def get_intf_ip_dict_from_cfg(filename):
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip

    return intf_ip_dict


r1 = get_intf_ip_dict_from_cfg("config_r1.txt")
pprint(r1)
r2 = get_intf_ip_dict_from_cfg("config_r2.txt")
pprint(r2)

config_list = ["config_r1.txt", "config_r2.txt", "config_r3.txt", "config_sw1.txt"]
for cfg in config_list:
    result = get_intf_ip_dict_from_cfg(cfg)
    pprint(result)
