import ollama

def generate_summary(text):

    prompt = f"""
Summarize the following content
in a concise and clear way.

Content:
{text}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]