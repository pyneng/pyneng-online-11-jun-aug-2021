import paramiko
import time
from pprint import pprint
import socket
import re


class BaseSSH:
    pause = 0.5
    max_read = 60000

    def __init__(
        self, host, username, password, prompt=None,
    ):
        print("Parent BaseSSH __init__")
        self.host = host
        self.username = username
        self.password = password
        self.prompt = prompt

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        self._ssh = client.invoke_shell()
        self._ssh.settimeout(2)
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)

    def _read_until(self, line):
        command_output = ""
        self._ssh.settimeout(5)
        while True:
            try:
                time.sleep(self.pause)
                part = self._ssh.recv(self.max_read).decode("utf-8")
                command_output += part
                match_prompt = re.search(line, command_output)
                if match_prompt:
                    break
            except socket.timeout:
                break
        return command_output.replace("\r\n", "\n")

    def send_command(self, command):
        print("Parent BaseSSH send_command")
        self._ssh.send(f"{command}\n")
        if self.prompt:
            output = self._read_until(self.prompt)
        else:
            time.sleep(self.pause)
            output = self._ssh.recv(self.max_read).decode("utf-8")
        return output

    def send_config_commands(self, commands):
        print("Parent BaseSSH send_config_commands")
        output = ""
        for cmd in commands:
            self._ssh.send(f"{cmd}\n")
            if self.prompt:
                output += self._read_until(self.prompt)
            else:
                time.sleep(self.pause)
                output += self._ssh.recv(self.max_read).decode("utf-8")
        return output

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
