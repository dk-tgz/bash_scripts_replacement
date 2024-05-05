#!/usr/bin/env python
import paramiko
paramiko.util.log_to_file("paramiko.log")

class SSHClient:
    def __init__(self, host, port, user, password, key_path, sudo_password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_config = {
            'hostname': host,
            'port': port,
            'username': user,
            'key_filename': key_path,
            'password': password
        }
        self.sudo_password = sudo_password
        client.connect(**self.ssh_config)        
        self.client = client

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        if self.sudo_password:
            stdin.write(self.ssh_config["password"] + "\n")
            stdin.flush()
        return {'out': stdout.read().decode("utf-8"), 'err': stderr.read().decode("utf-8"), 'retval': stdout.channel.recv_exit_status()}

def run_commands():
    try:
        ssh = SSHClient(host="localhost", port="2222", user="ubuntu", password=None, key_path="../../../ssh/id_rsa", sudo_password=False)
        output = ssh.execute('sudo ls -lrt /etc/test')
        print('result', output["retval"], '\nstdout:', output["out"], 'stderr:', output["err"])

        output = ssh.execute('sudo touch /etc/test')
        print('result', output["retval"], '\nstdout:', output["out"], 'stderr:', output["err"])

        ssh.close() 
    except Exception as e:
        print('error:', e)
run_commands()
