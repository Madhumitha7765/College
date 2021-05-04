import pandas as pd
import plotly.express as px

data = pd.read_csv("csv/data.csv")

# function to get the exact deacde years
def get_decade(year):
    first_year = int(year/10)*10
    decade = str(first_year)+"s"
    return decade

# counting songs for each decade
def decade_song_count():
    data["decade"] = data["year"].apply(get_decade)
    fig = px.histogram(data.sort_values("decade"), x="decade", color="decade", width=800, height=400)
    fig.show()

if __name__=="__main__":

    # function call
    decade_song_count()