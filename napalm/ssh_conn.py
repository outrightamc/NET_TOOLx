#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "router1",
    "username": "arkadin",
#    "password": getpass(),
    "password": "arkadin",
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
command = "show ip inter brief"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()