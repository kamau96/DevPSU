#DevPSU Project #4
#Name: Benson Kamau
original = input('Enter a sentence:')
word_list = original.split()
result = []

for word in word_list:
    if word[0] in "aeiouyAEIOUY":
        word=word+ "yay"
        result.append(word)
    else:
        while word[0] not in "aeiouyAEIOUY":
            word = word[1:] + word[0]
        word += "ay"
        result.append(word)


final_sentence = " ".join(result)
print(final_sentence[0] + final_sentence[1:])