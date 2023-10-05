################################### Importing libraries ###################################
import numpy as np
import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.stats.proportion import proportions_ztest

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

################################### Setting the Header ###################################
st.set_page_config(page_title = "Spotify Statistical Analysis",)

################################### Analyzing Top Five Albums of Each Artist Based on Popularity ###################################
def top_five_albums_page():
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

    artist_name_list = ["None"] + artist_name_list

    st.subheader("Top Albums by Artist")

    selected_artist = st.selectbox("Select an artist name:", artist_name_list, index=0)

    if selected_artist != "None":
        merged_df = pd.merge(artist_df, artist_album_df, on = "artist_id")
        final_df = pd.merge(merged_df, album_df, on = "album_id")
        artist_albums = final_df[final_df["artist_name"] == selected_artist]
        top_albums = artist_albums.sort_values(by = "popularity", ascending = False).head(5)
        result_df = top_albums[["album_name", "popularity"]]

        fig = px.bar(top_albums, x = "album_name", y = "popularity", text = "popularity", color = "popularity", title = f"Top Albums by {selected_artist}", labels = {"popularity": "Popularity"}, height = 500,)
        fig.update_traces(texttemplate = "%{text}", textposition = "outside")
        fig.update_layout(xaxis_title = "Album Name", yaxis_title = "Popularity")
        fig.update_xaxes(tickangle = -45)

        st.write(f"You selected: {selected_artist}")
        st.plotly_chart(fig, use_container_width = True)
    else:
        st.write("No artist selected.")

