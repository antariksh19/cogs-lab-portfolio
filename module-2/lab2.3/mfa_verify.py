import pyotp, time


SECRET = 'LZ26GCDRULIJWGORWY2U47COLIA7M4BX'
totp = pyotp.TOTP(SECRET)

# Verify the current OTP
current = totp.now()
print(f'Server-generated OTP: {current}')
print(f'Verify (should be True): {totp.verify(current)}')

# Try with a wrong OTP
print(f'Verify wrong OTP (should be False): {totp.verify("000000")}')

# Show time-sensitivity — wait 31 seconds and try again
print('Waiting 31 seconds to show OTP rotation...')
time.sleep(31)
new_otp = totp.now()
print(f'New OTP after 31 seconds: {new_otp}')
print(f'Are they different? {current != new_otp}')