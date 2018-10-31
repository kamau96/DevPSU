# DevPSU
Projects for the DevPSU progam



Pig LatinAncay youyay eakspay igpay atinlay? (Can you speak pig latin?) If you can’t, here are the rules:If a word begins with a consonant, take all of the letters before the first vowel and move them to the end of the word, then add ay to the end of the word. Examples: pig ? igpay, there ? erethay.If a word begins with a vowel (a, e, i, o, u, or y), simply add yay to the end of the word. For this problem, y is always a vowel. Examples: and ? andyay, ordinary ?ordinaryyay.Although there are many variants of Pig Latin (such as Kedelkloppersprook in Germany), for this problem we will always use the rules described above.A friend of yours was frustrated with everyone writing in Pig Latin and has asked you to write a program to translate to Pig Latin for him. Ouldway youyay ebay osay indkay otay oday ityay? (Would you be so kind to do it?)InputInput consists of 1 to 4000 lines, ending at end of file. Each line contains up to 100 words, each word up to 30 characters long, using only the characters a–z (lowercase). Every word contains at least one vowel, and adjacent words are separated by a single space. No punctuation or special characters will appear in the input.OutputYour program should output the text translated to Pig Latin using the rules described above.Sample Input:i cant speak pig latinSample Output:iyay antcay eakspay igpay atinlay



#code starts here
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
#code ends here