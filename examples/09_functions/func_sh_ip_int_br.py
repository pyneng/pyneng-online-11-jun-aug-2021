from pprint import pprint


def get_intf_ip_dict(filename):
    """
    Функция ожидает имя файла с выводом sh ip int br.
    Возвращает словарь intf: ip
    """
    result = {}

    with open(filename) as f:
        for line in f:
            line_list = line.split()
            if len(line_list) > 2 and line_list[1][0].isdigit():
                intf = line_list[0]
                ip = line_list[1]
                result[intf] = ip

    return result


files = ["sh_ip_int_br.txt", "sh_ip_int_br2.txt"]

for file in files:
    data = get_intf_ip_dict(file)
    pprint(data)






