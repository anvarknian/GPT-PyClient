import os
from dotenv import load_dotenv
from openai import OpenAI, AzureOpenAI

load_dotenv()

engine_type = os.getenv("ENGINE_TYPE", "chatgpt")
model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo-1106")

api_key = os.getenv("API_KEY")
endpoint = os.getenv("ENDPOINT")
api_version = os.getenv("API_VERSION")

max_tokens = int(os.getenv("MAX_TOKENS", 150))
temperature = float(os.getenv("TEMPERATURE", 0.7))

system_prompt = os.getenv("SYSTEM_PROMPT", "")


def setup_client():
    client = None
    print(f'Your settings are set to:\n '
          f'Engine: {engine_type}\n '
          f'Model Name: {model_name}\n '          
          f'System prompt: {system_prompt}\n '
          f'Temperature: {temperature}\n '
          f'Max tokens: {max_tokens}')
    if engine_type.lower() == 'chatgpt':
        client = OpenAI(api_key=api_key)
    elif engine_type.lower() == 'azure':
        client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=endpoint,
            azure_deployment=model_name,
            api_version=api_version
        )
    return client


def query_llm(client, query: str) -> str:
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        temperature=temperature,
    )
    return completion.choices[0].message.content


def run():
    client = setup_client()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Client: Goodbye!")
            break
        if not user_input:
            print("Client: What is your question?")
        else:
            response = query_llm(client, user_input)
            print(f"Client: {response}")
