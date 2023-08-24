################################### Importing libraries ###################################
import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px

################################### Connecting to Database ###################################
my_database = mysql.connector.connect(
  host = "127.0.0.1",
  port = "3306",
  user = "root",
  password = "Your Password",
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

st.title("Artist Name Selection")
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

st.title("Top Albums by Artist")
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

st.title("Genre Name Selection")
selected_genre = st.selectbox("Select an genre name:", genre_name_list)
selected_genre_id = genre_df[genre_df["genres_name"] == selected_genre]["genre_id"].values[0]
selected_tracks = track_df[track_df["genre_id"] == selected_genre_id]
selected_tracks = selected_tracks.nlargest(10, "popularity")

fig = px.bar(selected_tracks, x = "popularity", y = "title", orientation = "h", color = "popularity", labels = {"popularity": "Popularity", "title": "Track Title"}, title = f"Top 10 Most Popular Tracks in the {selected_genre} Genre")
fig.update_layout(annotations = [dict(x = popularity, y = title, text = str(popularity), xanchor = "left", showarrow = False) for popularity, title in zip(selected_tracks["popularity"], selected_tracks["title"])])
st.plotly_chart(fig)

################################### Exploring the Top 10 Most Popular Artists by Genre ###################################

################################### Exploring Beloved Albums: A Comparative Analysis of Five Notable Releases in the Year ###################################

###################################  Study of the Top Ten Artists with the Most Evocative Lyrics ###################################

###################################  A Study of Annual Distribution of Artist Activity (Total Album Counts) ###################################

################################### A Study of the Top 10 Explicit Songs ###################################

################################### Close the Database connection ###################################
cursor.close()
my_database.close()