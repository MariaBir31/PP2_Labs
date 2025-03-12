#write a func that checks whether all words in a sentence start with capitalize lette using all
def all_words_capitalized(sentence):
    return all(word.istitle() for word in sentence.split())

sentence = "Hello World This Is Python"
print(all_words_capitalized(sentence))

