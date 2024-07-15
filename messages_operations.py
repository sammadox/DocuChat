import json

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


