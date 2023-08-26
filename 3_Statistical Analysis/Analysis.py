################################### Importing libraries ###################################
import pandas as pd
import numpy as np
import mysql.connector
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title='Spotify Project',
)
st.title("Statistical Analysis on Spotify Data")

################################### Connecting to Database ###################################
my_database = mysql.connector.connect(
  host = "127.0.0.1",
  port = "3306",
  user = "root",
  password = "farzansql",
  auth_plugin = "mysql_native_password",
  database = "spotify"
)
cursor = my_database.cursor()

################################### Analyzing Top Five Albums of Each Artist Based on Popularity ###################################
cursor.execute("SELECT * FROM album")
album_data = cursor.fetchall()
album_df = pd.DataFrame(album_data, columns = [column[0] for column in cursor.description])
album_df = album_df[["album_id", "album_name", "popularity"]]
cursor.execute("SELECT * FROM artist")
artist_data = cursor.fetchall()
artist_df = pd.DataFrame(artist_data, columns = [column[0] for column in cursor.description])
artist_df = artist_df[["artist_id", "artist_name"]]
cursor.execute("SELECT * FROM artist_album")
artist_album_data = cursor.fetchall()
artist_album_df = pd.DataFrame(artist_album_data, columns = [column[0] for column in cursor.description])
artist_name_list = artist_df["artist_name"].unique().tolist()

st.subheader("Artist Name Selection")
selected_artist = st.selectbox("Select an artist name:", artist_name_list)
merged_df = pd.merge(artist_df, artist_album_df, on = "artist_id")
final_df = pd.merge(merged_df, album_df, on = "album_id")
artist_albums = final_df[final_df["artist_name"] == selected_artist]
top_albums = artist_albums.sort_values(by = "popularity", ascending = False).head(5)
result_df = top_albums[["album_name", "popularity"]]

fig = px.bar(top_albums, x = "album_name", y = "popularity", text = "popularity", color = "popularity", title = f"Top Albums by {selected_artist}", labels = {"popularity": "Popularity"}, height = 500)
fig.update_traces(texttemplate = "%{text}", textposition = "outside")
fig.update_layout(xaxis_title = "Album Name", yaxis_title = "Popularity")
fig.update_xaxes(tickangle = -45)

st.subheader("Top Albums by Artist")
st.write(f"You selected: {selected_artist}")
st.plotly_chart(fig, use_container_width = True)

################################### A Study of the Top 10 Chart-Topping Songs in Different Musical Categories ###################################
cursor.execute("SELECT * FROM genre")
genre_data = cursor.fetchall()
genre_df = pd.DataFrame(genre_data, columns = [column[0] for column in cursor.description])
genre_df = genre_df[["genre_id", "genres_name"]]
genre_df = genre_df[:21]
cursor.execute("SELECT * FROM track_info")
track_data = cursor.fetchall()
track_df = pd.DataFrame(track_data, columns=[column[0] for column in cursor.description])
track_df = track_df[["genre_id", "title", "popularity"]]
genre_name_list = genre_df["genres_name"].unique().tolist()

st.subheader("Genre Name Selection")
selected_genre = st.selectbox("Select an genre name:", genre_name_list)
selected_genre_id = genre_df[genre_df["genres_name"] == selected_genre]["genre_id"].values[0]
selected_tracks = track_df[track_df["genre_id"] == selected_genre_id]
selected_tracks = selected_tracks.nlargest(10, "popularity")

fig = px.bar(selected_tracks, x = "popularity", y = "title", orientation = "h", color = "popularity", labels = {"popularity": "Popularity", "title": "Track Title"}, title = f"Top 10 Most Popular Tracks in the {selected_genre} Genre")
fig.update_layout(annotations = [dict(x = popularity, y = title, text = str(popularity), xanchor = "left", showarrow = False) for popularity, title in zip(selected_tracks["popularity"], selected_tracks["title"])])
st.plotly_chart(fig)

################################### Exploring the Top 10 Most Popular Artists by Genre ###################################
st.subheader('Question 4')
# get data
query = """
SELECT artist_name, popularity, genres_name FROM spotify.artist_genre
join artist on artist.artist_id = artist_genre.artist_id
join genre on genre.genre_id = artist_genre.genre_id;
"""

