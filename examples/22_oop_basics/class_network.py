import ipaddress


class Network:
    all_allocated_ip = []

    def __init__(self, network, mask):
        self.network = network
        self.mask = mask
        self.allocated = []
        ipv4net = ipaddress.ip_network(f"{self.network}/{self.mask}")
        self.hosts = [str(ip) for ip in ipv4net.hosts()]

    def allocate_ip(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
                # Network.all_allocated_ip.append(ip)
                type(self).all_allocated_ip.append(ip)
            else:
                raise ValueError(
                    f"IP-адрес {ip} уже находится в allocated "
                    f"\n{self.allocated}"
            )
        else:
            raise ValueError(
                f"IP-адрес {ip} не входит в сеть {self.network}/{self.mask}"
            )

    def __str__(self):
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        return f"Network('{self.network}', {self.mask})"

    def __len__(self):
        return len(self.hosts)
