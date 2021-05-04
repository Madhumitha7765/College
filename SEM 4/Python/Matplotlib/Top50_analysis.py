import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import plotly as py
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, plot
import warnings
warnings.filterwarnings("ignore")


# loading data from csv files
def load_data():
    sData = pd.read_csv('csv/top50.csv', encoding="windows-1252")
    # renaming column values to desired variables
    sData = sData.rename(columns = {"Speechiness." : "Speechiness","Unnamed: 0" : "id","Track.Name" : "track_name", "Artist.Name" : "artist_name", "Beats.Per.Minute" : "b_p_m", "Loudness..dB.." : "loudness_db", "Valence." : "valence", "Length." : "length","Acousticness.." : "Acousticness" })
    sData = sData.drop(["id"], axis = 1)
    return sData



# function to plot popularity scores of genres
def genre_popularity():
    # popularity scores of genres
    genres = sData.Genre.unique()
    popularity_scores = []
    # append sum of scores and append to popularity scores list
    for g in genres:
        var = sData[sData.Genre == g]
        popularity = sum(var.Popularity)
        popularity_scores.append(popularity)

    # plotting figure
    plt.figure(figsize=(10, 10))
    sns.barplot(x=genres, y=popularity_scores, palette=sns.cubehelix_palette(len(genres)))

    # fixing scale factor for y axes
    scale_factor = 1
    ymin, ymax = plt.ylim()
    plt.ylim(ymin * scale_factor, ymax * scale_factor)

    # specifying plot labels and features
    plt.xticks(rotation=90,fontsize=7)
    plt.xlabel("Genres")
    plt.ylabel("Total popularity scores")
    plt.title("Genre/Popularity")
    plt.show()




# function to plot popularity scores of artists
def artist_popularity():

    global artis
    artis = sData.artist_name.value_counts()
    global artist_name
    artist_name = artis.index
    global artist_popularity
    artist_popularity = []
    # append sum of scores and append to popularity list
    for a in artist_name:
        artist = sData[sData.artist_name == a]
        popularity = sum(artist.Popularity)
        artist_popularity.append(popularity)

    # specifying plot labels and features
    plt.figure(figsize=(10, 10))
    sns.barplot(x=artist_name, y=artist_popularity, palette=sns.cubehelix_palette(len(artist_name)))
    plt.xticks(rotation=90,fontsize=7)
    plt.title("Artist/Popularity")
    plt.show()


def track_popularity():

    # track popularity
    plt.subplots(figsize=(10, 10))
    # specifying plot labels and features
    sns.pointplot(x=sData.track_name, y=sData.Popularity, color="cyan", alpha=0.5)
    plt.title("Track Name / Popularity")
    plt.xticks(rotation=90,fontsize=7)
    plt.show()

def pie_chart():

    # precentage pie chat
    a = sData.Genre.value_counts()
    labels = a.index
    colors = ["red", "blue", "cyan", "yellow"]
    #colors = ["lightcoral", "tomato", "violet", "mediumorchid"]
    explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(len(explode))
    sizes = a.values
    # specifying plot labels and features
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.show()

    # artisit pie
    artis = sData.artist_name.value_counts()

    labels = artis.index
    colors = ['palevioletred', 'hotpink', 'violet', 'mediumorchid', 'darkviolet']
    #colors = ["red", "blue", "cyan", "mediumorchid"]
    #explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               #0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    explode = [0,0.5, 0, 0.5, 0,0.5, 0, 0.5, 0, 0.5, 0, 0.5, 0,0.5, 0, 0.5, 0,0.5, 0, 0.5, 0, 0.5, 0, 0.5, 0, 0.2, 0, 0.5, 0, 0.5, 0, 0.5, 0, 0.5, 0,
               0.5, 0, 0.5]
    size = artis.values
    # specifying plot labels and features
    plt.figure(figsize=(10, 10))
    plt.pie(size, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%')
    plt.show()

# function to display no of popular songs for each artist
def artist_stats():

    # Artist's Popular Track Numbers
    # plotting scatter graph
    trace2 = go.Scatter(
        x=artist_name,
        y=artis.values,
        name="Track Number",
        mode='markers+lines',
        marker=dict(color="red"),
        text=artis.values,
    )

    data = [trace2]
    layout = dict(title="Artist's Popular Track Numbers")
    fig = dict(data=data, layout=layout)
    plot(fig)



if __name__ == "__main__":

    # loading data from csv files
    sData = load_data()

    # function calls
    artist_popularity()
    genre_popularity()
    track_popularity()
    pie_chart()
    artist_stats()










