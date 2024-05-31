import requests
import pytz
import logging
from datetime import datetime
from time import sleep
import os
import time

API_VERSION = 'v12.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

additional_logo = ''' 
 ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
██║     ███████║███████║██████╔╝███████╗██║
██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
'''

def approval():
    time.sleep(1)  # Import missing module
    uuid = str(os.geteuid())+"DS"+str(os.geteuid())
    id = "CHARSI :- "+"".join(uuid)
    os.system('clear')
    print(additional_logo)
    print("\033[1;39m━▷ You Get Approved for Using Command  Paid Tool 500 Per month \033[1;37m")
    print("\n\033[1;39m━▷ Your Key :\u001b[36m "+id);time.sleep(0.1)
    try:
        httpCaht = requests.get("https://github.com/CH9RSI/Charshiiw-/blob/main/approval.txt").text
        if id in httpCaht:
            print("Congrats You get approved successful And Enjoy")
            msg = str(os.geteuid())
            time.sleep(1)
            pass
        else: 
            print("▷ Your Key Not approved please  Say to Admin");
            time.sleep(0.1)
            input('\n\nWHEN YOU BUY TOOL THEN ENTER PRESS')
            tks = ('Hello%20Charsi%20!%20Please%20Approve%20My%20Key%20This%20My%20Key%20:%20'+id)
            os.system('am start https://wa.me/+918227039997?text='+tks),approval()
            time.sleep(1)
            exit()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during approval: {e}")
        exit()

def send_message(api_url, access_token, thread_id, message):
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(api_url, data=parameters, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending message: {e}")
        return None

def get_access_tokens():
    try:
        file_path = input("\n\033[1;35mEnter Token File Path :- ")
        with open(file_path, 'r') as file:
            access_tokens = file.read().splitlines()
    except FileNotFoundError:
        print("\033[91mFile not found. Please provide a valid file path.\033[0m")
        exit()

    return access_tokens

def get_thread_ids():
    try:
        file_path = input("   \n\033[1;35mEnter Group/Inbox File Path :- ")
        with open(file_path, 'r') as file:
            thread_ids = file.read().splitlines()
    except FileNotFoundError:
        print("\033[91mFile not found. Please provide a valid file path.\033[0m")
        exit()

    return thread_ids

def get_access_tokens_and_thread_ids():
    access_tokens = get_access_tokens()
    thread_ids = get_thread_ids()
    return access_tokens, thread_ids

def round_robin_send_messages(access_tokens, thread_ids, messages, mn, sleep_time):
    ist = pytz.timezone('Asia/Kolkata')

    num_tokens = len(access_tokens)
    num_threads = len(thread_ids)
    num_messages = len(messages)
    current_message_index = 0

    while True:
        for j in range(num_tokens):
            access_token = access_tokens[j]

            for k in range(num_threads):
                thread_id = thread_ids[k]
                api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                current_message = messages[current_message_index]
                message = f'{mn} {current_message}'

                response = send_message(api_url, access_token, thread_id, message)
                current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

                if response and response.status_code == 200:
                    print(f"\033[92m\n Message Sent Successfully. \n\033[1;32m✪Group Id :- {thread_id} \n\n\033[1;32m✪Message :- {message} \033[0m")
                else:
                    print(f"\033[91mFailed To Send Message. Please Help with Group Id {thread_id}: {message}\033[0m")

                sleep(sleep_time)

        current_message_index = (current_message_index + 1) % num_messages

def main():
    approval()
    print(additional_logo)
    logging.basicConfig(level=logging.INFO)

    while True:
        try:
            access_tokens, thread_ids = get_access_tokens_and_thread_ids()
            mn_color = input("\n\033[1;36mEnter Hater Name :- ")
            txt_file_path = input("\n\033[1;36mEnter Message File Path :- ")

            try:
                with open(txt_file_path, 'r') as file:
                    messages = file.read().splitlines()
            except FileNotFoundError:
                print("\033[91mFile not found. Please provide a valid file path.\033[0m")
                exit()

            sleep_time = float(input("\n\033[1;36mEnter Speed Time (second) :- "))

            round_robin_send_messages(access_tokens, thread_ids, messages, mn_color, sleep_time)

        except KeyboardInterrupt:
            logging.info("\nScript terminated by user.")

if __name__ == "__main__":
    main()