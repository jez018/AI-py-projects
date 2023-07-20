def stringCleaner(word):
    print('---inside stringCleaner')
    from nltk.corpus import stopwords

    word = list(word)
    counter = 0
    for letter in word:
        if letter.isalpha() == False:
            del word[counter]
        counter += 1
    word = ''.join(word)
    if word not in stopwords.words():
        return word
    else:
        return None