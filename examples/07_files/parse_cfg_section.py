from pprint import pprint

with open("config_r1.txt") as f:
    output = f.read()

cfg_sections = output.split("!\n")

for section in cfg_sections:
    if section.startswith("interface") and "ip address" in section:
        print("="*50)
        pprint(section)
        section_lines = section.split("\n")
        for line in section_lines:
            if line.startswith("interface"):
                intf = line.split()[-1]
                print(intf)
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                print(ip)

