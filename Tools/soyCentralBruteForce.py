import hmac
import hashlib
import base64

header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
payload = "eyJ1c2VyIjoiZ3JheW9ucyIsImlzQ2hhZCI6ZmFsc2UsImlhdCI6MTcwOTQ2NTEwNn0"
signature = "xdmRZ6yEYYceEzzDGsp2Fqqe7vlt0A3Pk79Zv3gs1Ik"

with open('/Users/bryanle/Downloads/10-million-password-list-top-1000000.txt', 'r') as file:
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
