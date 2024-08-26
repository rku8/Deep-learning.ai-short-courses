from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(
    api_key=os.getenv('GROQ_API_KEY')
)

def get_completion(prompt: str, model="llama3-8b-8192", client=client, temperature=0.0) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=temperature
    )
    
    
    return chat_completion.choices[0].message.content

def get_completion_from_messages(messages, model="llama3-8b-8192", client=client, temperature=0.0) -> str:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature
    )
    
    
    return chat_completion.choices[0].message.content