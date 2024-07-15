import nltk
import os

# Set the NLTK data path to the local nltk_data directory
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Now you can safely import and use the NLTK functions
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_text(text):
    """
    Tokenizes the given text into sentences and words.

    :param text: The input text.
    :return: A list of sentences, where each sentence is a list of words.
    """
    sentences = nltk.sent_tokenize(text)
    words = [nltk.word_tokenize(sentence) for sentence in sentences]
    return words

nltk.download('averaged_perceptron_tagger')

def pos_tag_sentences(sentences):
    """
    Tags each word in the sentences with its part of speech.

    :param sentences: A list of sentences, where each sentence is a list of words.
    :return: A list of sentences with POS tags.
    """
    pos_tagged_sentences = [nltk.pos_tag(sentence) for sentence in sentences]
    return pos_tagged_sentences

def chunk_sentences(pos_tagged_sentences, grammar):
    """
    Chunks the POS-tagged sentences based on the provided grammar.

    :param pos_tagged_sentences: A list of POS-tagged sentences.
    :param grammar: A grammar rule for chunking.
    :return: A list of chunked sentences.
    """
    chunk_parser = nltk.RegexpParser(grammar)
    chunked_sentences = [chunk_parser.parse(sentence) for sentence in pos_tagged_sentences]
    return chunked_sentences
def chunk_text(text, grammar):
    """
    Tokenizes, POS-tags, and chunks the given text.

    :param text: The input text.
    :param grammar: The grammar rule for chunking.
    :return: Chunked sentences.
    """
    sentences = tokenize_text(text)
    pos_tagged_sentences = pos_tag_sentences(sentences)
    chunked_sentences = chunk_sentences(pos_tagged_sentences, grammar)
    return chunked_sentences

def flatten_chunked_sentences(chunked_sentences):
    """
    Flattens chunked sentences back into plain text.

    :param chunked_sentences: A list of chunked sentences.
    :return: A list of sentences in plain text.
    """
    flattened_sentences = []
    for chunked_sentence in chunked_sentences:
        sentence = []
        for chunk in chunked_sentence:
            if isinstance(chunk, nltk.Tree):
                # Join words in the chunk (e.g., a noun phrase)
                sentence.append(" ".join(word for word, pos in chunk.leaves()))
            else:
                # It's a tuple (word, pos)
                word, pos = chunk
                sentence.append(word)
        flattened_sentences.append(" ".join(sentence))
    return flattened_sentences

