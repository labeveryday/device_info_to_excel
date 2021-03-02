#!/usr/bin/env python
import getpass
import os
import re
import xlsxwriter
from netmiko import ConnectHandler
from pathlib import Path


# Map the device info directory
data_folder = Path("./device_info/")


# Create an empty list
ip_list = []

# Read ip addresses from the ip_file.txt and add to ip_list
with open((data_folder / "ip_file.txt"), "r") as file:
    for address in file:
        ip_list.append(address.split('\n')[0])

# Open the inventory spreadsheet and add the device info
workbook = xlsxwriter.Workbook((data_folder / "inventory.xlsx"))
worksheet = workbook.add_worksheet('updated')
bold = workbook.add_format({'bold': True})
worksheet.write("A1", 'Hostname', bold)
worksheet.write("B1", 'IP Address', bold)
worksheet.write("C1", 'Serial Number', bold)
worksheet.write("D1", 'IOS Version', bold)
worksheet.write("E1", 'Uptime', bold)

# Open results.txt file
results_file = open((data_folder /"results.txt", "w"))

# Start with 2 to enter the 2nd row of the spreadsheet and increment
i = 2

# Device login info
username = input('Username: ')
password = getpass.getpass()
device_type = 'cisco_ios'

# Loop through ip_list and check if device up or down
# Gather hostname, ios version, uptime, and serial number
# Output results to inventory.xlsx
# Outputs to results.txt file
for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    if "Received = 1" and "Approximate" in response:
        print('\nPing successsful.\nNow connecting to: ', ip)
        net_connect = ConnectHandler(ip=ip, username=username,
                                     password=password,
                                     device_type=device_type)
        hostname = net_connect.send_command('show run | in hostname')[9:]
        version = net_connect.send_command('sh version | in System image |Cisco_IOS')
        uptime = net_connect.send_command('sh version | in uptime').split('is ')[1]
        image_version = re.search(r'System image file is .*', version).group()
        serial = net_connect.send_command('sh inventory | in PID')
        device_serial = re.search(r'SN: \w\w\w\w\w\w\w\w\w\w\w', serial).group()
        print(f'Backing up {hostname} config........')
        with open(f'.\\device_configs\\{hostname}.txt', 'w') as outf:
            outf.writelines(running_config)
        print(uptime)
        print(device_serial)
        print(image_version.split('"')[1], end=('\n\n'))
        print('-' * 40)
        worksheet.write(f"A{i}", hostname)
        worksheet.write(f"B{i}", ip)
        worksheet.write(f"C{i}", device_serial)
        worksheet.write(f"D{i}", image_version.split('"')[1])
        worksheet.write(f"E{i}", uptime)
        results_file.write(f"Up {ip} Ping successful" + "\n")
        i+=1
    else:
        print('!' * 40)
        print(f"Down {ip} Ping Unsuccessful")
        print('!' * 40)
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
        print('-' * 40)
        
# Close results_file and inventory.xlsx when script completes
results_file.close()
workbook.close()
