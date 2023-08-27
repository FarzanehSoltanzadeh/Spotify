#  Analyzing Spotify Data: A Comprehensive Data Analysis

Explore the rich tapestry of music through our in-depth analysis of Spotify data, unveiling hidden insights and trends at the intersection of data science and music appreciation.
## PHASE ONE: **Data Collection and Preparation**

In our initial phase, we kickstarted our analysis with the [dataset](https://www.kaggle.com/datasets/nicholaselkan/spotify) sourced from [Kaggle](https://www.kaggle.com/). As our exploration deepened, it became apparent that further data enrichment was necessary. Consequently, we employed the [Spotify](https://open.spotify.com/) library in Python, enabling us to extract comprehensive artist and album information.

The dataset acquired through the utilization of the Spotify library encompasses the following components:
```
Artists Information
├── Name
├── Type
├── Popularity
├── Genres
└── Followers
```
```
Albums Information
├── Name
├── Release Date
├── Total Tracks
├── Popularity
└── Artists
```

To install the [Spotify library](https://developer.spotify.com/), just use this command in your command prompt:
```bash
pip install spotify
```

## PHASE TWO: **Data Cleaning and Database Design**

Transitioning to the following phase, we undertook the construction of a database employing the previously gathered data. Our initial step encompassed the creation of an [entity-relationship diagram](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R7V1Zd9o4FP41nJM%2B0OMd80iWZjonTdOmnZnOC0fYAtQYi8pyAv31I3nDG%2BBgGxxGeQm6tmTru5%2Burq4W99SrxeqWgOX8E7ah01Mke9VTr3sK%2BzNl9o9L1qFkOFBDwYwgOxTJG8Ej%2Bg0joRRJfWRDL3MjxdihaJkVWth1oUUzMkAIfsneNsVO9qlLMIMFwaMFnKL0b2TTeSg1lcFG%2FgdEs3n8ZNkYhlcWIL45qok3BzZ%2BSYnUm556RTCm4a%2FF6go6HLwYlzDfhy1Xkxcj0KVVMjwC%2Bunv4eivnx%2F%2FfZA%2F4qcvztTqR6U8A8ePKmxh36UEMczDt6brGArvBS0c4LLUpTVHjn0H1tjnj%2FYosJ7i1OUcE%2FQbuxQ47JLMBOwyoZFmdSlzxyPPycRcStiDbWhHmabsepRH1uJ09C5SUCjBT4lKFJ4feuz%2BhxgPKRHdAY%2FGrxLrgF%2B1gTcPnscTwEEzl%2F22WG5IuIBY0fP541%2FmiMLHJbC44IVRnVeDLuIqTpHjXGEHkwAp1QbQnFrJW6auGJYJJ1N2pai9WBWQULhKiSJt3kK8gJSs2S3R1b6uRdSK2pZm6GH6ZcNU2YjumadYOoxkIGocs6TsDX%2FYj4hCr6CTUqBTTzEcGukvaKYxFMYvnzOfAaFOp5JkSmmRMeP%2FkYeVi6s%2FRl9ZRuVdXBJ7sbCw8KZYPCGxJGTw%2BuKv0dc4s%2FSuwOZY4Q6c0oKmXBzQPK3WSOQxDiB3dhfkutZyTOU85ApEzICMogdQvIypCCYJfwmmgKbSjAkxSVO8KrJkZyveT52IKbpUjShaW0RRC0SxAXLWYwbWWJGkgraE7alse3Ro2lqZ7TGViWoYDdkeVcrZnqqUkpW2OKUdZHwk9mdZReNDCaPHGNkpM6Lq1Y1QnUdHBmz8avuXajFxmRNMbEj60fNHAT7kot9Py9%2BFxeTewgYUXlyPvt28K9ZuiT1EEXYvPt5%2FO2%2FTqlZuGa80rYO2moFeaAYhlRe%2BhyxhWA82rNMpNKxSp84eDCeS1JJhNdSKhFKMthhlHNGwFi1ozt49wXVkdcLLzGq4pZav%2BOS9WQJC9L2QEdxWLgncVhJYcLq4E295WHp7bcPX2ylesHH2xeXnz3c3o%2FvOIVGrZg72bRd63sWHu8%2Bj02u5Vl0oXCzxOVTE9gng3f144Ym2R9ECjj3WsQDqE9hJPOopG7gWBBPkILpukbysP6T9sNPltXNx1AHXg4o7tA5YehvMPEie22kVW8TQhWQmkDtA7C0hZE5oh8x%2Fow0LsHGdx8YvXa3cUa0ocpkb7S8gHzB0WOFHxcRBz9DpEv1r1YYNFyDrSZKqnHGQQK88yntlkCCZBmt8TDfYEiVA7hSLIMHhQQLTguVBgompa3pTQQIlGyPQlZPzyWx05qdmjKDKo7eFJxhjkUdfG%2Fjdam4Pj7%2FusbbNhJpn0CWQVzYaxmztzxqtmudP8g%2FO1Qk4E39xePR9iZe%2BA0i7I5juORAUUQemIJMl6Y3V%2FHXjh87VqYt1qMUouFo6yEK01WBj868NPCueOJPfyCuHXZ7rLyaQnP%2B02qCyy%2FNKj1lubRZkWPBwgj5MOMs1ZtSmypYZNWNi6A0tVdCzvnLiAp9skVT8Ag35yns8qS0%2BU5jLBYu0v6Cft9EZVqZOV5ZJycX1mbHvLOzOwXYHyrYOB2V2Z2gMVNDUEinFzFkeo4RO5lEtj9Ko5dk2jNs7PEsy5uyPeuYGSG5koWYZZdqzQMXFH6Gn6qyJWE5UwwhNJKhCo8wISdCUTLMZIyTLWRtklng%2FyXrbzPI0vTVGFUPPdSJYNddpuuMXTOxuLGuoNX701v7vOaRjF5NFJ2pz0kjYhNn%2B7kBRL5YxRa7bnbqcVK0usbqDRBPN9Rwmenlb64RCTkrNoJkKGFgLFSAAd5YEcf%2FXMLABFlqC1E6R%2FzEaNvJmvkcFEFMIutE4atXiJxb7EC49EC7Wf4tA1Ku4T5YEed1c%2Fn3cNQdEGDVeDJyxfu5ZECLaGyqQiNzAcLzajWFeZ7xBAUrWKRR4pHxDAcbGxRRYZD1NgUfOARWApP1QgUbOHRWA5LxSAUjBOVUEHCXeqUCll3VPBSC9lH8q0OhtHFQBRi%2FroQpAejkXVSDSS%2FuoAo5ezkkViPRyXqpAJM2RCZ6Nf57BvGGi4g5V6KQavgRr%2BDZnEBuF4T4meohHVw93OzImPiXAEZBsxA%2Bx%2BThDTE63cfrNqD9Z1zx2w7ZxXgyoD0sy%2B7zB5Zw3FBmVN4Rs31BUvv9DamD%2Fxz2kV9fPiqJBbYGcX8uR%2Fu%2B0L2sFlUB7BuONO5jQOZ5hFzg3G2lq4w%2FHbHPPHeYgB5D9hJSuI30An%2BIsoHCF6D88%2B3s9Sv2ICuO%2Fr1fpxDpO8FO4U5l48kdcHk9ssgWpTT57xD89wpI3Xxl7vuFPwF2HFz4gjlZw29btPR72iQV3qT06bYcCMoN0B9bRwVQc353kINAJnI%2FMazS%2F86d4SFB42o7YRlZnD%2F002CxW2EamGupQtXfxrPo2MlXObiNTh1WPY2jttH%2B5eB5D3Dkcspd1z7FPe%2FfTR%2FnLNrTmS0gdTlS%2BZX%2BKHQe%2FQOKd%2FzkgiUno5Pn6X5bDL8b3%2B7n3XV49mVe39yv9Ov7GzWm6r%2Fh30Hm9V%2BK%2BbE%2F%2F1ZfeS1LSa4V5VWN%2FN8ZSD5Aghhu3U8fp25Ri17brax%2FH79pKSXFanyZDioqcyNFB0feyoWXFl%2Fg0b0DxenesQQ1jYJj71b%2FbGESdTFNkMCqSwewUGYzOkKHquEbJDGykU9sAuar1H3RK74PujGjlqpofqlpa9Vmr0CmPIB57dJcUpWPvpH4dYEVle6CpwzQr5PeSPjw1KcqjSEVOlN%2BndooUxfO8gpNuC0wRAZDK5%2BgAy7TVwjiYXVFUTdMbCoDog2wARB9W%2FNSqrLYVR1UKVKoV%2F9h54PL%2B8EeQvUr0g7UzCDw43vV5QYoZX8fByT7elhhJIYhyHkGSnUaj8RiJ2RY31e50fRUdolMOh3c17%2BOPgIKsrG5gnbphiZFLvVTJD1ywsY9G7pTVgaanSVS4X1Xr3W%2FIUo6k4RtvKJtU%2FXAWFz8oG0V5xQGcNSctgD0A5V%2FJ0BiTtGb67PykxVFP%2Ft01HdfQyXeVpyyqHdJ5xh2oVpk6Jzj4t%2FSNh6IDrR02GFbsQU8WNnj%2BNbslQ391%2F%2Bctmhs%2FvgPH6Ze69TuowGBhPvDX4NWwm6ZDvt2lFb0N%2ByyFNnGBrG73qvaA8PThei5R8y4jsFfN6TZftjImEb7Ooyq4NHLOZdLy3nhY8yjXDt8of8K9mi8ohKZQUFNuUsmp0lHXJGIb9fwkW7IgVMr8JN3Q5QFsKLaRO6dckyrGNlrzk%2BKg3bEdpVd%2BdeqMPaakTb8dl0k%2Bqc902MIMPumiZjtXTTL3ek4nmYWp2s%2FG1OlIxH2P%2F9QpV7qt2fSqSyvi5cStq44lCeY2euOHsL5w%2FgnbkN%2FxHw%3D%3D) to strategically guide our progress. 

After carefully refining and optimizing the data, we harnessed the power of the SQLAlchemy library in Python. This process led to the meticulous development of our database infrastructure, ensuring efficiency and precision throughout.

To install the [SQLAlchemy library](https://www.sqlalchemy.org/), just use this command in your command prompt:
```bash
pip install SQLAlchemy
```

## PHASE THREE: **Statistical Analysis**


In the third phase of our project, we conducted a comprehensive statistical analysis on the Spotify dataset that had been curated and refined throughout the preceding phases. 

This analytical stage was aimed at extracting meaningful insights and enhancing our understanding of the dataset. This analytical phase served as a pivotal step in unearthing intricate patterns and correlations within the dataset, fostering a more profound comprehension of the dynamics underpinning the realm of music on the Spotify platform. 

The following inquiries were systematically examined:

- Investigation of the Top Five Albums of Each Artist Based on Popularity
- Examination of Popular Literary Genres: Patterns and Influences
- A Comparative Study of the Top 10 Chart-Topping Songs across Distinct Musical Categories
- Exploration of the Top 10 Most Popular Artists Segregated by Genre
- Comparative Analysis of Noteworthy Album Releases: Unveiling Distinctive Attributes of Five Select Albums from the Current Year
- Scrutiny of the Ten Most Profoundly Expressive Lyricists in the Artistic Domain
- Profiling the Annual Distribution of Artist Activity through the Aggregation of Total Song Counts
- Delving into Musical Trends: An Appraisal of the Leading 10 Songs' Popularity, Both Explicit and Implicit in Content

Employing Streamlit and Plotly frameworks, we developed a user-friendly web application to visually present our data insights. To install the [Streamlit library](https://streamlit.io/) and [Plotly library](https://plotly.com/), just use these command in your command prompt:
```bash
pip install streamlit
```
```bash
pip install plotly
```

Through the utilization of the MySQL connector library, we established direct connectivity to the database for efficient data retrieval, ensuring a seamless integration of information. To install the [mysql-connector library](https://dev.mysql.com/doc/connector-python/en/), just use this command in your command prompt:
```bash
pip install mysql-connector-python
```

## Prerequisites:
Prior to engaging with the content and materials presented in this repository, a foundational set of prerequisites should be fulfilled. These prerequisites have been identified to ensure a seamless and productive interaction with the project environment. The following steps are recommended:
1. **Python Installation:** It is imperative to have the [`Python`](https://www.python.org/) programming language installed on your system. The latest version is recommended to leverage the most up-to-date functionalities.

2. **Jupyter Notebook Installation:** To facilitate an interactive and organized computational environment, the utilization of [`Jupyter Notebook`](https://jupyter.org/) is recommended. Alternatively, for users who prefer [`Visual Studio Code`](https://code.visualstudio.com/), the Jupyter Notebook extension can be integrated.

3. **MySQL Installation:** In order to partake in database-related activities, the installation of [`MySQL`](https://www.mysql.com/) is necessary. This will enable efficient management and manipulation of structured data.

4. **Power BI Installation:** For advanced data visualization and exploration, [`Microsoft Power BI Desktop`](https://powerbi.microsoft.com/en-us/downloads/) installation is recommended. This tool will empower users to derive comprehensive insights from complex datasets.

5. **Python Library Installation:** To harness the full spectrum of capabilities offered by the project, ensure the installation of all the Python libraries explicitly mentioned in the project documentation.

*By meticulously fulfilling these prerequisites, users can immerse themselves in the project material with a heightened capacity to comprehend, analyze, and derive value from the presented content.*

## Additional Libraries:

Below, you'll find a list of other libraries that have been employed in this project. To install them, simply copy and execute the commands provided in your command prompt (cmd). This will ensure the proper setup of all required dependencies.
- [time](https://docs.python.org/3/library/time.html)
- [pandas](https://pandas.pydata.org/)
```bash
pip install pandas
```
- [NumPy](https://numpy.org/)
```bash
pip install numpy
```
## Authors

- [Milad Nooraei](https://github.com/MiladNooraei)
- [Farzaneh Soltanzadeh](https://github.com/FarzanehSoltanzadeh)
- [Zahra Honarvar](https://github.com/zahra-honarvar)
- [Ali Mousavi](https://github.com/Alimousavi48)
