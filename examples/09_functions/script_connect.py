from pprint import pprint


def connect(device_type, host, username, password, secret, command):
    print(f"Подключаемся к {host}")
    print(f"отправляем команду {command}")


devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.2",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    },
]
for dev in devices:
    pprint(dev)
    connect(
        device_type=dev["device_type"], username=dev["username"],
        host=dev["host"], password=dev["password"], secret=dev["secret"],
        command="sh run"
    )
    connect(**dev, command="sh run")
    #connect(
    #    device_type="cisco_ios", username="cisco",
    #    host="192.168.100.1", password="cisco", secret="cisco",
    #    command="sh run"
    #)

