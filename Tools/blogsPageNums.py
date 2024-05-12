from requests_pkcs12 import get

url = 'https://blog.quoccabank.com/?page_id='
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

with open('nums100.txt', 'r') as file:
    nums = file.read().splitlines()

interesting = []

for num in nums:
    response = get(url + num, pkcs12_filename=p12_path, pkcs12_password=p12_password)
    if "Page not found" in response.text:
        print(f"Nothing in {num}")
    else:
        print(f"Something in {num}")
        interesting.append(num)

print(interesting)