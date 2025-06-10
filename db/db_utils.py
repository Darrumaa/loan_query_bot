import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def get_user_by_mobile(mobile):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE mobile = %s", (mobile,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_loan_info(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM loans WHERE user_id = %s", (user_id,))
    loan = cursor.fetchone()
    conn.close()
    return loan

def store_otp(mobile, otp):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET otp = %s WHERE mobile = %s", (otp, mobile))
    conn.commit()
    conn.close()
