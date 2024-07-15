import os
from openai import AzureOpenAI

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv('.env')  # Adjust the path if your .env file is located elsewhere



def send_chat_message(messages):
    # Initialize the client using environment variables
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT'")
    )

    response = client.chat.completions.create(
        model="DgOpenApiChat1Dev",
        messages=messages
    )

    return response


