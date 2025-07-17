def mostWordsFound(sentences):
    return max(len(sentences[i].split()) for i in range(len(sentences)))
