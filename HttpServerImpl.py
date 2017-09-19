'''
MIT License

Copyright (c) 2017 Avinesh Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from SimplePyHttpServer import MyHandler
import time
import subprocess
import json

# You can implement here from simple to complex logic in order to get the work done.
# For demo, I have implemented ifconfig command.
# http://localhost/?command=ifconfig ==> this request to server will return ifconfig command output on host.

# Data is a dictionary.
# The dictionary keys are the unique query variable names and the values are lists of values for each name.
# example:
# http://localhost/?command=ifconfig&value=1  ==> result to data = {'command': ['ifconfig'], 'value': ['1']}
# http://localhost/?command=ifconfig&value=1&value=2  ==> result to data = {'command': ['ifconfig'], 'value': ['1','2']}

# this should return desired response.
def process_get(data):
    command = data.get('command')
    cmd = command[0]
    if cmd == 'ifconfig':
        nw_config = subprocess.check_output(["ifconfig"], shell=True)
        return nw_config
    else:
        return "invalid command."


# data should be in JSON format.
# this should return desired response.
def process_post(data):
    eid = data["eid"]
    processed = {}
    processed["name"] = "Avinesh Kumar"
    processed["id"] = eid
    processed["email"]= "avinesh@gmail.com"
    json_data = json.dumps(processed)
    return json_data