cursor.execute(query)
rows = cursor.fetchall()

column_names = [column[0] for column in cursor.description]
artistGenre_popularityBased = pd.DataFrame(rows, columns = column_names)

# get genre name from user
genre_selected = st.selectbox('Select genre:', sorted(artistGenre_popularityBased['genres_name'].unique()), index=1463, key='k1')
top_10_artists = artistGenre_popularityBased.query('genres_name == @genre_selected').sort_values(by=['popularity', 'artist_name'], ascending=True)[:10]

st.write(f"Most popular artists in {genre_selected} genre:")
# create a bar chart using st.bar_chart
st.bar_chart(top_10_artists[['artist_name', 'popularity']].set_index('artist_name'))

################################### Exploring Beloved Albums: A Comparative Analysis of Five Notable Releases in the Year ###################################
st.subheader('Question 5')
# get data
query = """
SELECT album_name, artists, release_date, popularity FROM spotify.album;
"""

cursor.execute(query)
rows = cursor.fetchall()

column_names = [column[0] for column in cursor.description]
album_yearBased = pd.DataFrame(rows, columns = column_names)
album_yearBased['release_date'] = pd.to_datetime(album_yearBased['release_date'], format='%Y-%m-%d', errors='coerce')

# get the min and max year of the release_date column
min_year, max_year = map(int, album_yearBased['release_date'].dt.year.agg(['min', 'max']))

year_selected = st.slider(
    'Select a range of years:',
    min_year, max_year, (1990, 2010))
st.write(f'Most popular albums from **{year_selected[0]}** to **{year_selected[1]}**:')

# filter dataFrame by selected years
top_5_albums = album_yearBased.query('release_date.dt.year >= @year_selected[0] and release_date.dt.year <= @year_selected[1]').sort_values(by=['popularity', 'release_date'], ascending=False)[:5]

st.dataframe(top_5_albums.set_index('album_name').astype({'release_date': 'str'}))

#  Study of the Top Ten Artists with the Most Evocative Lyrics 
st.subheader('Question 6')
st.subheader('Study of the Top Ten Artists with the Most Evocative Lyrics:')

cursor.execute('select * from track_lyric;')
track_lyric = cursor.fetchall()
track_lyric = pd.DataFrame(track_lyric, columns = [column[0] for column in cursor.description])
cursor.execute("select * from artist;")
artist = cursor.fetchall()
artist = pd.DataFrame(artist, columns = [column[0] for column in cursor.description])
cursor.execute("select * from track_info;")
track_info = cursor.fetchall()
track_info = pd.DataFrame(track_info, columns = [column[0] for column in cursor.description])


artist_lyric_track=pd.merge(artist,track_info,how='inner',on='artist_id')
artist_lyric_track=pd.merge(artist_lyric_track,track_lyric,how='inner',on='track_id')
artist_lyric_track=artist_lyric_track[['artist_id','artist_name','track_id','anger','disgust','fear','joy','sadness','surprise','trust','negative','positive']]

x=artist_lyric_track.mask(artist_lyric_track.select_dtypes(include=np.number) <= 0)
artist_lyric_track.loc[:,'anger':]=x

artist_lyric_track=artist_lyric_track.groupby(by='artist_id')[['anger','disgust','fear','joy','sadness','surprise','trust','negative','positive']].sum()

result=pd.merge(artist_lyric_track,artist,how='inner',on='artist_id')
result=result[['artist_id','artist_name','anger','disgust','fear','joy','sadness','surprise','trust','negative','positive']]

all_optiona=result.columns.to_list()[2:]
option=st.selectbox('select an option:',options=all_optiona)
result=result.sort_values(by=option,ascending=False).reset_index()

fig = px.bar(result.loc[:9,['artist_name',option]], x="artist_name", y=option,color = "artist_name",labels = {"artist_name": "Artist Name"},title =f"top 10 singers based on {option}")
st.plotly_chart(fig, use_container_width = True)

###################################  A Study of Annual Distribution of Artist Activity (Total Album Counts) ###################################

################################### A Study of the Top 10 Explicit Songs ###################################

################################### Close the Database connection ###################################
cursor.close()
my_database.close()