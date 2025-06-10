from db.db_utils import get_user_by_mobile, get_loan_info
from chatbot.otp_handler import generate_and_store_otp
from chatbot.prompt_engine import generate_response

def chat():
    query = input("User: ")
    if "emi" not in query.lower():
        print("Bot: Sorry, I can only help with EMI-related queries.")
        return

    mobile = input("Bot: Please enter your registered mobile number: ")
    user = get_user_by_mobile(mobile)
    if not user:
        print("Bot: Mobile number not found.")
        return

    otp = generate_and_store_otp(mobile)
    otp_input = input("Bot: Enter the OTP sent to your mobile: ")

    if otp_input != otp:
        print("Bot: ❌ OTP verification failed.")
        return

    loan = get_loan_info(user['id'])
    if not loan:
        print("Bot: No EMI info found.")
        return

    response = generate_response(query, loan)
    print("Bot:", response)
