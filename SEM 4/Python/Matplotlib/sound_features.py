import numpy as np
import pandas as pd
# The plotly.express module is plotly's API for rapid figure generation.
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv("csv/data.csv")
genre_data = pd.read_csv('csv/data_by_genres.csv')
year_data = pd.read_csv('csv/data_by_year.csv')

# function to display features of songs
def sound_features():
    sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence']
    fig = px.line(year_data, x='year', y=sound_features)
    fig.show()

# function to plot distribution of features in different genres
def genre_distribution():
    top10_genres = genre_data.nlargest(10, 'popularity')
    fig = px.bar(top10_genres, x='genres', y=['valence', 'energy', 'danceability', 'acousticness'], barmode='group')
    fig.show()

# correlation function to display how close 2 features are related
def heatmap():
    #Pearson Correlation Table
    main_df = pd.read_csv('csv/data.csv')
    main_corr_df = main_df.drop(['key','mode','year','explicit'],axis=1).corr(method='pearson')
    fig = px.imshow(main_corr_df,title="Song Feautures Pearson Correrlation Heatmap",width=750,height=500,labels={'color':"correlation"})
    fig.show()

if __name__=="__main__":

    # function calls
    sound_features()
    genre_distribution()
    heatmap()

