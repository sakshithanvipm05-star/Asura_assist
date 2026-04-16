from openai import OpenAI

client = OpenAI()

def get_answer(query):
    prompt = f"""
Answer the question clearly and concisely.

Question: {query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
