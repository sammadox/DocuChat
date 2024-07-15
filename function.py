import nltk
from nltk.data import find
from nltk.data import load

# Attempt to find 'punkt' tokenizer
try:
    punkt_path = find('tokenizers/punkt')
    print(f"'punkt' tokenizer found at: {punkt_path}")
except LookupError:
    print("'punkt' tokenizer not found. Downloading...")
    nltk.download('punkt')
    print("Downloaded 'punkt' tokenizer.")

# Verify that 'punkt' tokenizer can be loaded
try:
    tokenizer = load('tokenizers/punkt/english.pickle')
    print("'punkt' tokenizer loaded successfully.")
except LookupError:
    print("Failed to load 'punkt' tokenizer.")
