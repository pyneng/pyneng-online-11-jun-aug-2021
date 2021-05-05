from pprint import pprint
import subprocess
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler
import paramiko
import yaml


class ScanDevices:
    def __init__(self, devices_list):
        self.devices_list = devices_list

    def _scan_device(self, ip):
        result = subprocess.run(
            ["ping", "-c", "3", "-n", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        ip_is_reachable = result.returncode == 0
        return ip_is_reachable, ip, result.stdout + result.stderr

    def scan(self, max_threads=5):
        scan_ok = {}
        scan_not_ok = {}
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            results = executor.map(self._scan_device, self.devices_list)
        for status, device, msg in results:
            if status:
                scan_ok[device] = msg
            else:
                scan_not_ok[device] = msg
        return {"success": scan_ok, "fail": scan_not_ok}


class ScanSSH(ScanDevices):
    def _scan_device(self, device_params):
        try:
            with ConnectHandler(**device_params) as telnet:
                telnet.enable()
                output = telnet.find_prompt()
                return True, device_params["host"], output
        except paramiko.ssh_exception.SSHException as error:
            return False, device_params["host"], error


if __name__ == "__main__":
    # Ping scan
    s = ScanDevices(["8.8.8.8", "8.8.4.4", "10.1.1.1"])
    pprint(s.scan(), width=120)

    # SSH scan
    with open("devices.yaml") as f:
        ssh_devices = yaml.safe_load(f)
    ssh_scan = ScanSSH(ssh_devices)
    pprint(ssh_scan.scan(), width=120)

