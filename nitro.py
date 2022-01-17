import os
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install colorama')
os.system('pip install Fore')
os.system('pip install time')
os.system('pip install requests')
os.system('clear')

import requests
import time
import os
import pyfiglet
from colorama import Fore


print(Fore.GREEN + f"=========================================")
banner = pyfiglet.figlet_format("NITRO COIN")
print(Fore.GREEN + banner)
print("Cr: @mioxiliya")
print(Fore.GREEN + f"=========================================")

usr = input(Fore.RED + f"[?] Enter your username: ")
print(Fore.BLUE + f"[!] Username set to " + usr)
coin = input(Fore.RED + f"[?] Enter coin value: ")
print(Fore.BLUE + f"[!] Coin value set to " + coin)

api = f"http://zux021.xyz/TD/nitro.php?un={usr}&c={coin}&submit=submit"
try:
    req = requests.get(api)
except:
    print("[!] Network connection error, Check your internet connection.")
