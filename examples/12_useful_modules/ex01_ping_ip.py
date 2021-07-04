import platform
import subprocess


def ping_ip(ip):
    if platform.system().lower() == "windows":
        cmd = ['ping', '-n', '1', ip]
    else:
        cmd = ['ping', '-c', '1', ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        encoding="utf-8"
    )
    # output = result.stdout + result.stderr
    # print(output)
    if result.returncode == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "10.1.1.1", "8.8.4.4", "10.2.2.2"]
    for ip in ip_list:
        status = ping_ip(ip)
        if status:
            print(f"Адрес {ip} пингуется")
        else:
            print(f"Адрес {ip} не пингуется")
