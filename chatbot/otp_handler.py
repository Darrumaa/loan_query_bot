import random
from db.db_utils import store_otp

def generate_and_store_otp(mobile):
    otp = str(random.randint(100000, 999999))
    store_otp(mobile, otp)
    print(f"[DEBUG] OTP sent to {mobile}: {otp}")  # Simulated
    return otp