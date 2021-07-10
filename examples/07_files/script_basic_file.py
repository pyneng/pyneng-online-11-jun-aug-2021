path = (
    "/home/vagrant/repos/pyneng-11/"
    "pyneng-online-11-jun-aug-2021/examples/07_files"
)
files = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt", "sh_cdp_n_sw1.txt"]
print(files)

for file in files:
    with open(f"{path}/{file}", "r") as f:
        print(f"{path}/{file}")
        for line in f:
            if "Eth" in line:
                print(line.rstrip())
