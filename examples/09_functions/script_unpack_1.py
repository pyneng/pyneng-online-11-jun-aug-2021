from pprint import pprint
with open("sh_ip_int_br.txt") as f:
    result = []
    for line in f:
        line_list = line.split()
        if line_list:
            intf, ip, *_, st, prot = line_list
            result.append([intf, ip, st, prot])

pprint(result)
