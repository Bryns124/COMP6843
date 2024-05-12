from requests_pkcs12 import get
import re

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
count = 1
while True:
    response = get(
        login_url + b58encoding,
        headers=headers,
        pkcs12_filename=p12_path,
        pkcs12_password=p12_password
    )
    # if 'COMP6443' in response.text or 'flag' in response.text:
    if flag_match.search(response.text):
        print(f"{count} - Something interesting!! with endpoint")
        print(response.text)
        interesting_things.append(response.text)
    else:
        print(f"{count} - Nothing interesting with endpoint")
    count += 1

# print(f"Potential flag: {potential_flags}")
print(f"Interesting things: {interesting_things}")