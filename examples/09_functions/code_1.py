with open("config_r1.txt") as f:
    for index, line in enumerate(f, 1):
        print(f"{index:<5}{line}", end="")
