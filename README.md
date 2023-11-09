#  Analyzing Spotify Data: A Comprehensive Data Analysis

Explore the rich tapestry of music through our in-depth analysis of Spotify data, unveiling hidden insights and trends at the intersection of data science and music appreciation.
## PHASE ONE: **Data Collection and Preparation**

In our initial phase, we kickstarted our analysis with the [dataset](https://www.kaggle.com/datasets/nicholaselkan/spotify) sourced from [Kaggle](https://www.kaggle.com/). As our exploration deepened, it became apparent that further data enrichment was necessary. Consequently, we employed the [Spotify](https://open.spotify.com/) library in Python, enabling us to extract comprehensive artist and album information.

*Please note that our dataset exclusively comprises the top 200 songs from each day from 2017 to 2020, across 35 different countries. All the data analyses and insights we present are rooted in this comprehensive dataset, offering a thorough examination of music trends and patterns during that specific year and across diverse geographical regions.*

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

Transitioning to the following phase, we undertook the construction of a database employing the previously gathered data. Our initial step encompassed the creation of an [entity-relationship diagram](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R7V1bd9q6Ev41rJU%2BpMt3zCO5NLtnpekl7d6n%2B4UlbAFqjEVlOYH%2B%2BiPZsvENcLABh6O8BI0l2%2Frm02g0urinX8%2BXdwQsZp%2BwC72eprjLnn7T0zTNtnT2j0tWsUTVLS2WTAlyhWwteER%2FoBAqQhoiFwa5jBRjj6JFXuhg34cOzckAIfgln22CvfxTF2AKS4JHB3hl6T%2FIpbNYamv9tfwviKaz5MmqNYivzEGSWdQkmAEXv2RE%2Bm1PvyYY0%2FjXfHkNPY5egktc7sOGq%2BmLEejTOgUeAf30z2D496%2BP%2F35RP%2BKnr97EuRR3eQZeKCrs4NCnBDHM47emqwSK4AXNPeCz1JUzQ557D1Y45I8OKHCektTVDBP0B%2FsUeOySygTsMqFCs6aSy%2FHISzIxlxL2YBe6otCEXRdlVCNJi3dRopsS%2FJSqROPlYcDyf0nwUFLRPQho8iqJDvhVFwSz6Hk8ATw09dlvh5WGhAuII57PH%2F8yQxQ%2BLoDDBS%2BM67wadJ5UcYI87xp7mERI6S6A9sRJ3zJzxXJsOJ6wK2XtJaqAhMJlRiS0eQfxHFKyYlnE1UvTENQSjcuwzDj9smaqaok8swxLB0IGROOYpvde84f9EBR6BZ20Ep16muVRob%2BomSZQWL9DznwGhD6ZKIqtZEXWlP9HAdYurv8afmMFtXfJndiLxTeLMyXiMUkkMYNXF38PvyWFlXclNicK9%2BCEljTl44jmWbUKUcA4gPzpfVTqxigwlfOQKxAxAzIUD6B4kVARjFP%2BEkwBzaQZExKSZnhVZsnWVrybOoIpplKPKMahiKKXiOIC5K1GDKyRpiglbUnbU9v2mNB2jSrbY2tj3bJasj2aXbA9dk1KqdqhOGXsZXwU9uc4ZeNDCaPHCLkZM6Kb9Y1Qk0cLAzZ6tf3LtJjknmNMXEguxfOHET7k4vIyK38X36bwFgR6EARw5AIKL26G32%2FflWu5wAGiCPsXHx%2B%2Bn7eJ1Wu3kFea2P6hmoNZag4xpedhgBxpYPc2sJMJtJxK587tD8aK0pKB1ZW8gbX0moTSrEMxyjqigS1b0oLde4IrYXXiy8xq%2BJUWsPzknUUiQlwGMSO4zVwQuOlOYM7p4o%2BDxX7pzbWNX2%2BreM4G3BdXnz%2Ff3w4fOodEo5p5OHR9GAQXH%2B4%2FD0%2Bv5UZ1oXC%2BwOdQETckgHf3o3kg2x5FczgKWMcCaEhgJ%2FFopmzgOxCMkYfo6oDkZf0hvYw7XV47H4sOuBlU3LH1wCJYYxZA8nyYVrFBDH1IphK5PcTBAkLmhHbI%2FLfasAAb3wVs%2FNLVyh3ViiKfudHhHPIBQ4cVflRMPPQMvS7Rv1Ft2HABsp4krcoZBwnM2qO8VwYJ0umw1sd0%2FQ1RAuRPsAwS7B8ksB1YHSQY26ZhthUk0PIxAlOrG4Q92AyQ3eoMUMMYQZ1HbwpPMMaigL42ALzR3O4fh91hbdsJOU%2BhTyCvrBjGbOzPWq1aEI6LDy7UCXjjcL5%2FFH6BF6EHyGFHMN1zICiiHszNfypvrOavGz90rk5drEMjRsHlwkMOogcNNrb%2F2nH%2FAQInmUZTz9sB7df2IF7pgKoHWwkwKDkMUZcgfc8GE1QTbcMElTW2zJZWAJh51zMdoZxs7VHyAi25njsckw0uSFzKB%2FNs92uc%2BfKjQW3udGX5kVpe95j4otLw7G14oOqasF9leAZWXweHWnqUTnhn6WQf1fS0u%2B5x07Bo53AnLVgwQNGQ6YwNkNrKAsgqyhzOApUXU8TOqrcicnlOAyM0VqAOrSojpEBbse12jJCq5m2QXeH%2BpOtYc8u9zIMxqhzKbRIRarj%2B0R%2B9YOJ2Y5lAoyFksAr%2FzCAd%2BZjMO1Gbk0aWxsz2dweKZtOwE%2BT73anLSdXqE6c7SLTRXM9h4pS3tU4o5KTUjJqphIG1UAkC8KeQSBiAzwZYaAEyOy%2F%2Bj9FwUTANAyqBmEDQjcbRqBa%2FsFzXfxWAePH7WwSiWcVDsiAo6OZy6uPO4RNp1Pht4JT1c8%2BSEGKvpURCuIHxeLUbw7zOeIMSlLxTKPHI%2BIYSjLWLKbHIe5oSj4IDKgHJ%2BqESjYI7KgEpeKUSkJJzqkk4KrxTiUov755KQHoZ%2F1Si0Vs7qBKMXt5DlYD0Ci6qRKSX9VElHL2CkyoR6RW8VIlIliNjPB39OoN5w1TFHarQSTV8BVbwbc4gtgrDQ0L0GI%2BuHpZ2ZExCSoAnIVmLvyTm4wwxOd1G5Dej%2FnRd88iP28Z5MaA5LOns8xqXc95QZNXeELJ5Q1H1%2Fg%2Blhf0fD5Be3zxrmgGNOfJ%2BL4bmv5NL1SipBLpTmGzcwYTO8BT7wLtdSzMbfzhm6zz3mIMcQfYLUroS%2BgAhxXlA4RLR%2F%2FLi702R%2Biluxn%2FfLLOJVZLgp1tnCvHkz%2BR%2BPLEuFqXW5dwh%2F6QHS95%2BY%2Bz5jj8BfxVf%2BIA4WlG2jdt7AhwSB25Tuzi9hgIyhXQL1uKgJ47vVnIQ6EXOR%2B412t%2F5Uz50Jz69Rm4ja7KJfhJtFittI9MtfaC723hWfxuZrua3kemDuucxHOwUfbV8IEPSOeyzl3XHMUo7N9SL8oUNrWrmQJvK036qN%2B1PsOfhF0iC8z%2BvPrUJnTyw%2Futi8NX68TALfqjLJ%2Fv67mFp3iQfjzlN%2F5X8jnqv91rSme3owC6V94qSdltxWd3a3Y%2Bx1BdIEMONG6rjdG5auW%2Fb9hmN4%2FdtlaQ4rVOTI0VNThTooJk72XBgxVc4NW9A8WZ3rEEDY2DZu9W%2F3RiITqYtMlg1yWB3igxWZ8hQd2Cj5UY2yqltgFrX%2Bvc7pfd%2Bd4a0al3ND3Qjq%2Fq8VeiUR5AMPrpLisrBd1q%2FDrCitj0w9EGWFep7xRycmhTVYaQyJ6rz6Z0iRflAr%2Bjo2BJTZASk9kE6wLFdvTQOZlc03TDMliIgZj8fATEHFd8w7VdFQPRDBVK1EpUaBUC2nmC8O%2F4RFS%2Be51UZ%2FqjzwT6KGWFH0dk%2BwYYgSSmKch5Rkq1Wo1GQpIqd9qHIqXen76vpEZ1yPLytfR9%2FCBQVZXUDq0yGBUY%2BDTJ3%2FsIFawNpFQ5a7RtmlkSl%2FLreLL%2BlKgWSxm%2B8pmxa9f1ZXP5Uq4jzyiM4G05bALcPqr87YTAmGe102sVpi6Me%2FrttQq6ls%2B9qT1rUO6bzjDtQozZ1TnD0b%2BUbD2QH2jhuMKjZg54sbvD8e3pHBuHy4T93aGb9%2FAE877LSr99CBQYL84G%2FRa%2BG%2FSwdiu0uq%2BhN2OcptA4M5HW7U7V7xKf313OFmrcZgZ1qzrb5qrUxqfB1HlXJpVELLpNR9MbjmotSW3yj4iH3evFGMTSlG7XlJlWcKy26JhncaOYnuYoDoVblJ5mWqfZhS8GNwknlhlIR3Diqn5RE7Y7tKL3yO05n7DGlbfrtuEzqSX2m%2FVZm8FkXPd%2B5Goq903M6yTRM3X42oU5HQu47%2FKdOudKHmk6vu7YiWVB8cNWxJMHcRq%2F9ENYXzj5hF%2FIc%2FwM%3D) to strategically guide our progress. 

After carefully refining and optimizing the data, we harnessed the power of the SQLAlchemy library in Python. This process led to the meticulous development of our database infrastructure, ensuring efficiency and precision throughout.

To install the [SQLAlchemy library](https://www.sqlalchemy.org/), just use this command in your command prompt:
```bash
pip install SQLAlchemy
```

## PHASE THREE: **Statistical Analysis**


In the third phase of our project, we conducted a comprehensive statistical analysis on the Spotify dataset that had been curated and refined throughout the preceding phases. 

This analytical stage was aimed at extracting meaningful insights and enhancing our understanding of the dataset. This analytical phase served as a pivotal step in unearthing intricate patterns and correlations within the dataset, fostering a more profound comprehension of the dynamics underpinning the realm of music on the Spotify platform. 

The following inquiries were systematically examined:

- Investigation of the Top 5 Albums of Each Artist Based on Popularity
- Examination of Popular Literary Genres: Patterns and Influences
- Identifying the Top 5 Popular Artists within Each Subgenre
- A Comparative Study of the Top 10 Chart-Topping Songs across Distinct Musical Categories
- Exploration of the Top 10 Most Popular Artists Segregated by Genre
- Comparative Analysis of Noteworthy Album Releases: Unveiling Distinctive Attributes of 5 Select Albums from the Current Year
- Scrutiny of the Ten Most Profoundly Expressive Lyricists in the Artistic Domain
- Profiling the Annual Distribution of Artist Activity through the Aggregation of Total Song Counts
- Delving into Musical Trends: An Appraisal of the Leading 10 Songs' Popularity, Both Explicit and Implicit in Content
- The lyrical themes and content in rap music compared to other music genres
- Exploring the Popularity of Explicit vs. Non-Explicit Songs: A Comparative Analysis
- Examine the relationship between popularity and followers (Hypothesis Testing)
- Factors Influencing Song Popularity (Definition of Criteria)
- Personalized Mood-Based Music Selection

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
[statsmodels](https://www.statsmodels.org/stable/index.html) is a versatile Python library designed for statistical modeling and hypothesis testing. It empowers users to perform a wide range of statistical analyses, including linear and generalized linear regression, time series analysis, nonparametric methods, hypothesis testing, and survival analysis. With tools for modeling and interpreting data, statsmodels is invaluable in fields like statistics, economics, and data science, enabling professionals to estimate model parameters, assess goodness of fit, conduct hypothesis tests, and visualize results. Whether analyzing relationships between variables, conducting hypothesis tests, or working with time series data, statsmodels is a reliable choice for rigorous statistical analysis and inference. To install the [statsmodels library](https://pypi.org/project/statsmodels/), just use this command in your command prompt:
```bash
pip install statsmodels
```

## PHASE FOUR: **Predictive Modeling and Machine Learning**

In this section, we leveraged a variety of machine learning techniques to gain valuable insights from Spotify data. Our approach included both supervised learning, with regression and classification methods, and unsupervised learning, particularly clustering. We employed specific models such as linear regression and random forest for the following key objectives:

- Predicting Artist Popularity through Regression Analysis
- Genre-Based Track Classification Analysis
- Mood-Driven Track Classification through Lyric Analysis
- Track Clustering using K-Means Analysis
- Predicting Track Popularity through Regression Analysis

This comprehensive approach allowed us to extract meaningful information and enhance our understanding of the Spotify dataset.

For our supervised learning tasks, we harnessed the power of the [scikit-learn](https://scikit-learn.org/stable/) library, enabling us to employ linear regression and random forest models for classification. Additionally, our unsupervised learning efforts, particularly K-Means clustering, were made possible through the utilization of the [kmodes](https://pypi.org/project/kmodes/) library. To install these essential libraries, simply execute the following commands in your command prompt:
```bash
pip install scikit-learn
```
```bash
pip install kmodes
```

## PHASE FIVE: **Visualization and Business Insights in Power BI**

In the fifth and final phase, we employed Power BI to craft a comprehensive dashboard. This dashboard served as the culmination of our efforts, providing a visual representation of our findings. Through these visualizations, we aimed to enhance our understanding of the Spotify data and offer a more intuitive and insightful presentation of our results.


![PowerBI](https://github.com/FarzanehSoltanzadeh/Spotify/raw/main/assets/108691050/769ecf9e-0fe3-460b-bdc3-b5db9f66cd63)


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
- [os](https://docs.python.org/3/library/os.html)
- [time](https://docs.python.org/3/library/time.html)
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html)
- [patool](https://pypi.org/project/patool/)
```bash
pip install patool
```
- [pandas](https://pandas.pydata.org/)
```bash
pip install pandas
```
- [NumPy](https://numpy.org/)
```bash
pip install numpy
```
- [Matplotlib](https://matplotlib.org/)
```bash
pip install matplotlib
```
- [seaborn](https://seaborn.pydata.org/)
```bash
pip install seaborn
```
- [SciPy](https://scipy.org/)
```bash
pip install scipy
```
## Authors

- [Milad Nooraei](https://github.com/MiladNooraei)
- [Farzaneh Soltanzadeh](https://github.com/FarzanehSoltanzadeh)
- [Zahra Honarvar](https://github.com/zahra-honarvar)
- [Ali Mousavi](https://github.com/Alimousavi48)
