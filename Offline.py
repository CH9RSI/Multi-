import requests
from colorama import Fore, Style, init
import time
import os
import hashlib
import random
from urllib.parse import quote

init(autoreset=True)

def get_unique_id():
    try:
        unique_str = str(os.getuid()) + os.getlogin() if os.name != 'nt' else str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

def check_permission(unique_key):
    while True:
        try:
            response = requests.get('https://github.com/Badmaash0/APROVAL-/blob/main/Aproval.txt')
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(f'{Fore.GREEN}[√] Permission granted. Your Key Was Approved.')
                    return
                print(f'{Fore.RED}Checking Approval.....')
                time.sleep(10)
            else:
                print(f'Failed to fetch permissions list. Status code: {response.status_code}')
                time.sleep(10)
        except Exception as e:
            print(f'Error checking permission: {e}')
            time.sleep(10)

def send_approval_request(unique_key):
    try:
        message = f'Hello JACK SIIR II AM USIING YOUR OFFLINE TERMUX...MY KEY PLACE APPROVAL :: {unique_key}0'
        os.system(f'am start https://wa.me/+916360448086?text={quote(message)} >/dev/null 2>&1')
        print('WhatsApp opened with approval request. Waiting for approval...')
    except Exception as e:
        print(f'Error sending approval request: {e}')
        exit(1)

def print_colored_logo(logo):
    colors = [31, 32, 33, 34, 35, 36]
    for line in logo.split('\n'):
        color = random.choice(colors)
        print(f'\033[1;{color}m{line}\033[0m')
        time.sleep(0.1)

def pre_main():
    logo = '''
    #######  ######## ######## ##       #### ##    ## ######## 
    ##     ## ##       ##       ##        ##  ###   ## ##       
    ##     ## ##       ##       ##        ##  ####  ## ##       
    ##     ## ######   ######   ##        ##  ## ## ## ######   
    ##     ## ##       ##       ##        ##  ##  #### ##       
    ##     ## ##       ##       ##        ##  ##   ### ##       
    #######  ##       ##       ######## #### ##    ## ######## 
    '''
    unique_key = get_unique_id()
    os.system('clear')
    print_colored_logo(logo)
    print('•──────────────────────────────────────────────────────────────────────────────────────•')
    print('[~] OWNER-BROKEN-JACK')
    print('•──────────────────────────────────────────────────────────────────────────────────────•')
    print(f'[ ] YOUR K3Y :: {unique_key}')
    print('•──────────────────────────────────────────────────────────────────────────────────────•')
    send_approval_request(unique_key)
    check_permission(unique_key)

def display_logo():
    logo = f'''
    {Fore.GREEN} 
    #######  ######## ######## ##       #### ##    ## ######## 
    ##     ## ##       ##       ##        ##  ###   ## ##       
    ##     ## ##       ##       ##        ##  ####  ## ##       
    ##     ## ######   ######   ##        ##  ## ## ## ######   
    ##     ## ##       ##       ##        ##  ##  #### ##       
    ##     ## ##       ##       ##        ##  ##   ### ##       
    #######  ##       ##       ######## #### ##    ## ########                                          
    {Fore.CYAN}< INFORMATION >----------------------------------------
    [ DEVELOPER  ]: OWNER-JACK 
    [ VERSION    ]: 1.1
    [ TOOL NAME  ]: CONVO OFFLINE
    [ FACEBOOK   ]: JACK DIXIT 
    ------------------------------------------------------------
    '''
    print(logo)

def fetch_ip_info():
    try:
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            data = response.json()
            return {'ip': data.get('query', 'N/A'), 'country': data.get('country', 'N/A'), 'region': data.get('regionName', 'N/A'), 'city': data.get('city', 'N/A')}
        print(f'{Fore.RED}Failed to fetch IP information.')
    except requests.RequestException as e:
        print(f'{Fore.RED}Error fetching IP info: {e}')

def display_info():
    ip_info = fetch_ip_info()
    if ip_info:
        info = f"\n{Fore.YELLOW}< YOUR INFO >-----------------------------------------\n[ IP ADDRESS ]: {ip_info['ip']}\n[ TIME       ]: {time.strftime('%I:%M %p')}\n[ DATE       ]: {time.strftime('%d/%B/%Y')}\n------------------------------------------------------------\n[ COUNTRY    ]: {ip_info['country']}\n[ REGION     ]: {ip_info['region']}\n[ CITY       ]: {ip_info['city']}\n------------------------------------------------------------\n"
        print(info)
    else:
        print(f'{Fore.RED}Could not retrieve IP and location information.')

server_url = 'https://wa.me/+916360448086'

def menu():
    display_logo()
    display_info()
    note = f'\n{Fore.LIGHTMAGENTA_EX}< NOTE >-------------------------------------------\n              Tool Paid Monthly: ₹250\n------------------------------------------------------------\n'
    print(note)

if __name__ == '__main__':
    pre_main()
    menu()
