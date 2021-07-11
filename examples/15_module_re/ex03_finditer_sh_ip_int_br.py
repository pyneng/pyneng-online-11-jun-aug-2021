from pprint import pprint
import re


def parse_sh_ip_int_br(output):
    regex = r"(\S+) +(\S+) +\w+ +\w+ +(up|down) +(up|down)"
    all_match = re.finditer(regex, output)
    #for match in all_match:
    #    print(match.groups())

    results = [match.groups() for match in all_match]
    return results

if __name__ == "__main__":
    with open("sh_ip_int_br.txt", "r") as f:
        content = f.read()
    pprint(parse_sh_ip_int_br(content))

