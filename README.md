# GPT-PyClient

GPT-PyClient is a Python client for querying GPT models using OpenAI's API or Azure's OpenAI Service. This client is configured using environment variables for ease of setup and security.

## Features

- Easy setup with environment variables.
- Configurable prompt, engine type, model name, endpoint, API version, and more.
- Simple interface for querying the GPT models.

## Prerequisites

- Python 3.8+
- `python-dotenv==1.0.1` library
- `openai==1.38.0` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/gpt-pyclient.git
    cd gpt-pyclient
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Setup

1. Create a `.env` file in the root directory of the project and add the appropriate environment variables based on your use case.

    ### For OpenAI ChatGPT:
    
        ```env
        ENGINE_TYPE=chatgpt
        MODEL_NAME=gpt-3.5-turbo-1106
        API_KEY=your_openai_api_key
        SYSTEM_PROMPT='you are a very smart ai copilot, your name is LLM-PyClient'
        MAX_TOKENS=300
        TEMPERATURE=0.7
        ```
    
    ### For Azure OpenAI:
    
        ```env
        ENGINE_TYPE=azure
        MODEL_NAME=mydeployment
        ENDPOINT=https://mydeployment.openai.azure.com/
        API_KEY=your_openai_api_key
        API_VERSION=2024-05-01-preview
        SYSTEM_PROMPT='you are a very smart ai copilot, your name is LLM-PyClient'
        MAX_TOKENS=300
        TEMPERATURE=0.7
        ```

2. Replace the placeholder values with your actual configuration:
    - `ENGINE_TYPE`: The type of engine you are using (`chatgpt` or `azure`).
    - `MODEL_NAME`: The model name (e.g., `gpt-3.5-turbo-1106` for ChatGPT, `mydeployment` for Azure OpenAI).
    - `ENDPOINT`: The endpoint URL for Azure OpenAI (not required for ChatGPT).
    - `API_KEY`: Your OpenAI API key.
    - `API_VERSION`: The API version for Azure OpenAI (not required for ChatGPT).
    - `SYSTEM_PROMPT`: The system prompt you want to use.
    - `MAX_TOKENS`: The maximum number of tokens to generate.
    - `TEMPERATURE`: The temperature setting for the model's responses.

## Usage

To Run the client:

```bash
python -m app
```
