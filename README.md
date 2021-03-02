# device_info_to_excel

This is a script leverages netmiko to gather Cisco device info and output the results to an excel spreadsheet

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

## Execute the script

Now that you have everything installed you can execute the script

```bash
python main.py
```

### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night. 

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)
