from jinja2 import Environment, FileSystemLoader
import yaml


env = Environment(loader=FileSystemLoader("."))
templ = env.get_template("cfg_template.txt")

liverpool = {"id": "11", "name": "Liverpool", "int": "Gi1/0/17", "ip": "10.1.1.10"}
print(templ.render(liverpool))

"""
Examples:

$ python generator.py

hostname Liverpool
!
interface Loopback255
 description Management loopback
 ip address 10.255.11.1 255.255.255.255
!
interface GigabitEthernet0/0
 description LAN to Liverpool sw1 Gi1/0/17
 ip address 10.1.1.10 255.255.255.0
!
router ospf 10
 router-id 10.255.11.1
 auto-cost reference-bandwidth 10000
 network 10.0.0.0 0.255.255.255 area 0
"""
