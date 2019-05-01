# import numpy as np
import pandas as pd
# import random
# import matplotlib.pyplot as plt
# import operator
# from wordcloud import WordCloud, STOPWORDS #used to generate world cloud

r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']

data = pd.read_csv('ml-100k/u1.base', delimiter='\t', names=r_cols, encoding='latin-1')

# A. for each movie- average rating todo: needs merge?
r_data = data.groupby('movie_id')['rating'].mean()
# how many unique rates
u_rates = data['rating'].unique().tolist()  # todo: needs to do ceil? or floor?
num_u_rates = len(u_rates)
print(data.shape)
print(r_data.shape)
print(u_rates.shape)
print(num_u_rates)
