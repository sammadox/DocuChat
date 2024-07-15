import json

# Function to read JSON data from a file
def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Load QA pairs from a local JSON file
qa_pairs = load_json_file('qa_pairs.json')['qa_pairs']

# User's input
user_input = "What are entities that filled PA returns?"

# Tokenize user input and predefined questions for better matching
def tokenize(text):
    return set(text.lower().replace('?', '').split())

user_input_tokens = tokenize(user_input)

# Function to match questions considering specific keywords in user query and return top 20%
def advanced_match(user_input, qa_pairs):
    matches = []
    
    for qa_pair in qa_pairs:
        question_tokens = tokenize(qa_pair['question'])
        common_tokens = user_input_tokens.intersection(question_tokens)
        match_ratio = len(common_tokens) / len(user_input_tokens)
        matches.append((match_ratio, qa_pair['question'], qa_pair['answer']))

    # Sort matches based on the match_ratio in descending order
    matches.sort(reverse=True, key=lambda x: x[0])

    # Select the top 20% of the matches
    top_20_percent_index = max(1, len(matches) // 5)  # Ensure at least one match is returned
    top_matches = matches[:top_20_percent_index]

    return top_matches

# Perform the matching
top_matches = advanced_match(user_input, qa_pairs)

# Prepare JSON response with the top matches
response = {
    "user_input": user_input,
    "top_matches": [{
        "question": match[1],
        "answer": match[2],
        "score": match[0]
    } for match in top_matches]
}

# Print or return JSON response
print(json.dumps(response, indent=2))
