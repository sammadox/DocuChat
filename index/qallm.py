import os
from openai import AzureOpenAI
import json

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


data = {
    "role": "user",
    "content": "January 23, 2024 Client Name Address Wilmington DE 19803 Dear Client Name: Belfint, Lyons & Shuman, P.A.",
    "id": "4fc9e403-beb0-4f10-a8cc-827a4bd26720",
    "qa": [
        {
            "question": "What is the date of the letter?",
            "answer": "January 23, 2024"
        },
        {
            "question": "Who is the client?",
            "answer": "Client Name"
        }
    ]
}
messages = [
    {"role": "user", "content": "From the following text \"January 23 , 2024 Client Name Address Wilmington DE 19803 Dear Client Name : Belfint , Lyons & Shuman , P.A .\" what are all possible questions as well as there respective answers in a json format, return the json only"},
]


response = send_chat_message(messages)
print(response.choices[0].message.content)

data['qa'].extend(response['questions'])
# Converting back to JSON format to view the result
json_output = json.dumps(data, indent=4)
print(json_output)
