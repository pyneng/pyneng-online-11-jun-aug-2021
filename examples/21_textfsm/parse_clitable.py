import yaml
from pprint import pprint
import netmiko
from textfsm import clitable
import textfsm


def parse_output_textfsm(
    output,
    attributes_dict,
    pth="/home/vagrant/repos/pyneng-11/pyneng-online-11-jun-aug-2021/examples/21_textfsm/templates",
    index="index",
):
    cli = clitable.CliTable(index, pth)  # clitable
    try:
        cli.ParseCmd(output, attributes_dict)  # clitable
        data = [list(item) for item in cli]  # clitable
        return data
    except FileNotFoundError:
        print("Шаблон не найден, но есть вывод команды")
    except textfsm.clitable.CliTableError:
        print("Команды нет в index файле")


def send_show(device, command, parse_textfsm=True):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        prompt = ssh.find_prompt()
        output = ssh.send_command(command)
        output = f"{prompt}{command}\n{output}"
        if parse_textfsm:
            parsed_data = parse_output_textfsm(
                output, {"Command": command, "Vendor": device["device_type"]}
            )
            if parsed_data:
                return parsed_data
        return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh ip int br"
    pprint(send_show(devices[0], cmd))
