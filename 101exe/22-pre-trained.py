# 22. How to find similar words using pre-trained Word2Vec?
# Q. Find all similiar words to “amazing” using Google news Word2Vec.

# Import gensim api
import gensim.downloader as api

# Load the pretrained google news word2vec model
word2vec_model300 = api.load('word2vec-google-news-300')


# Using most_similar() function
word2vec_model300.most_similar('amazing')
