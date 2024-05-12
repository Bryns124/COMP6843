import base58

encoded_ticket = base58.b58encode("1:1".encode()).decode()
print(encoded_ticket)