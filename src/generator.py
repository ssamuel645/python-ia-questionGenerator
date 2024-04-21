from blessings import Terminal
from openai import OpenAI
import json

client = OpenAI(
    api_key='YOUR_API_KEY'
)
term = Terminal()

def generate_question(topic):
    answer = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": """
                You're a highly experienced developer with knowledge across different stacks and theoretical concepts in programming and software engineering.
                You're working on a pre-hiring process, and your task now is to write questions for an interview.
                Each question should have 4 possible answers, with one of them being correct.
                Write these questions in the following format:
                '{"question": "Question", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "correct": "Option 1"}'
            """
        }, {
            "role": "user",
            "content": f"Generate a question about {topic}"
        }]
    )

    content = answer.choices[0].message.content
    return json.loads(content)

score = 0
topic = input("What topic you want to answer about? ")

while topic:
    print("Loading...")
    question = generate_question(topic)
    print(term.clear)
    print(term.bold_underline(question['question']))