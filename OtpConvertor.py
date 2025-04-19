
import pyotp

# Your secret key
secret = "3O36OG5H3RG7XZ5V"

# Generate current TOTP
totp = pyotp.TOTP(secret)
print("Your current 2FA code is:", totp.now())


# !Have to install the library pip install pyotp