################################### Exploring Popular Literary Genres: Trends and Influences ###################################
def popular_genres_page():
    cursor.execute("select * from genre;")
    genre = cursor.fetchall()
    genre = pd.DataFrame(genre, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from track_info;")
    track_info = cursor.fetchall()
    track_info = pd.DataFrame(track_info, columns = [column[0] for column in cursor.description])

    genre_track = pd.merge(genre,track_info, how = "inner", on = "genre_id")
    genre_track = genre_track[["genre_id", "genres_name", "popularity"]]
    genre_track = genre_track.groupby(by = "genre_id")["popularity"].sum()
    genre_track = pd.merge(genre_track, genre, how = "inner", on = "genre_id")
    genre_track.sort_values(by = "popularity", ascending = False)

    st.subheader("Popular Genres")

    fig = px.bar(genre_track.sort_values(by = "popularity", ascending = False), x = "genres_name", y = "popularity", color = "popularity", color_continuous_scale = "Oranges", labels = {"genres_name": "Genre", "popularity": "Popularity"}, orientation = "v")
    fig.update_layout(width = 1200, height = 800, margin = {"l": 50, "r": 20, "t": 20, "b": 100}) 
    fig.update_traces(texttemplate = "%{y}", textposition = "outside")
    st.plotly_chart(fig)

################################### A Study of the Top 10 Chart-Topping Songs in Different Musical Categories ###################################
def popular_tracks_in_different_genres_page():
    cursor.execute("SELECT * FROM genre")
    genre_data = cursor.fetchall()
    genre_df = pd.DataFrame(genre_data, columns = [column[0] for column in cursor.description])
    genre_df = genre_df[["genre_id", "genres_name"]]
    genre_df = genre_df[:21]
    cursor.execute("SELECT * FROM track_info")
    track_data = cursor.fetchall()
    track_df = pd.DataFrame(track_data, columns = [column[0] for column in cursor.description])
    track_df = track_df[["genre_id", "title", "popularity"]]
    genre_name_list = genre_df["genres_name"].unique().tolist()

    st.subheader("Top 10 Chart-Topping Songs in Different Musical Categories")

    selected_genre = st.selectbox("Select a genre name:", ["None"] + genre_name_list)

    if selected_genre != "None":
        selected_genre_id = genre_df[genre_df["genres_name"] == selected_genre]["genre_id"].values[0]
        selected_tracks = track_df[track_df["genre_id"] == selected_genre_id]
        selected_tracks = selected_tracks.nlargest(10, "popularity")

        fig = px.bar(selected_tracks, x = "popularity", y = "title", orientation = "h", color = "popularity", color_continuous_scale = "Greens", labels = {"popularity": "Popularity", "title": "Track Title"}, title = f"Top 10 Most Popular Tracks in the {selected_genre} Genre",)
        fig.update_layout(annotations = [dict(x = popularity, y = title, text = str(popularity), xanchor = "left", showarrow = False,) for popularity, title in zip(selected_tracks["popularity"], selected_tracks["title"])])
        st.plotly_chart(fig)

################################### Exploring the Top 10 Most Popular Artists by Genre ###################################
def popular_artists_by_genre_page():
    query = """
    SELECT artist_name, popularity, genres_name FROM spotify.artist_genre
    join artist on artist.artist_id = artist_genre.artist_id
    join genre on genre.genre_id = artist_genre.genre_id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    artistGenre_popularityBased = pd.DataFrame(rows, columns = column_names)

    st.subheader("Top 10 Most Popular Artists by Genre")

    genre_selected = st.selectbox("Select genre:", ["None"] + sorted(artistGenre_popularityBased["genres_name"].unique()), key = "k1")

    if genre_selected != "None":
        top_10_artists = artistGenre_popularityBased.query("genres_name == @genre_selected").sort_values(by = ["popularity", "artist_name"], ascending = True)[:10]
        st.write(f"Most popular artists in {genre_selected} genre:")
        st.bar_chart(top_10_artists[["artist_name", "popularity"]].set_index("artist_name"))

################################### Exploring the Top 5 Most Popular Artists by Subgenre ###################################
def popular_artists_by_sub_genre_page():
    query = """
        SELECT artist.artist_name, artist.popularity, track_info.title, subgenre.subgenre_name
        FROM artist JOIN track_info ON track_info.artist_id = artist.artist_id JOIN subgenre ON track_info.subgenre_id = subgenre.subgenre_id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    artist_Subgenre_popularityBased = pd.DataFrame(rows, columns = column_names)

    st.subheader("Top 5 Most Popular Artists by Subgenre")

    unique_subgenres_list = list(artist_Subgenre_popularityBased["subgenre_name"].unique())
    selected_subgenre = st.selectbox("Select a Subgenre", ["None"] + unique_subgenres_list)

    if selected_subgenre != "None":
        filtered_df = artist_Subgenre_popularityBased[artist_Subgenre_popularityBased["subgenre_name"] == selected_subgenre]
        top_artists = filtered_df.sort_values(by = "popularity", ascending = False).head(5)
        custom_color_scale = px.colors.qualitative.Set1
        fig = px.bar(top_artists, x = "artist_name", y = "popularity", title = f"Top 5 Most Popular Artists in {selected_subgenre}", color = "artist_name", color_discrete_sequence = custom_color_scale)
        fig.update_traces(showlegend = False)
        st.plotly_chart(fig)

################################### Exploring Beloved Albums: A Comparative Analysis of Five Notable Releases in the Year ###################################
def top_albums_by_year_page():
    query = """
    SELECT album_name, artists, release_date, popularity FROM spotify.album;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    album_yearBased = pd.DataFrame(rows, columns = column_names)
    album_yearBased["release_date"] = pd.to_datetime(album_yearBased["release_date"], format = "%Y-%m-%d", errors = "coerce")

    st.subheader("Five Popular Albums Based on the Year")

    min_year, max_year = map(int, album_yearBased["release_date"].dt.year.agg(["min", "max"]))

    year_selected = st.slider("Select a range of years:", min_year, max_year, (1990, 2010))
    st.write(f"Most popular albums from **{year_selected[0]}** to **{year_selected[1]}**:")

    top_5_albums = album_yearBased.query("release_date.dt.year >= @year_selected[0] and release_date.dt.year <= @year_selected[1]").sort_values(by = ["popularity", "release_date"], ascending = False)[:5]

    st.dataframe(top_5_albums.set_index("album_name").astype({"release_date": "str"}))

###################################  Study of the Top Ten Artists with the Most Evocative Lyrics ###################################
def artists_with_emotional_lyrics_page():
    cursor.execute("select * from track_lyric;")
    track_lyric = cursor.fetchall()
    track_lyric = pd.DataFrame(track_lyric, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from artist;")
    artist = cursor.fetchall()
    artist = pd.DataFrame(artist, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from track_info;")
    track_info = cursor.fetchall()
    track_info = pd.DataFrame(track_info, columns = [column[0] for column in cursor.description])

    st.subheader("Top Ten Artists with the Most Evocative Lyrics")

    artist_lyric_track = pd.merge(artist, track_info, how = "inner", on = "artist_id")
    artist_lyric_track = pd.merge(artist_lyric_track, track_lyric, how = "inner", on = "track_id")
    artist_lyric_track = artist_lyric_track[["artist_id", "artist_name", "track_id", "anger", "disgust", "fear", "joy", "sadness", "surprise", "trust", "negative", "positive"]]

    x = artist_lyric_track.mask(artist_lyric_track.select_dtypes(include = np.number) <= 0)
    artist_lyric_track.loc[:, "anger":] = x

    artist_lyric_track = artist_lyric_track.groupby(by = "artist_id")[["anger", "disgust", "fear", "joy", "sadness", "surprise", "trust", "negative", "positive"]].sum()

    result = pd.merge(artist_lyric_track, artist, how = "inner", on = "artist_id")
    result = result[["artist_id", "artist_name", "anger", "disgust", "fear", "joy", "sadness", "surprise", "trust", "negative", "positive"]]

    all_options = result.columns.to_list()[2:]
    option = st.selectbox("Select an option:", options = ["None"] + all_options)

    if option != "None":
        result = result.sort_values(by = option, ascending = False).reset_index()

        fig = px.bar(result.loc[:9, ["artist_name", option]], x = "artist_name", y = option, color = "artist_name", labels = {"artist_name": "Artist Name"}, title = f"Top 10 singers based on {option}")
        fig.update_xaxes(tickangle = -45)
        for i, value in enumerate(result[option][:10]):
            fig.add_annotation(x = result["artist_name"][i], y = value, text = str(value), showarrow = False, yshift = 10)
        fig.update_layout(showlegend = False)
        st.plotly_chart(fig, use_container_width = True)

###################################  A Study of Annual Distribution of Artist Activity (Total Songs Counts) ###################################
def artist_activity_through_years_page():
    query = """
        SELECT YEAR(a.release_date) AS year, artist.artist_name, COUNT(DISTINCT ti.title) AS num_songs
        FROM track_info ti
        JOIN album a ON ti.album_id = a.album_id
        JOIN artist ON ti.artist_id = artist.artist_id
        GROUP BY YEAR(a.release_date), artist.artist_name
        ORDER BY YEAR(a.release_date), artist.artist_name;
    """
    with my_database.cursor(dictionary = True) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    df = pd.DataFrame(data)
    st.subheader("Song Activity Distribution")

    selected_artist = st.selectbox("Select Artist:", df["artist_name"].unique())
    filtered_data = df[df["artist_name"] == selected_artist]

    fig = px.bar(filtered_data, x = "year", y = "num_songs", title = f"Song Activity Distribution for {selected_artist}", text = "num_songs",)
    fig.update_traces(texttemplate = "%{text}", textposition = "outside", marker_color = "lightblue")
    line_trace = px.line(filtered_data, x = "year", y = "num_songs").data[0]
    line_trace.line.color = "orange"
    fig.add_trace(line_trace)
    fig.update_layout(xaxis_title = "Year", yaxis_title = "Number of Released Songs", xaxis = dict(tickmode = "linear", tickvals = filtered_data["year"], ticktext = filtered_data["year"]))
    st.plotly_chart(fig, use_container_width = True)

################################### Exploring Music Trends: Top 10 Popular Songs with and without Explicit Content ###################################
def top_ten_explicit_non_explicit_page(): 
    def get_popular_songs(explicit): 
        cursor = my_database.cursor() 
        explicit_value = 1 if explicit else 0 
        query = f""" 
            SELECT ti.track_id, ti.title, ti.popularity, ti.explicit 
            FROM track_info ti 
            WHERE ti.explicit = {explicit_value} 
            ORDER BY ti.popularity DESC 
            LIMIT 10 
        """ 
        cursor.execute(query) 
        songs = cursor.fetchall() 
        cursor.close() 
        return songs 
 
    st.subheader("Top 10 Popular Songs with and without Explicit Content") 
    song_type = st.radio("Select Song Type", ("Explicit Songs", "Non-Explicit Songs")) 
 
    if song_type == "Explicit Songs": 
        songs = get_popular_songs(True) 
        st.subheader("Top 10 Popular Explicit Songs") 
    elif song_type == "Non-Explicit Songs": 
        songs = get_popular_songs(False) 
        st.subheader("Top 10 Popular Non-Explicit Songs") 
 
    song_data = pd.DataFrame(songs, columns = ["Track ID", "Title", "Popularity", "Explicit"]) 
 
    fig = go.Figure(data = [go.Bar(x = song_data["Title"], y = song_data["Popularity"], text = song_data["Popularity"], textposition = "outside", marker = dict(color = px.colors.sequential.Reds, colorscale = "Viridis"),)]) 
    fig.update_layout(xaxis_title = "Title", yaxis_title = "Popularity", title = "Popularity of Songs", xaxis_tickangle = -45, width = 800, height = 600,) 
    st.plotly_chart(fig, use_container_width = True)

################################### The lyrical themes and content in rap music compared to other music genres ###################################
def rap_musics_lyric_page():
    st.subheader("Rap lyrics and their emotional content in comparison to other music genres")

    st.write("It has long been asserted that rap music is more laden with negative emotions than other musical genres.\n\nIn this section, \
             we aim to ascertain whether rap music indeed exhibits higher levels of anger, disgust, fear, sadness, and overall negativity when compared to other genres. \
             \n\n✅ To achieve this objective, it is imperative that we prepare our dataset meticulously. In the subsequent table, we have normalized the columns \
             pertaining to anger, disgust, fear, sadness, and overall negativity, ensuring that they have been scaled between 0 and 10.")
    # Obtaining the necessary data
    sql_query = """
        SELECT DISTINCT track_info.title, genre.genres_name AS genre, track_info.popularity, track_info.explicit,
            track_lyric.anger, track_lyric.disgust, track_lyric.fear, track_lyric.sadness, track_lyric.negative
        FROM track_info
        JOIN genre ON track_info.genre_id = genre.genre_id
        JOIN track_lyric ON track_info.track_id = track_lyric.track_id;
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    selected_df = pd.DataFrame(result, columns = columns)
    # Normalize the columns for anger, disgust, fear, sadness, and negativity, scaling them from 0 to 10
    columns_to_normalize = ["anger", "disgust", "fear", "sadness", "negative"]
    min_values = selected_df[columns_to_normalize].min()
    max_values = selected_df[columns_to_normalize].max()
    df_normalized = ((selected_df[columns_to_normalize] - min_values) / (max_values - min_values)) * 10
    df_normalized = df_normalized.round(2) 
    selected_df[columns_to_normalize] = df_normalized
    selected_df.rename(columns = {"title": "song title"}, inplace = True)
    st.dataframe(selected_df)
    # Comparing
    st.write("In the next phase of our analysis, we will initiate by calculating the average emotion scores for each musical genre. \
             This will be followed by the assessment of the percentage of explicit songs within each genre. \
             Subsequently, we will segregate rap songs from the remaining genres, allowing for a comparative evaluation of emotion scores \
             between rap songs and other genres. Furthermore, we will conduct a comparative analysis of the percentage of explicit songs between rap songs and the other genres. \
             \n\n Rap songs have higher emotion scores than other genres:")
    feeling_df = {
        "Emotion": ["anger", "disgust", "fear", "sadness", "negative"],
        "Status": [False, True, False, False, False]
    }
    st.dataframe(pd.DataFrame(feeling_df))

    st.write("As evident from the table above, rap songs exhibit a pronounced presence of anger, disgust, fear, sadness, \
             and an overall negative emotional tone in their lyrics. However, when specifically examining the emotion of disgust, \
              rap songs stand out as having the highest levels compared to other genres. \
              \n\nFor a more detailed comparison of these emotional attributes between rap and other genres, please refer to the table below:")
    emotion_columns = ["anger", "disgust", "fear", "sadness", "negative"]
    genre_emotion_means = selected_df.groupby("genre")[emotion_columns].mean()
    genre_explicit_percentage = selected_df.groupby("genre")["explicit"].mean() * 100
    rap_emotion_means = genre_emotion_means.loc["rap"]
    other_genre_emotion_means = genre_emotion_means[genre_emotion_means.index != "rap"]
    rap_explicit_percentage = genre_explicit_percentage.loc["rap"]
    other_genre_explicit_percentage = genre_explicit_percentage[genre_explicit_percentage.index != "rap"]
    emotion_comparison_result = pd.DataFrame(rap_emotion_means > other_genre_emotion_means, columns = emotion_columns)
    explicit_comparison_result = pd.DataFrame(rap_explicit_percentage > other_genre_explicit_percentage, columns = ["explicit"])
    st.write("Rap Emotion Comparison with Other Genres Results:")
    st.dataframe(emotion_comparison_result)
    st.write("Rap songs have higher explicit percentage than other genres:")
    st.dataframe(explicit_comparison_result)
    #Conclusion
    st.markdown("<h2 style='color: red;'>Summary:</h2>", unsafe_allow_html = True)
    st.write("In summary, while rap lyrics indeed convey pronounced sentiments of anger, disgust, fear, sadness, and an overall \
             negative emotional tone, they predominantly excel in the aspect of expressing the emotion of disgust, holding the top \
              position in this regard. Furthermore, when considering the explicit content, rap songs also exhibit a noteworthy presence, \
              ranking second in comparison to other genres. \n\nIn a holistic evaluation, it becomes evident that rap songs convey  \
             intense emotions of anger, disgust, fear, sadness, negativity, and explicit content.")

################################### Exploring the Popularity of Explicit vs. Non-Explicit Songs: A Comparative Analysis ###################################
def explicit_non_explicit_comparison_page():
    st.subheader("Are Explicit Songs more popular than Non-explicit songs ⁉")

    st.write("In this section, our objective is to examine the popularity of explicit and non-explicit songs. \
             To achieve this, we employ the Z-test for proportions, a statistical method designed for comparing \
             proportions between two independent groups, in this case, explicit and non-explicit songs. \n\n✅ The Z-test \
             for proportions is particularly suitable when dealing with large sample sizes. It is predicated on the \
             assumption of a normal distribution of proportions, which is generally justifiable when the sample sizes \
             are sufficiently large. \n\n To accomplish this, we utilize data encompassing all songs to discern their categorization as either explicit or non-explicit.")
    sql_query = """
        SELECT DISTINCT track_info.title, track_info.popularity, track_info.explicit FROM track_info
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    selected_df = pd.DataFrame(result, columns = columns)
    selected_df.rename(columns = {"title": "song title"}, inplace = True)
    st.dataframe(selected_df)
    # Z-Test
    selected_df["popularity"] = selected_df["popularity"] / selected_df["popularity"].max()
    explicit_popular = selected_df[selected_df["explicit"] == 1]["popularity"]
    non_explicit_popular = selected_df[selected_df["explicit"] == 0]["popularity"]
    # Perform the two-sample z-test for proportions
    count = [explicit_popular.sum(), non_explicit_popular.sum()]
    nobs = [len(explicit_popular), len(non_explicit_popular)]
    z_score, p_value = proportions_ztest(count, nobs, alternative = "larger")
    # Interpret the results
    if not pd.isnull(p_value):
        if p_value < 0.05:
            st.write("Reject null hypothesis. Explicit songs are more popular than non-explicit songs.")
        else:
            st.write("Fail to reject null hypothesis. There is no significant difference in popularity.")
        st.write("Z-Score:", z_score)
        st.write("P-Value:", p_value)
    else:
        st.write("Error: NaN values encountered in calculations.")

    st.write("As indicated by the preceding results, it is evident that the normalization of popularity values has been appropriately \
             addressed. The displayed z-score and accompanying p-value are now considered valid, with the latter serving as a \
             determinant of the statistical significance regarding the disparity in popularity between explicit and non-explicit songs. \
              \n\nIn this instance, the computed p-value stands at 0.9999, surpassing the conventional significance threshold of 0.05. \
              Consequently, we fail to reject the null hypothesis, signifying that there exists no substantial distinction in \
             terms of popularity between explicit and non-explicit songs. \n\nThe negative z-score, quantified at -5.1873, signifies \
             the direction of this observed dissimilarity. Given its negative orientation, it suggests that, on average, explicit \
              songs within the dataset possess a slightly lower degree of popularity in comparison to their non-explicit counterparts. \
             It is imperative to note, however, that this disparity lacks statistical significance.")
    #Conclusion
    st.markdown("<h2 style='color: red;'>Summary:</h2>", unsafe_allow_html = True)
    st.write("In light of the comprehensive analysis conducted, it is reasonable to conclude that there is insufficient compelling \
             evidence to assert that explicit songs exhibit a higher degree of popularity than non-explicit songs within your dataset. \
             \n\n Therefore, Non-explicit songs may be estimated to be approximately 0.51873% more popular than explicit songs, although this difference is not statistically significant.")

################################### Examine the relationship between popularity and followers (Hypothesis Testing) ###################################
def popularity_followers_page():
    st.subheader("Analyzing the Relation Between Popularity and Followers: A Hypothesis Testing Approach")
    st.write("""
            💢 In this section, we aim to analyze the relationship between an artist's number of followers and their level
            of popularity. We have a hypothesis to investigate whether having more followers necessarily leads to greater 
            popularity for an artist or not.
             """)

    cursor.execute("SELECT * FROM spotify.artist")
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    artist_df = pd.DataFrame(rows, columns = column_names)
    
    st.write("Correlation of popularity and followers:")
    st.dataframe(artist_df[["popularity", "followers"]].corr())
    st.write("""
             Table shows that the correlation between popularity and followers is 0.376, 
             which is close to 0.4. This indicates a weak positive correlation, meaning that as popularity increases, 
             followers also tend to increase slightly, but not very strongly. This suggests that there are other factors 
             that influence the number of followers besides popularity, such as genre, style, or marketing.
             """)

    artist_df["is_popular"] = np.where(artist_df["popularity"] >= 70, True, False)

    # Calculate the mean and standard deviation of followers for each group
    mean_popular = artist_df[artist_df["is_popular"] == True]["followers"].mean()
    std_popular = artist_df[artist_df["is_popular"] == True]["followers"].std()
    mean_non_popular = artist_df[artist_df["is_popular"] == False]["followers"].mean()
    std_non_popular = artist_df[artist_df["is_popular"] == False]["followers"].std()
    st.write(f"Mean followers for popular artists: {mean_popular}")
    st.write(f"Mean followers for non-popular artists: {mean_non_popular}")
    st.write(f"Standard deviation of followers for popular artists: {std_popular}")
    st.write(f"Standard deviation of followers for non-popular artists: {std_non_popular}")

    # Create a scatter plot
    fig = px.scatter(artist_df, x = "popularity", y = "followers", color = "is_popular", color_discrete_sequence = ["blue", "orange"])
    fig.update_layout(title = "Scatter Plot of Popularity vs. Followers")
    st.plotly_chart(fig, use_container_width = True)

    st.markdown("""
        The scatter plot reveals some interesting patterns and insights about the data. Here are some of them:

        •  There is a positive correlation between followers and popularity, meaning that as popularity increases, followers also tend to increase. 
           This makes sense, as more popular artists are likely to have more exposure and fan base. However, the correlation is not very strong, 
           as there is a lot of variation and outliers in the data. The correlation coefficient is 0.376, which is close to 0.4. This indicates a weak positive correlation.
                
        •  There are some outliers on the plot, especially on the upper right corner. These are the artists that have very high values of both followers and popularity, 
           such as Ed Sheeran, Drake, Ariana Grande, and BTS. These are some of the most famous and successful artists in the world, and they have millions of loyal fans and listeners. 
           They are exceptions to the general trend of the data, and they show that popularity and followers are not always proportional or linearly related.

        •  The popular artists have higher values of both followers and popularity than the non-popular artists. 
        """)
    
    st.markdown("<h2 style='color: red;'>Summary:</h2>", unsafe_allow_html = True)
    st.write("""
            In summary, while there is a discernible positive correlation between followers and popularity among artists, 
             the relationship is not uniform, and there are notable exceptions. Popularity can be influenced by various factors 
             beyond just the number of followers, such as the artist's talent, marketing strategies, and external events. Therefore, 
             while having a large following can contribute to an artist's popularity, it is not the sole determinant, and individual 
             circumstances play a crucial role in an artist's success in the music industry.
             """)
 
################################### Factors Influencing Song Popularity (Definition of Criteria) ###################################
def factors_influencing_song_popularity_page():
    st.subheader("Factors Influencing Song Popularity")

    st.write("""
            In this part, our objective is to establish a set of criteria for determining if a song's popularity aligns
              with the values we currently possess. We have identified seven key factors: danceability, loudness, energy, valence,
              tempo, acousticness, and instrumentalness. Our approach involved calculating the average values of these factors for
              the top 300 popular songs, and the results are displayed in the table below. \n\nNow, you can select a song, and if at least 
             four of the mentioned factors exceed the corresponding averages from the table, we can categorize it as a popular song. 
             In this classification, we won't give undue attention to other factors or the song's actual popularity value. Otherwise, 
             it will be considered as not popular.
             """)
    
    # Fetch all unique song titles
    query = """
        SELECT DISTINCT title
        FROM track_info
    """
    with my_database.cursor() as cursor:
        cursor.execute(query)
        all_unique_song_titles = [row[0] for row in cursor.fetchall()]

    st.write("Average Characteristics for the First Hundred Songs:")
    avg_characteristics = {
        "danceability": 0.702783,
        "loudness": -5.65259,
        "energy": 0.662133,
        "valence": 0.527967,
        "tempo": 117.00113,
        "acoustics": 0.197693,
        "instrumentalness": 0.161937
    }
    # Convert the dictionary to a DataFrame
    avg_characteristics_df = pd.DataFrame(list(avg_characteristics.items()), columns = ["Track Feature", "AVG Amount"])
    st.dataframe(avg_characteristics_df)
    # Select a song title
    song_title = st.selectbox("Select a song title:", [None] + all_unique_song_titles)

    if song_title:
        if song_title is None:
            st.write("Please select a song.")
        else:
            # Fetch song features by title
            query = """
                SELECT danceability, loudness, energy, valence,
                    tempo, acoustics, instrumentalness
                FROM track_music
                WHERE track_id = (
                    SELECT track_id FROM track_info WHERE title = %s LIMIT 1
                )
            """
            with my_database.cursor(dictionary = True) as cursor:
                cursor.execute(query, (song_title,))
                song_features = cursor.fetchone()

            if song_features:
                # Check if the song is popular
                num_popular_criteria = 0
                for characteristic, avg_value in avg_characteristics.items():
                    if song_features[characteristic] > avg_value:
                        num_popular_criteria += 1
                threshold = 3
                is_popular = num_popular_criteria >= threshold
                popularity_status = "popular" if is_popular else "not popular"
                st.write(f'🎼 The song "{song_title}" is {popularity_status} based on the defined criteria.')

    st.markdown("<h2 style='color: red;'>Summary:</h2>", unsafe_allow_html = True)
    st.write("""
            To sum up, it's evident that focusing solely on musical factors can yield varying results when determining the popularity 
             of a track. We can assert that other elements, such as the artist's influences, the lyrics, and their associated factors,
              exert significant influence on a track's popularity. Relying solely on track-specific factors and information is 
             insufficient for determining whether a song is popular or not.
             """)

################################### Personalized Mood-Based Music Selection ###################################
def song_suggestions_page():
    st.subheader("Song Recommendations 🎵")
    
    st.write("""
            In this section, you have the option to select from the available moods. Depending on your feelings, we will suggest
              songs along with their Spotify links. You can choose more than one emotion, but please ensure that your selected moods
              are not conflicting, such as both sad and happy.
             """)

    cursor.execute("select * from track_lyric;")
    track_lyric = cursor.fetchall()
    track_lyric = pd.DataFrame(track_lyric, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from track_info;")
    track_info = cursor.fetchall()
    track_info = pd.DataFrame(track_info, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from track_music;")
    track_music = cursor.fetchall()
    track_music = pd.DataFrame(track_music, columns = [column[0] for column in cursor.description])
    cursor.execute("select * from artist;")
    artist = cursor.fetchall()
    artist = pd.DataFrame(artist, columns = [column[0] for column in cursor.description])
    artist.drop(columns = ["popularity"], inplace = True)

    all_df = pd.merge(track_info, track_music, how = "inner", on = "track_id")
    all_df = pd.merge(all_df, track_lyric, how = "inner", on = "track_id")
    all_df = pd.merge(all_df, artist, how = "inner", on = "artist_id")

    selected = st.multiselect("Please select your preferred mood(s):", ["sad", "happy", "relaxing", "energetic", "angry", "dancing"], placeholder = "Choose an option")
    all_df = all_df[["track_id", "title", "artist_id", "artist_name", "popularity", "loudness", "danceability", "energy", "valence", "anger", "joy", "sadness", "negative", "positive"]]
    all_df["loudness"] += np.abs(min(all_df["loudness"]))
    x = all_df.mask(all_df.select_dtypes(include = np.number) < 0)
    all_df.loc[:,"popularity":] = x
    all_df = all_df.sort_values(by = "popularity", ascending = False).reset_index()

    result = pd.DataFrame([])
    if all(mood in selected for mood in ["dancing", "happy", "energetic"]):
        result = all_df.loc[(all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 2) & (all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 2) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 3.5) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 5) & (all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 2)]
    elif all(mood in selected for mood in ["dancing", "happy", "relaxing"]):
        result = all_df.loc[((all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 1.5) & (all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 2) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 3.5) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 5) & (all_df.loudness <= np.median(all_df.loudness)) & all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 1.2)]
    elif all(mood in selected for mood in ["sad", "energetic", "angry"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 4) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 4) & (all_df.anger >= (min(all_df.anger) + max(all_df.anger)) / 4) & (all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 1.2)]
    elif all(mood in selected for mood in ["sad", "relaxing", "angry"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 4) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 4) & (all_df.anger >= (min(all_df.anger) + max(all_df.anger)) / 4) & (all_df.loudness <= 19) & (all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 1.2)]
    elif all(mood in selected for mood in ["sad", "energetic"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 4) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 3) & (all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 1.5)]
    elif all(mood in selected for mood in ["sad", "dancing"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 4) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 3) & (all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 1.2)]
    elif all(mood in selected for mood in ["angry", "energetic"]):
        result = all_df.loc[(all_df.anger >= (min(all_df.anger) + max(all_df.anger)) / 3) & (all_df.loudness >= 20) & (all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 1.5)]
    elif all(mood in selected for mood in ["sad", "relaxing"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 4) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 4) & (all_df.loudness <= 19) & (all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 3)]
    elif all(mood in selected for mood in ["sad", "angry"]):
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 3) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 1.5) & (all_df.anger >= (min(all_df.anger) + max(all_df.anger)) / 1.5)]
    elif all(mood in selected for mood in ["dancing", "happy"]):
        result = all_df.loc[(all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 1.2) & (all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 1.5) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 3.5) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 5)]
    elif all(mood in selected for mood in ["energetic", "happy"]):
        result = all_df.loc[(all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 2) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 3) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 5) & (all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 1.2)]
    elif all(mood in selected for mood in ["relaxing", "happy"]):
        result = all_df.loc[(all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 1.5) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 3) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 5) & (all_df.loudness <= 19) & (all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 2)]
    elif all(mood in selected for mood in ["relaxing", "dancing"]):
        result = all_df.loc[(all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 1.5) & (all_df.loudness < 15) & (all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 4)]
    elif "sad" in selected:
        result = all_df.loc[(all_df.negative >= (min(all_df.negative) + max(all_df.negative)) / 3) & (all_df.sadness >= (min(all_df.sadness) + max(all_df.sadness)) / 2)]
    elif "happy" in selected:
        result = all_df.loc[(all_df.valence >= (min(all_df.valence) + max(all_df.valence)) / 2) & (all_df.joy >= (min(all_df.joy) + max(all_df.joy)) / 2.5) & (all_df.positive >= (min(all_df.positive) + max(all_df.positive)) / 3)]
    elif "relaxing" in selected:
        result = all_df.loc[(all_df.loudness < 15) & (all_df.energy <= (min(all_df.energy) + max(all_df.energy)) / 4)]
    elif "energetic" in selected:
        result = all_df.loc[(all_df.energy >= (min(all_df.energy) + max(all_df.energy)) / 1.2)]
    elif "dancing" in selected:
        result = all_df.loc[(all_df.danceability >= (min(all_df.danceability) + max(all_df.danceability)) / 2)]
    elif "angry" in selected:
        result = all_df.loc[(all_df.anger >= (min(all_df.anger) + max(all_df.anger)) / 3)]
    if all(mood in selected for mood in ["relaxing", "energetic"]) | all(mood in selected for mood in ["angry", "relaxing"]) | all(mood in selected for mood in ["angry", "dancing"]) | all(mood in selected for mood in ["happy", "sad"]) | all(mood in selected for mood in ["happy", "angry"]):
        result = pd.DataFrame([])
        st.write("Your selected moods exhibit a striking contrast!")

    if not result.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.write("Here is a selection of recommended tracks:")
            result = result.sort_values("popularity", ascending = False).drop_duplicates(subset = ["title", "artist_name"]).reset_index(drop = True)
            st.dataframe(result.loc[:10,["title", "popularity", "artist_name"]], width = 500, height = 450)
        with col2:
            st.write("Click on each button to access the Spotify page for the respective track:")
            for i in range(11):
                st.markdown(f'<a href="https://open.spotify.com/track/{result.loc[i, "track_id"]}"><button>{result.loc[i, "title"]}</button></a>', unsafe_allow_html = True)

################################### Create a dictionary to map page names to functions ###################################
pages = {
    "Top 5 Albums of Each Artist": top_five_albums_page,
    "Popular Genres": popular_genres_page,
    "Top 10 Tracks in Various Genres": popular_tracks_in_different_genres_page,
    "Top 10 Artists in Each Genre": popular_artists_by_genre_page,
    "Top 5 Artists in Each Subgenre": popular_artists_by_sub_genre_page,
    "Top 5 Albums Based on the Year": top_albums_by_year_page,
    "Top 10 Artists with Emotional Lyrics": artists_with_emotional_lyrics_page,
    "Artist Activity Through the Years": artist_activity_through_years_page,
    "Top 10 Explicit vs. Clean Songs": top_ten_explicit_non_explicit_page,
    "Rap Music's Lyrical Themes vs. Other Genres": rap_musics_lyric_page,
    "Comparing the Popularity of Explicit and Non-Explicit Songs": explicit_non_explicit_comparison_page,
    "Relationship Between Popularity and Followers": popularity_followers_page,
    "What Drives a Song's Success": factors_influencing_song_popularity_page,
    "Customized Mood-Driven Music Selection": song_suggestions_page
}

################################### Add a sidebar to select the page ###################################
st.sidebar.title("Statistical Analysis on Spotify Data")
selected_page = st.sidebar.radio("Choose a page:", list(pages.keys()))

################################### Run the selected page function ###################################
pages[selected_page]()

################################### Closing the Database connection ###################################
cursor.close()
my_database.close()