import pyotp

def generate_secret_key():
    secret_key = pyotp.random_base32()
    print("Secret Key:", secret_key)
    return secret_key

if __name__ == "__main__":
    generate_secret_key()
