# OTP Generator

This project demonstrates how to generate and verify time-based one-time passwords (TOTP) using Python. 
It includes scripts to create a secret key, generate OTPs valid for 30 seconds, and verify them.

## Features
- Generate a secret key for OTP authentication.
- Generate a 6-digit OTP valid for 30 seconds.
- Verify OTPs within the valid time window.

## Installation
1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install pyotp
   ```

## Usage
- **Generate Secret Key**: Run `generate_secret.py` to create a secret key.
- **Generate and Verify OTP**: Run `generate_otp.py` to generate and verify OTPs.

## Requirements
- Python 3.7 or higher
- `pyotp` library

## License
This project is licensed under the MIT License.
