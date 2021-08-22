import telnetlib
import time


class CiscoTelnet:
    def __init__(
        self, ip, username, password, enable_password=None, disable_paging=True
    ):
        self.ip = ip
        self.username = username

        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._telnet.write(username.encode("ascii") + b"\n")
        self._telnet.read_until(b"Password:")
        self._telnet.write(password.encode("ascii") + b"\n")
        if enable_password:
            self._telnet.write(b"enable\n")
            self._telnet.read_until(b"Password:")
            self._telnet.write(enable_password.encode("ascii") + b"\n")
        if disable_paging:
            self._telnet.write(b"terminal length 0\n")
        time.sleep(0.5)
        self._telnet.read_very_eager()

    def send_show_command(self, command):
        self._telnet.write(command.encode("utf-8") + b"\n")
        output = self._telnet.read_until(b"#").decode("utf-8")
        return output

    def _read_until_prompt(self, prompt="#"):
        return self._telnet.read_until(prompt.encode("utf-8")).decode("utf-8")

    def send_config(self, commands):
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        output = ""
        for cmd in commands:
            self._telnet.write(cmd.encode("utf-8") + b"\n")
            output += self._read_until_prompt()
        return output

    def close(self):
        self._telnet.close()

    def get_cfg(self, command="sh run"):
        return self.send_show_command(command)


if __name__ == "__main__":
    r1 = CiscoTelnet("192.168.100.1", "cisco", "cisco", "cisco")
    r1.send_show_command("sh clock")
    # CiscoTelnet.send_show_command(r1, "sh clock")
