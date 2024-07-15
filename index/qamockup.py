import json

class Document:
    def __init__(self, role, content, doc_id):
        self.document = {
            "role": role,
            "content": content,
            "id": doc_id,
            "qa": []  # Adding a list to hold questions and answers
        }
    
    def add_question(self, question):
        # Adds a new question with an empty answer field
        self.document['qa'].append({"question": question, "answer": ""})
    
    def add_answer(self, question, answer):
        # Finds the question and adds/updates the answer
        for qa in self.document['qa']:
            if qa['question'] == question:
                qa['answer'] = answer
                return True
        return False  # If the question was not found
    
    def get_all_qa(self):
        # Returns all questions and answers
        return self.document['qa']
    
    def get_document(self):
        # Returns the entire document structure
        return self.document
    
    def save_to_json(self, filename):
        # Saves the document structure to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(self.document, json_file, indent=4)

# Example usage
doc = Document(
    role="user",
    content="January 23, 2024 Client Name Address Wilmington DE 19803 Dear Client Name: Belfint, Lyons & Shuman, P.A.",
    doc_id="4fc9e403-beb0-4f10-a8cc-827a4bd26720"
)

# Adding questions
doc.add_question("What is the date of the letter?")
doc.add_question("Who is the client?")

# Adding answers
doc.add_answer("What is the date of the letter?", "January 23, 2024")
doc.add_answer("Who is the client?", "Client Name")

# Saving to JSON
doc.save_to_json("document.json")

# Print to verify
print("Document saved as document.json")
