import pyotp
import time

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key, interval=30)
    otp_code = totp.now()
    print("Generated OTP (valid for 30 sec):", otp_code)
    return otp_code

def verify_otp(secret_key, otp_code):
    totp = pyotp.TOTP(secret_key, interval=30)
    if totp.verify(otp_code, for_time=time.time()):
        print("OTP is valid")
        return True
    else:
        print("OTP is invalid (expired or incorrect)")
        return False

if __name__ == "__main__":
    secret_key = "JBSWY3DPEHPK3PXP"  # Replace this with the generated key
    otp = generate_otp(secret_key)
    time.sleep(5)  # Simulate delay
    verify_otp(secret_key, otp)
