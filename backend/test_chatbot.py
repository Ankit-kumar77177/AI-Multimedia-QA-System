from app.services.chatbot_service import ask_question

context = """
Artificial Intelligence is the simulation of human intelligence.
Machine Learning is a subset of AI.
"""

question = "What is Machine Learning?"

answer = ask_question(context, question)

print(answer)