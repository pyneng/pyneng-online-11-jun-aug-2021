from pprint import pprint
result = {
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
}

result_dict = {}

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        # if line_list:
        #    str_index_0 = line_list[0]
        #    if str_index_0[-1].isdigit():
        if line_list and line_list[0][-1].isdigit():
            intf, ip = line_list[:2]
            # intf = line_list[0]
            # ip = line_list[1]
            if ip == "unassigned":
                ip = None
            result_dict[intf] = ip

pprint(result_dict)
for intf, ip in result_dict.items():
    if not ip:
        print(intf)
