import pyotp, qrcode

# Generate a secret key (this is what gets embedded in the QR code)
secret = pyotp.random_base32()
print(f'TOTP Secret: {secret}')

# Create TOTP object
totp = pyotp.TOTP(secret)

# Generate the provisioning URI (for QR code)
uri = totp.provisioning_uri(name='testuser@instasafe.local', issuer_name='InstaSafe Lab')
print(f'Provisioning URI: {uri}')

# Generate QR code
qr = qrcode.make(uri)
qr.save('totp_qr.png') # This saves it in your current folder
print('QR code saved to totp_qr.png')

# Generate current OTP
current_otp = totp.now()
print(f'Current OTP: {current_otp}')
print(f'Valid for: {30 - (__import__("time").time() % 30):.0f} more seconds')