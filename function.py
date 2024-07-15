import nltk
from nltk.data import find
from nltk.data import load

# Attempt to find 'averaged_perceptron_tagger'
try:
    tagger_path = find('taggers/averaged_perceptron_tagger')
    print(f"'averaged_perceptron_tagger' found at: {tagger_path}")
except LookupError:
    print("'averaged_perceptron_tagger' not found. Downloading...")
    nltk.download('averaged_perceptron_tagger')
    print("Downloaded 'averaged_perceptron_tagger'.")

# Verify that 'averaged_perceptron_tagger' can be loaded
try:
    tagger = load('taggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickle')
    print("'averaged_perceptron_tagger' loaded successfully.")
except LookupError:
    print("Failed to load 'averaged_perceptron_tagger'.")
