import json
from AzureOp import send_chat_message

def add_message(conversation, role, content):
    new_message = {"role": role, "content": content}
    conversation.append(new_message)
    return conversation

def update_message(conversation, index, new_content):
    if 0 <= index < len(conversation):
        conversation[index]['content'] = new_content
    else:
        print("Invalid index.")
    return conversation

def delete_message(conversation, index):
    if 0 <= index < len(conversation):
        del conversation[index]
    else:
        print("Invalid index.")
    return conversation

def get_message_content(conversation, index):
    if 0 <= index < len(conversation):
        return conversation[index]['content']
    else:
        print("Invalid index.")
        return None

# messages_operations.py

def format_message(message, user):
    return f"User {user} says: {message}"

def parse_message(formatted_message):
    if ":" in formatted_message:
        user, message = formatted_message.split(":", 1)
        user = user.replace("User ", "").strip()
        message = message.strip()
        return user, message
    return None, None


def test_get_message_content():
    # Sample conversation data
    conversation = [
        {"content": "Hello! How can I help you today?"},
        {"content": "Can you tell me the weather forecast for today?"},
        {"content": "Sure, the weather today is sunny with a high of 25 degrees."},
    ]

    # Test cases
    test_cases = [
        (conversation, 0, "Hello! How can I help you today?"), # Valid index
        (conversation, 1, "Can you tell me the weather forecast for today?"), # Valid index
        (conversation, 2, "Sure, the weather today is sunny with a high of 25 degrees."), # Valid index
        (conversation, -1, None), # Invalid index
        (conversation, 3, None), # Invalid index
        (conversation, 100, None), # Invalid index
    ]

    # Testing the function
    for i, (conv, index, expected) in enumerate(test_cases):
        result = get_message_content(conv, index)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        if result is None:
            print(f"Test case {i+1} passed with invalid index: {index}")
        else:
            print(f"Test case {i+1} passed: {result}")

# Define the function to be tested
def get_message_content(conversation, index):
    if 0 <= index < len(conversation):
        return conversation[index]['content']
    else:
        print("Invalid index.")
        return None

# Run the test
def HasInfo(userquery, chunk):
    conversation = []
    conversation = add_message(conversation, "user", "can the following question " + userquery + " be answered from the following text " + chunk + " reply with a yes or no")
    # More logic here
    res=send_chat_message(conversation)
    return res

# Example usage
