cfg = input("Введите что надо настроить: ")

if cfg == "access":
    print("access_cfg")
elif cfg == "trunk":
    print("trunk_cfg")
elif cfg == "vpn":
    print("vpn_cfg")
else:
    print("такой конфигурации нет")

# version 2
cfg_dict = {
    "access": "access_cfg",
    "trunk": "trunk_cfg",
    "vpn": "vpn_cfg"
}

if cfg in cfg_dict:
    print(cfg_dict[cfg])
else:
    print("такой конфигурации нет")

