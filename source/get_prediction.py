# source/get_prediction.py

# Globals (will be set from main.py)
uni_freq = None
bi_freq = None
tri_freq = None
total_words = 0


def set_frequencies(uni, bi, tri):
    """
        Set the n-gram frequencies for prediction functions.
    """
    global uni_freq, bi_freq, tri_freq, total_words
    uni_freq = uni
    bi_freq = bi
    tri_freq = tri
    total_words = sum(uni_freq.values())


def predict_next_unigram():
    """
        Predict the most likely unigram.
    """
    max_prob = 0
    next_word = None
    for word, count in uni_freq.items():
        prob = count / total_words
        if prob > max_prob:
            max_prob = prob
            next_word = word
    return next_word


def predict_next_bigram(word):
    """
        Predict next word given one word; backoff to unigram if word not found.
    """
    words = [(w2, count) for (w1, w2), count in bi_freq.items() if w1 == word]

    if words:
        # MLE probability = count(w1, w2) / count(w1)
        word_count = sum([c for (w2, c) in words])
        next_word, _ = max(words, key=lambda x: x[1] / word_count)
        return next_word
    else:
        print(f"Word '{word}' not found in bigrams. Backing off to unigram.")
        return predict_next_unigram()


def predict_next_trigram(word1, word2):
    """
        Predict next word given two words; backoff to lower-order models if necessary.
    """
    # Step 1: Try trigram
    words = [(w3, count) for (w1, w2, w3), count in tri_freq.items() if w1 == word1 and w2 == word2]
    if words:
        # MLE probability = count(w1, w2, w3) / count(w1, w2)
        total_count = sum([c for (w3, c) in words])
        next_word, _ = max(words, key=lambda x: x[1] / total_count)
        return next_word

    # Step 2: Backoff to bigram using word2
    words_bi = [(w2, c) for (w1, w2), c in bi_freq.items() if w1 == word2]
    if words_bi:
        print(f"Trigram '{word1} {word2}' not found. Backing off to bigram with '{word2}'.")
        return predict_next_bigram(word2)

    # Step 3: Backoff to bigram using word1
    words_bi_w1 = [(w2, c) for (w1, w2), c in bi_freq.items() if w1 == word1]
    if words_bi_w1:
        print(f"Trigram '{word1} {word2}' not found. Backing off to bigram with '{word1}'.")
        return predict_next_bigram(word1)

    # Step 4: Backoff to unigram
    print(f"Trigram '{word1} {word2}' not found. Backing off to unigram.")
    return predict_next_unigram()