with open("sh_ip_int_br.txt") as src:
    with open("result.txt", "w") as dest:
        for line in src:
            if line.startswith("Fast"):
                dest.write(line)

print()
