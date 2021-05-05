import re


def get_interfaces_without_ip(config):
    regex = (
        r"^interface (\S+)\n"
        r"( .+\n)+"
    )
    interfaces_without_ip_address = []
    match_all = re.finditer(regex, config, re.MULTILINE)
    for m in match_all:
        # print(m.group())
        # print("#"*40)
        if "\n ip address" not in m.group():
            interfaces_without_ip_address.append(m.group(1))

    return interfaces_without_ip_address


if __name__ == "__main__":
    with open("config_r1.txt") as f:
        content = f.read()
        print(get_interfaces_without_ip(content))
