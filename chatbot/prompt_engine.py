import ollama

def generate_response(user_query, emi_info):
    prompt = f"""
You are a helpful bank assistant. A user asked: "{user_query}"

EMI Details:
- Amount: ₹{emi_info['emi_amount']}
- Due Date: {emi_info['next_emi_date']}

Respond clearly and politely.
"""

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
