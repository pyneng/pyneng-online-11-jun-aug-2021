from pprint import pprint
import platform
import subprocess


def ping_ip_list(ip_list):
    pingable = []
    unpingable = []
    if platform.system().lower() == "windows":
        cmd = ['ping', '-n', '1']
    else:
        cmd = ['ping', '-c', '1']

    processes = {}
    for ip in ip_list:
        p = subprocess.Popen(
            cmd + [ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            encoding="utf-8"
        )
        processes[ip] = p
    pprint(processes)
    for ip, process in processes.items():
        returncode = process.wait()
        if returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    return pingable, unpingable


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "10.1.1.1", "8.8.4.4", "10.2.2.2"]
    result = ping_ip_list(ip_list)
    pprint(result)
