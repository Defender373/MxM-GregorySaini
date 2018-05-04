import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#Takes a long time to load
model = gensim.models.KeyedVectors.load_word2vec_format(r'D:\MxM-Project\GoogleNews-vectors-negative300.bin', binary = True)
vocab = model.vocab.keys()


#the word 'of' is not in the vocabulary


sentence = ["(London)", ".", "'",   "/" , " \" " , "!" , "is", "the", "capital", "of" ,"Great", "Britain"]

#In order to maximize the number of words that will be put into the Vector model, we will clear the words of any extraneous syntax such as parentheses, that would otherwise prevent the word from being used
counter = 0
for clean in sentence:
    for each in clean:
        if each == "(":
            clean = clean.strip("(")
        if each == ")":
            clean = clean.strip(")")
        if each == ",":
            clean = clean.strip(",")
        if each == "[":
            clean = clean.strip("[")
        if each == "]":
            clean = clean.strip("]")
        if each == "?":
            clean = clean.strip("?")
        if each == "-":
            clean = clean.strip("-")
        if each == ".":
            clean = clean.strip(".")
        if each == "'":
            clean = clean.strip("'")
        if each == "/":
            clean = clean.strip("/")
        if each == '"':
            clean = clean.strip('"')
        if each == "!":
            clean = clean.strip("!")
    
    sentence[counter] = clean
    counter = counter + 1

print(sentence)


vectors = []
for w in sentence:
    if w in vocab:
        vectors.append(model[w])
    else:
        print("Word '{}' not in vocab".format(w))
        vectors.append([0])
        
print(len(vectors))        

        
#vectors = [model[w] for w in sentence]
#print(len(vectors))
#print(vectors[0]) This would print out an array of numbers for a single word




#First we put all of the songs' titles, composers, etc into a single respective array

file = 'D:\\MxM-Project\\songFinal.txt'
#D:\MxM-Project
f = open(file, 'r')

songsWithAllInfo = []
songTitle = []
singerName = []
albumName = []
for song in f:
    enterRemover = song.rstrip("\n")
    enterRemover = enterRemover.split("\t")
    songTitle.append(enterRemover[0])
    singerName.append(enterRemover[1])
    albumName.append(enterRemover[2])
    #print(enterRemover.split("\t"))
    songsWithAllInfo.append(enterRemover)





#print(songsWithAllInfo[0][0])
#songsWithAllInfo[song][category]
'''
Categories:
1. Song Title
2. Singer
3. Album (May be same as song title if it is a single)
'''



#print(model.most_similar(positive=['woman', 'king'], negative=['man']))

#print(model.doesnt_match("breakfast cereal dinner lunch".split()))

#print(model.similarity('woman', 'man'))


#vocab = model.vocab.keys()





#model.score(["The fox jumped over a lazy dog".split()])

'''
fileNum = 1

wordsInVocab = len(vocab)
wordsPerFile = int(100E3)

# Write out the words in 100k chunks.
for wordIndex in range(0, wordsInVocab, wordsPerFile):
    # Write out the chunk to a numbered text file.    
    with open("vocabulary/vocabulary_%.2d.txt" % fileNum, 'w') as f:
        # For each word in the current chunk...        
        for i in range(wordIndex, wordIndex + wordsPerFile):
            # Write it out and escape any unicode characters.            
            f.write(vocab[i].encode('UTF-8') + '\n')
    
    fileNum += 1
    
'''