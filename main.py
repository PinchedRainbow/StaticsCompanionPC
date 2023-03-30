import os
import time
import requests
from flask import Flask, jsonify
import urllib3
urllib3.disable_warnings()

data = []
name = ""
PID = ""
port = ""
password = ""
protocol = ""
accessToken = ""
entitelmentToken = ""


# start the flask server
app = Flask(__name__)

import logging

# New, 2022 Method:

logging.getLogger('werkzeug').disabled = True


@app.route("/")
def send_message():
    return jsonify({"accessToken": accessToken, "entitlementToken": entitelmentToken})


def getLockFile():
    return os.path.join(os.getenv('LOCALAPPDATA'), R'Riot Games\Riot Client\Config\lockfile')


# try to read the lockfile
while True:
    try:
        with open(getLockFile()) as lockfile:
            data = lockfile.read().split(':')
            break
    except:
        # tell user that valorant is not running then wait for keypress
        print("Valorant is not running! Please open Valorant and press any key to continue...")
        input()

name = data[0]
PID = data[1]
port = data[2]
password = data[3]
protocol = data[4]

# print("Name: " + name)
# print("PID: " + PID)
# print("Port: " + port)
# print("Password: " + password)
# print("Protocol: " + protocol)

# print out the device IP
import socket

# Get the IPV4 address of the local host
ip_address = socket.gethostbyname(socket.gethostname())

# Print out the IPV4 address
#print("IPV4 address:", ip_address)

r = requests.get(f"https://127.0.0.1:{port}/entitlements/v1/token", auth=('riot', password),
                        verify=False)
accessToken = r.json()["accessToken"]
entitelmentToken = r.json()["token"]

# # print out the tokens
# print("Access Token: " + accessToken)
# print("Entitelment Token: " + entitelmentToken)

# if the tokens are not empty, start the server
if (accessToken != "", entitelmentToken != ""):
    print("Server started! Enter the IP into Statics: " + ip_address)
    print("You can now close this window!")
    app.run(host='0.0.0.0', port=5000)
    

