import json

def load_json(json_string):
    """Load JSON data from a string."""
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None

def extract_main_content(data):
    """Extract the main content from JSON data."""
    if isinstance(data, list) and len(data) > 0:
        return data[0].get('content', None)
    return None

def extract_qa_pairs(data):
    """Extract QA pairs from JSON data."""
    if isinstance(data, list) and len(data) > 0:
        return data[0].get('qa_pair', {})
    return {}

def add_qa_pair(data, question, answer):
    """Add a new QA pair to the JSON data."""
    if isinstance(data, list) and len(data) > 0:
        if 'qa_pair' not in data[0]:
            data[0]['qa_pair'] = {}
        data[0]['qa_pair']['question'] = question
        data[0]['qa_pair']['answer'] = answer
        return True
    return False

# Example JSON string
json_string = '''
[
    {
        "role": "user",
        "content": "January 23 , 2024 Client Name Address Wilmington DE 19803 Dear Client Name : Belfint , Lyons & Shuman , P.A .",
        "qa_pair": {
            "question": "What is the client's address?",
            "answer": "Wilmington DE 19803"
        }
    }
]
'''

# Using the functions
data = load_json(json_string)
if data:
    content = extract_main_content(data)
    qa_pair = extract_qa_pairs(data)
    
    print("Content:", content)
    print("QA Pair:", qa_pair)
    
    # Adding a new QA pair
    if add_qa_pair(data, "What is the date?", "January 23, 2024"):
        print("Updated Data:", json.dumps(data, indent=2))
    else:
        print("Failed to add QA pair.")
