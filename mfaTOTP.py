import pyotp

secret_key = 'MFSG22LO'
totp = pyotp.TOTP(secret_key)
current_otp = totp.now()
print(current_otp)
