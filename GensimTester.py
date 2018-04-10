
#print("Hello")
#from gensim import corpora, models, similarities

import gensim
#from gensim.models import Word2Vec
model = gensim.models.KeyedVectors.load_word2vec_format(r'C:\Users\Gregory\Desktop\GoogleNews-vectors-negative300.bin', binary=True)
#model.score(["The fox jumped over a lazy dog".split()])

