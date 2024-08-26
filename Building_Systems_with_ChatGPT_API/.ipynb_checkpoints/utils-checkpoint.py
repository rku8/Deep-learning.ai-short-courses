from dotenv import load_dotenv
from groq import Groq
import os
import openai

load_dotenv()

client_openai = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

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

def get_completion_from_messages(messages, model="llama3-8b-8192", client=client, temperature=0.0, max_tokens=500) -> str:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    
    return chat_completion.choices[0].message.content

def get_completion_with_openai(prompt, model="llama3-8b-8192"):
    messages = [{"role": "user", "content": prompt}]
    response = client_openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_completion_with_openai_from_messages(messages, 
                                 model="llama3-8b-8192", 
                                 temperature=0, 
                                 max_tokens=500):
    response = client_openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message.content

def get_completion_and_token_count(messages, 
                                   model="llama3-8b-8192", 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content
    
    token_dict = {
'prompt_tokens':response.usage.prompt_tokens,
'completion_tokens':response.usage.completion_tokens,
'total_tokens':response.usage.total_tokens,
    }

    return content, token_dict