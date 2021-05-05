import yaml
from pprint import pprint
import netmiko
from textfsm import clitable


def send_show(device, command):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
        cmd = "sh cdp ne de"
        out = send_show(r1, cmd)
        pprint(out)
    pth = (
        "/home/vagrant/repos/pyneng-10/pyneng-online-10-jan-apr-2021/"
        "examples/21_textfsm/templates"
    )

    cli = clitable.CliTable("index", pth)
    cli.ParseCmd(out, {"Command": cmd, "Vendor": r1["device_type"]})
    headers = list(cli.header)
    data = [dict(zip(headers, line)) for line in cli]
    pprint(data)
