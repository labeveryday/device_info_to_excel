# device_info_to_excel, use this script to gather Cisco device info

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/labeveryday/device_info_to_excel)

This is a script that leverages [netmiko](https://github.com/ktbyers/netmiko) to gather Cisco device info. The script then outputs the results to an excel spreadsheet. Use this script to improve your understanding of python. While also learning how to leverage network automation to update your network documentation. Another note, if you need access to a lab environment you can have free access to the [Cisco DevNet Always-On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/e83cfd31-ade3-4e15-91d6-3118b867a0dd?diagramType=Topology)

**Gathers**:

- hostname
- ios version
- device uptime
- serial number
- hardware type
- running device image

The intent of the of this script is to help you understand the basics of writing a line-by-line execution Python script.

## Download the Code

To get started: Download the code and cd the `DeviceInfoToExcel` directory

```bash
git clone https://github.com/labeveryday/device_info_to_excel.git
cd device_info_to_excel
```

## Python Virtual Environment

When executing python code or installing python applications you should get into the practice of creating and managing python virtual environments.
This will allow you to run different versions of a python library while avoiding version conflicts. My preferred tool for python virtual environments is `venv`
There are tools out there. Remember to find what works best for you.

**On Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**On Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Install project requirements

Once you have your virtual environment setup and activated you will need to install your python packages if needed. One way to do this is by doing `pip install <python package>` another way is by using the
example listed below. It will installed the required libraries for this specific package.

```bash
pip install -r requirements.txt
```

## Example: Script in action

![Lab](https://github.com/labeveryday/Notes/blob/main/images/cml.png)

Before executing your script you must update your device ip address list in the `device_info/ip_file.txt` file. This will be the list of ip addresses that will be used in the script.

```bash
(venv) duan@ubuntu device_info_to_excel$ cat device_info/ip_file.txt 
192.168.23.142
192.168.23.143
192.168.23.144
192.168.23.145
192.168.23.146
192.168.23.147
```

Now that you have everything installed and updated you can execute the script

```bash
(venv) duan@ubuntu device_info_to_excel$ python main.py
Username: duan
Password: 

Attempting to ping 192.168.23.145.....
Ping successsful!!!!
Now connecting to: 192.168.23.145

Device Hostname: R1-CSR1000v
------ Uptime:   21 minutes
------ Serial:   9O840KC3ZG2
------ Version:  17.3.1a

----------------------------------------

Attempting to ping 192.168.23.146.....
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Down 192.168.23.146 ---- Ping Unsuccessful 😔
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
----------------------------------------
```

After the script successfully pulls data from the devices the `inventory.xlsx` file will be updated accordingly.

> NOTE: With the python xlsxwriter there is no way to append to a workbook. Each time the script is executed the `inventory.xlsx` file will be recreated.

![excel](https://github.com/labeveryday/Notes/blob/main/images/device_excel.png)

### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)
