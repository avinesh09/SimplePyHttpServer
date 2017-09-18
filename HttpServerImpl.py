from SimplePyHttpServer import MyHandler
import time
import subprocess

# you can implement here from simple to complex logic in order to get the work done.
# here i have implemented ifconfig command.
# http://localhost/?command=ifconfig ==> this request to server will return ifconfig command output on host.

def perform_command(query_components):
    command = query_components.get('command')
    cmd = command[0]
    if cmd == 'ifconfig':
        nw_config = subprocess.check_output(["ifconfig"], shell=True)
        return nw_config
    else:
        return "invalid command."
