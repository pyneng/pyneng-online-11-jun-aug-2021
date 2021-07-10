import re
from pprint import pprint

result_list = []

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0][-1].isdigit():
            intf_ip_list = line_list[:2] + line_list[-2:]
            result_list.append(intf_ip_list)

#pprint(result_list)
[['FastEthernet0/0', '15.0.15.1', 'up', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'up', 'up'],
 ['FastEthernet0/3', 'unassigned', 'up', 'up'],
 ['Loopback0', '10.1.1.1', 'up', 'up'],
 ['Loopback100', '100.0.0.1', 'up', 'up']]


def parse_sh_ip_int_br(output):
    # regex = r"(\S+) +([\d.]+|unassigned) +\S+ +\w+ +(\S+) +(\S+)"
    regex = (
        r"(\S+) +" # интерфейс
        r"([\d.]+|unassigned) +" # ip адрес
        r"\S+ +\w+ +" # пропускаем
        r"(\S+) +(\S+)" # status protocol
    )

    result_list = []

    for line in output.split("\n"):
        m = re.search(regex, line)
        if m:
            groups = list(m.groups())
            result_list.append(groups)
    return result_list


if __name__ == "__main__":
    with open("sh_ip_int_br.txt", "r") as f:
        content = f.read()
    pprint(parse_sh_ip_int_br(content))
