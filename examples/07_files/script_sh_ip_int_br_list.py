from pprint import pprint
result = {
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
}

result_list = []

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        # if len(line_list != 0):
        # if line_list:
        #    str_index_0 = line_list[0]
        #    if str_index_0[-1].isdigit():
        if line_list and line_list[0][-1].isdigit():
            intf_ip_list = line_list[:2]
            result_list.append(intf_ip_list)

pprint(result_list)
