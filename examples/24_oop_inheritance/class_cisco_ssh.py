import time
from class_base_ssh import BaseSSH


class ErrorInCommand(Exception):
    pass


class CiscoSSH(BaseSSH):
    def __init__(self, host, username, password, enable_password, prompt="[>#]"):
        print("Child CiscoSSH __init__")
        # BaseSSH.__init__(self, host, username, password, prompt=prompt)
        # super(CiscoSSH, self).__init__(host, username, password, prompt=prompt)
        super().__init__(host, username, password, prompt=prompt)

        self._ssh.send("enable\n")
        self._ssh.send(f"{enable_password}\n")
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)
        self._ssh.send(f"terminal length 0\n")
        time.sleep(self.pause)
        self._ssh.recv(self.max_read).decode("utf-8")

    def get_config(self):
        output = self.send_command("sh run")
        return output

    def send_command(self, command):
        output = super().send_command(command)
        if "%" in output:
            raise ErrorInCommand(
                f"Возникла ошибка при выполнении команды {command}"
            )
        return output

    def send_config_commands(self, commands):
        print("Child CiscoSSH send_config_commands")
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        output = super().send_config_commands(commands)
        return output


if __name__ == "__main__":
    with CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        print(r1.send_command("sh clck"))
        #print(r1.send_config_commands("interface lo88"))

"""
Child CiscoSSH __init__
Parent BaseSSH __init__
Parent BaseSSH send_command
sh clock
*08:16:38.347 UTC Sat Apr 17 2021
R1#
Child CiscoSSH send_config_commands
Parent BaseSSH send_config_commands
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface lo88
R1(config-if)#end
R1#
"""
