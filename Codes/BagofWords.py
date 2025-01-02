import numpy as np
from collections import Counter

def bag_of_words(texts, binary=False):
    """
    Create a Bag of Words representation from a list of texts.

    Args:
        texts (list of str): Input texts.
        binary (bool): If True, use binary representation (presence/absence).
                      If False, use count-based representation.

    Returns:
        tuple: (vocabulary, BoW matrix)
               - vocabulary: List of words in the vocabulary.
               - BoW matrix: 2D NumPy array (documents x vocabulary size).
    """
    # Tokenize and build vocabulary
    tokenized_texts = [text.lower().split() for text in texts]
    vocabulary = sorted(set(word for text in tokenized_texts for word in text))
    vocab_index = {word: idx for idx, word in enumerate(vocabulary)}

    # Initialize the BoW matrix
    bow_matrix = np.zeros((len(texts), len(vocabulary)), dtype=int)

    # Populate the matrix
    for doc_idx, text in enumerate(tokenized_texts):
        word_counts = Counter(text)  # Count word frequencies
        for word, count in word_counts.items():
            if word in vocab_index:
                bow_matrix[doc_idx, vocab_index[word]] = 1 if binary else count

    return vocabulary, bow_matrix
