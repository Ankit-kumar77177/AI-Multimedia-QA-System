import ollama

def ask_question(context, question):

    prompt = f"""
    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
         model='tinyllama',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content'] 