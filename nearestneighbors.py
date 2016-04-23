import pickle
import numpy as np

def getNN(word, vocabulary, vocabulary_inv, embeddings, topn=2):
    # TODO: Implement this function
    return ['film', 'films']

if __name__ == "__main__":
    with open("vocabulary.pkl", "r") as f:
        vocabulary = pickle.load(f)
    with open("vocabulary_inv.pkl", "r") as f:
        vocabulary_inv = pickle.load(f)
    embeddings = np.load("embeddingMatrix.npy")

    # vocabulary maps a word to its corresponding index
    print(vocabulary["the"])
    # vocabulary_inv maps an index to its corresponding word
    print(vocabulary_inv[1])
    # embeddings[i, :] is the embedding vector of a word
    print(embeddings[1, :])

    print(getNN("movie", vocabulary, vocabulary_inv, embeddings))
