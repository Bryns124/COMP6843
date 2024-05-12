from requests_pkcs12 import get

login_page_url = 'https://quoccaid.quoccabank.com/'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

try:
    response = get(login_page_url, pkcs12_filename=p12_path, pkcs12_password=p12_password)
    print("Response body:", response.text)
except Exception as e:
    print("An error occurred:", e)