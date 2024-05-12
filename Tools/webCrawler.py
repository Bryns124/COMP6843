from requests_pkcs12 import post
from bs4 import BeautifulSoup
import re

base_url = 'https://haas.quoccabank.com/'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='
visited_urls = set()

def find_flag(url_path):
    if url_path in visited_urls:
        return None
    visited_urls.add(url_path)

    data_to_send = {
        'requestBox': f"""GET {url_path} HTTP/1.1
Host: kb.quoccabank.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: {base_url}
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: {base_url}
Connection: keep-alive

"""
    }

    response = post(url=base_url, data=data_to_send, pkcs12_filename=p12_path, pkcs12_password=p12_password)
    soup = BeautifulSoup(response.text, 'html.parser')
    flag_pattern = re.compile('COMP6443{.*?}')
    flag_match = flag_pattern.search(response.text)
    if flag_match:
        return flag_match.group(0)

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        next_url_path = href if href.startswith('/') else f'/{href}'
        flag = find_flag(next_url_path)
        if flag:
            return flag
    return None

flag = find_flag('/deep')
if flag:
    print(f"Flag is: {flag}")
else:
    print("Flag not found.")
