import hmac
import hashlib
import base64

header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
payload = "eyJVc2VybmFtZSI6ImJvYkBxdW9jY2FiYW5rLmNvbSIsImV4cCI6MTcwODc4NjMwMX0"
signature = "5eOAf-v7fM-imk3IJvW7Oj96Wyv7jygbyRE-bwTiyXs"

with open('/Users/bryanle/Downloads/100k-most-used-passwords-NCSC.txt', 'r') as file:
    possible_secrets = file.read().splitlines()

def base64url_decode(input):
    input += '=' * (4 - (len(input) % 4))
    return base64.urlsafe_b64decode(input)

decoded_signature = base64url_decode(signature)

def is_correct_secret(secret):
    key = secret.encode()
    message = f'{header}.{payload}'.encode()
    new_signature = hmac.new(key, message, hashlib.sha256).digest()

    return hmac.compare_digest(new_signature, decoded_signature)

for secret in possible_secrets:
    print(secret)
    if is_correct_secret(secret):
        print(f'The secret is: {secret}')
        break
else:
    print('No matching secret found.')
