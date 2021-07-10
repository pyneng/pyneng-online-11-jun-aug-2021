ignore = ['duplex', 'alias', 'Current configuration']

with open("config_r1.txt") as f:
    for line in f:
        if not any([word in line for word in ignore]):
            print(line.rstrip())
