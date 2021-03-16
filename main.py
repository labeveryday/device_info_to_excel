#!/usr/bin/env python
"""
    Copyright 2016 Cisco Systems All rights reserved.
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are
 met:
     * Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.
 The contents of this file are licensed under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with the
 License. You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 License for the specific language governing permissions and limitations under
 the License.
"""
import datetime
import getpass
import subprocess
from pathlib import Path
import xlsxwriter
from netmiko import ConnectHandler

# Enter today's date into a variable
today = f"{datetime.datetime.now():%Y-%m-%d}"

# Map the device info directory
data_folder = Path("./device_info/")


# Create an empty list
ip_list = []

# Read ip addresses from the ip_file.txt and add to ip_list
with open(data_folder / "ip_file.txt", "r") as file:
    for address in file:
        ip_list.append(address.split('\n')[0])

# Create a new workbook if not there
workbook = xlsxwriter.Workbook(data_folder / "inventory.xlsx")
# Create a new worksheet in the working book title `updated today's date1`
worksheet = workbook.add_worksheet(f"updated {today}")
# Create bold titled columns in the worksheet
bold = workbook.add_format({"bold": True})
worksheet.write("A1", "Hostname", bold)
worksheet.write("B1", "IP Address", bold)
worksheet.write("C1", "Serial Number", bold)
worksheet.write("D1", "IOS Version", bold)
worksheet.write("E1", "Running Image", bold)
worksheet.write("F1", "Hardware", bold)
worksheet.write("G1", "Uptime", bold)
# Set the width of columns A:G to 20
worksheet.set_column(0, 6, 20)


# Open results.txt file
results_file = open(data_folder /"results.txt", "w")

# Start with 2 to enter the 2nd row of the spreadsheet and increment
i = 2

# Device login info
username = input('Username: ')
password = getpass.getpass()
DEVICE_TYPE = 'cisco_ios'

# Loop through ip_list and check if device up or down
# Gather hostname, ios version, uptime, and serial number
# Output results to inventory.xlsx
# Outputs to results.txt file
for ip in ip_list:
    response = subprocess.run(["ping", ip, "-c", "1"], stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL, check=True)
    print(f"\nAttempting to ping {ip}.....")
    if response.returncode == 0:
        print(f'Ping successsful!!!!\nNow connecting to: {ip}\n')
        net_connect = ConnectHandler(ip=ip, username=username,
                                     password=password,
                                     device_type=DEVICE_TYPE)
        device_info = net_connect.send_command('show version', use_textfsm=True)[0]
        print(f"Device Hostname: {device_info['hostname']}")
        print(f"------ Uptime:   {device_info['uptime']}")
        print(f"------ Serial:   {device_info['serial'][0]}")
        print(f"------ Version:  {device_info['version']}", end=('\n\n'))
        print('-' * 40)
        worksheet.write(f"A{i}", device_info['hostname'])
        worksheet.write(f"B{i}", ip)
        worksheet.write(f"C{i}", device_info['serial'][0])
        worksheet.write(f"D{i}", device_info['version'])
        worksheet.write(f"E{i}", device_info['running_image'])
        worksheet.write(f"F{i}", device_info['hardware'][0])
        worksheet.write(f"G{i}", device_info['uptime'])
        results_file.write(f"Up {ip} Ping successful" + "\n")
        i+=1
    else:
        print('!' * 40)
        print(f"Down {ip} ---- Ping Unsuccessful 😔")
        print('!' * 40)
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
        print('-' * 40)

# Close results_file and inventory.xlsx when script completes
results_file.close()
workbook.close()
