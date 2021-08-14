# -*- coding: utf-8 -*-
from pprint import pprint
import sys
import os
import ipaddress

from jinja2 import Environment, FileSystemLoader
import yaml


def add_0(number, zeroes=4):
    return f"{number:0{zeroes}}"

def is_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        #if str(ip).count(".") != 3:
        #    return False
        return True
    except ValueError:
        return False

# $ python cfg_gen.py templates/for.txt data_files/for.yml
template_dir, template_file = os.path.split(sys.argv[1])

vars_file = sys.argv[2]

env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True, lstrip_blocks=True
)
env.filters["add_zero"] = add_0
env.tests["ip_address"] = is_ip_address
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)
    pprint(vars_dict)

print(template.render(vars_dict))
