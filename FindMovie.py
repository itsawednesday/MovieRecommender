import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movieFile = pd.read_csv('/Users/noor/Downloads/movies.csv')

creditsFile = pd.read_csv('/Users/noor/Downloads/credits.csv')
creditsFile.columns = ['id','titles','cast','crew']


movieFile= movieFile.merge(creditsFile,on='id')


tfidf = TfidfVectorizer(stop_words='english')

movieFile['overview'] = movieFile['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(movieFile['overview'])
tfidf_matrix.shape


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movieFile.index, index=movieFile['title']).drop_duplicates()

#  output most similar movies
def getRecommendations(title, cosine_sim=cosine_sim):
    # get the index of the movie that matches the title
    index = indices[title]

    scores = list(enumerate(cosine_sim[index]))
    scores = sorted(scores, key= lambda x: x[1], reverse=True)
    scores = scores[1:11]

    movie_indices = [i[0] for i in scores]
    return movieFile['title'].iloc[movie_indices]


print (getRecommendations('Niagara'))