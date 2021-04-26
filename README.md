# device_info_to_excel, use this script to gather Cisco device info

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/labeveryday/device_info_to_excel)

This script leverages [Netmiko](https://github.com/ktbyers/netmiko) to gather a Cisco device info. The script then outputs the results to an Excel spreadsheet.

Use this script to improve your understanding of Python. While also learning how to leverage network automation to update your network documentation.

Another note, if you need access to a lab environment you can have free access to the [Cisco DevNet Always-On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology)

**Gathers**:

- Hostname
- Ios Version
- Device Uptime
- Serial Number
- Hardware Type (Device Model)
- Running Device Image

The intent of the of this script is to help you understand the basics of writing a line-by-line execution Python script.

## Download the Code

To get started: Download the code and cd into the `device_info_to_excel` directory.

```bash
$ git clone https://github.com/labeveryday/device_info_to_excel.git
$ cd device_info_to_excel
```

## Python Virtual Environment

When executing Python code or installing Python applications, you should get into the practice of creating and managing Python virtual environments. This allows you to run different versions of a Python library while avoiding version conflicts.

My preferred tool for Python virtual environments is `venv`. There are [other tools](https://python.libhunt.com/venv-alternatives) out there. Remember to find what works best for you.

**Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Install Project Requirements

Once you have your virtual environment setup and activated, you will need to install your Python packages if needed. One way to do this is by doing `pip install <python package>`. Another way is by using the example listed below. It will install the required libraries for this project.

```bash
pip install -r requirements.txt
```

## Example: Script in Action

![Lab](https://github.com/labeveryday/Notes/blob/main/images/cml.png)

Before executing your script you must update your device IP address list in the `device_info/ip_file.txt` file. This will be the list of IP addresses that will be used in the script.

```bash
(venv) duan@ubuntu device_info_to_excel$ cat device_info/ip_file.txt
192.168.23.142
192.168.23.143
192.168.23.144
192.168.23.145
192.168.23.146
192.168.23.147
```

Now that you have everything installed and updated you can execute the script.

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

> **NOTE:** With the Python [XlsxWriter](xlsxwriter.readthedocs.io/), there is no way to append data to a workbook. Each time the script is executed the `inventory.xlsx` file will be recreated. Make sure you close the `inventory.xlsx` file before the script is executed.

![Excel](https://github.com/labeveryday/Notes/blob/main/images/device_excel.png)

### For Windows Users Only

You might get a permission error message when you use `use_textfsm=true` parameter in `send_command("show version", use_textfsm=True)[0]`. The workaround to this issue is to add `NET_TEXTFSM` variable in Windows Environment Variables. Steps listed below.

1. Go to **Control Panel** > **View Advanced system settings**, and click on **Environment Variables**.

2. Under **System variables**, click New and add the following variable:

   **Variable name:** NET_TEXTFSM
   **Variable value:** `%APPDATA%\Python\Python39\site-packages\ntc_templates\templates`

> Test the path in Windows Explorer first.

Also in the ping subprocess, don't forget to replace `-c` flag with `-n`.

```python
response = subprocess.run(
    ["ping", ip, "-n", "1"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    check=True
)
```

### About Me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)
- [Twitter](https://twitter.com/labeveryday)
