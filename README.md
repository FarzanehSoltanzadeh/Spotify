#  Analyzing Spotify Data: A Comprehensive Data Analysis

Explore the rich tapestry of music through our in-depth analysis of Spotify data, unveiling hidden insights and trends at the intersection of data science and music appreciation.
## PHASE ONE

In our initial phase, we kickstarted our analysis with the [dataset](https://www.kaggle.com/datasets/nicholaselkan/spotify) sourced from [Kaggle](https://www.kaggle.com/). As our exploration deepened, it became apparent that further data enrichment was necessary. Consequently, we employed the [Spotify](https://open.spotify.com/) library in Python, enabling us to extract comprehensive artist and album information.

To install the [Spotify library](https://pypi.org/project/spotify/), just use this command in your command prompt:
```bash
pip install spotify
```

## PHASE TWO

Transitioning to the following phase, we undertook the construction of a database employing the previously gathered data. Our initial step encompassed the creation of an [entity-relationship diagram](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R7V1Zd9o4FP41nJM%2B0OMd80iWZjonTdOmnZnOC0fYAtQYi8pyAv31I3nDG%2BBgGxxGeQm6tmTru5%2Burq4W99SrxeqWgOX8E7ah01Mke9VTr3sK%2BzNl9o9L1qFkOFBDwYwgOxTJG8Ej%2Bg0joRRJfWRDL3MjxdihaJkVWth1oUUzMkAIfsneNsVO9qlLMIMFwaMFnKL0b2TTeSg1lcFG%2FgdEs3n8ZNkYhlcWIL45qok3BzZ%2BSYnUm556RTCm4a%2FF6go6HLwYlzDfhy1Xkxcj0KVVMjwC%2Bunv4eivnx%2F%2FfZA%2F4qcvztTqR6U8A8ePKmxh36UEMczDt6brGArvBS0c4LLUpTVHjn0H1tjnj%2FYosJ7i1OUcE%2FQbuxQ47JLMBOwyoZFmdSlzxyPPycRcStiDbWhHmabsepRH1uJ09C5SUCjBT4lKFJ4feuz%2BhxgPKRHdAY%2FGrxLrgF%2B1gTcPnscTwEEzl%2F22WG5IuIBY0fP541%2FmiMLHJbC44IVRnVeDLuIqTpHjXGEHkwAp1QbQnFrJW6auGJYJJ1N2pai9WBWQULhKiSJt3kK8gJSs2S3R1b6uRdSK2pZm6GH6ZcNU2YjumadYOoxkIGocs6TsDX%2FYj4hCr6CTUqBTTzEcGukvaKYxFMYvnzOfAaFOp5JkSmmRMeP%2FkYeVi6s%2FRl9ZRuVdXBJ7sbCw8KZYPCGxJGTw%2BuKv0dc4s%2FSuwOZY4Q6c0oKmXBzQPK3WSOQxDiB3dhfkutZyTOU85ApEzICMogdQvIypCCYJfwmmgKbSjAkxSVO8KrJkZyveT52IKbpUjShaW0RRC0SxAXLWYwbWWJGkgraE7alse3Ro2lqZ7TGViWoYDdkeVcrZnqqUkpW2OKUdZHwk9mdZReNDCaPHGNkpM6Lq1Y1QnUdHBmz8avuXajFxmRNMbEj60fNHAT7kot9Py9%2BFxeTewgYUXlyPvt28K9ZuiT1EEXYvPt5%2FO2%2FTqlZuGa80rYO2moFeaAYhlRe%2BhyxhWA82rNMpNKxSp84eDCeS1JJhNdSKhFKMthhlHNGwFi1ozt49wXVkdcLLzGq4pZav%2BOS9WQJC9L2QEdxWLgncVhJYcLq4E295WHp7bcPX2ylesHH2xeXnz3c3o%2FvOIVGrZg72bRd63sWHu8%2Bj02u5Vl0oXCzxOVTE9gng3f144Ym2R9ECjj3WsQDqE9hJPOopG7gWBBPkILpukbysP6T9sNPltXNx1AHXg4o7tA5YehvMPEie22kVW8TQhWQmkDtA7C0hZE5oh8x%2Fow0LsHGdx8YvXa3cUa0ocpkb7S8gHzB0WOFHxcRBz9DpEv1r1YYNFyDrSZKqnHGQQK88yntlkCCZBmt8TDfYEiVA7hSLIMHhQQLTguVBgompa3pTQQIlGyPQlZPzyWx05qdmjKDKo7eFJxhjkUdfG%2Fjdam4Pj7%2FusbbNhJpn0CWQVzYaxmztzxqtmudP8g%2FO1Qk4E39xePR9iZe%2BA0i7I5juORAUUQemIJMl6Y3V%2FHXjh87VqYt1qMUouFo6yEK01WBj868NPCueOJPfyCuHXZ7rLyaQnP%2B02qCyy%2FNKj1lubRZkWPBwgj5MOMs1ZtSmypYZNWNi6A0tVdCzvnLiAp9skVT8Ag35yns8qS0%2BU5jLBYu0v6Cft9EZVqZOV5ZJycX1mbHvLOzOwXYHyrYOB2V2Z2gMVNDUEinFzFkeo4RO5lEtj9Ko5dk2jNs7PEsy5uyPeuYGSG5koWYZZdqzQMXFH6Gn6qyJWE5UwwhNJKhCo8wISdCUTLMZIyTLWRtklng%2FyXrbzPI0vTVGFUPPdSJYNddpuuMXTOxuLGuoNX701v7vOaRjF5NFJ2pz0kjYhNn%2B7kBRL5YxRa7bnbqcVK0usbqDRBPN9Rwmenlb64RCTkrNoJkKGFgLFSAAd5YEcf%2FXMLABFlqC1E6R%2FzEaNvJmvkcFEFMIutE4atXiJxb7EC49EC7Wf4tA1Ku4T5YEed1c%2Fn3cNQdEGDVeDJyxfu5ZECLaGyqQiNzAcLzajWFeZ7xBAUrWKRR4pHxDAcbGxRRYZD1NgUfOARWApP1QgUbOHRWA5LxSAUjBOVUEHCXeqUCll3VPBSC9lH8q0OhtHFQBRi%2FroQpAejkXVSDSS%2FuoAo5ezkkViPRyXqpAJM2RCZ6Nf57BvGGi4g5V6KQavgRr%2BDZnEBuF4T4meohHVw93OzImPiXAEZBsxA%2Bx%2BThDTE63cfrNqD9Z1zx2w7ZxXgyoD0sy%2B7zB5Zw3FBmVN4Rs31BUvv9DamD%2Fxz2kV9fPiqJBbYGcX8uR%2Fu%2B0L2sFlUB7BuONO5jQOZ5hFzg3G2lq4w%2FHbHPPHeYgB5D9hJSuI30An%2BIsoHCF6D88%2B3s9Sv2ICuO%2Fr1fpxDpO8FO4U5l48kdcHk9ssgWpTT57xD89wpI3Xxl7vuFPwF2HFz4gjlZw29btPR72iQV3qT06bYcCMoN0B9bRwVQc353kINAJnI%2FMazS%2F86d4SFB42o7YRlZnD%2F002CxW2EamGupQtXfxrPo2MlXObiNTh1WPY2jttH%2B5eB5D3Dkcspd1z7FPe%2FfTR%2FnLNrTmS0gdTlS%2BZX%2BKHQe%2FQOKd%2FzkgiUno5Pn6X5bDL8b3%2B7n3XV49mVe39yv9Ov7GzWm6r%2Fh30Hm9V%2BK%2BbE%2F%2F1ZfeS1LSa4V5VWN%2FN8ZSD5Aghhu3U8fp25Ri17brax%2FH79pKSXFanyZDioqcyNFB0feyoWXFl%2Fg0b0DxenesQQ1jYJj71b%2FbGESdTFNkMCqSwewUGYzOkKHquEbJDGykU9sAuar1H3RK74PujGjlqpofqlpa9Vmr0CmPIB57dJcUpWPvpH4dYEVle6CpwzQr5PeSPjw1KcqjSEVOlN%2BndooUxfO8gpNuC0wRAZDK5%2BgAy7TVwjiYXVFUTdMbCoDog2wARB9W%2FNSqrLYVR1UKVKoV%2F9h54PL%2B8EeQvUr0g7UzCDw43vV5QYoZX8fByT7elhhJIYhyHkGSnUaj8RiJ2RY31e50fRUdolMOh3c17%2BOPgIKsrG5gnbphiZFLvVTJD1ywsY9G7pTVgaanSVS4X1Xr3W%2FIUo6k4RtvKJtU%2FXAWFz8oG0V5xQGcNSctgD0A5V%2FJ0BiTtGb67PykxVFP%2Ft01HdfQyXeVpyyqHdJ5xh2oVpk6Jzj4t%2FSNh6IDrR02GFbsQU8WNnj%2BNbslQ391%2F%2Bctmhs%2FvgPH6Ze69TuowGBhPvDX4NWwm6ZDvt2lFb0N%2ByyFNnGBrG73qvaA8PThei5R8y4jsFfN6TZftjImEb7Ooyq4NHLOZdLy3nhY8yjXDt8of8K9mi8ohKZQUFNuUsmp0lHXJGIb9fwkW7IgVMr8JN3Q5QFsKLaRO6dckyrGNlrzk%2BKg3bEdpVd%2BdeqMPaakTb8dl0k%2Bqc902MIMPumiZjtXTTL3ek4nmYWp2s%2FG1OlIxH2P%2F9QpV7qt2fSqSyvi5cStq44lCeY2euOHsL5w%2FgnbkN%2FxHw%3D%3D) to strategically guide our progress. 

After carefully refining and optimizing the data, we harnessed the power of the SQLAlchemy library in Python. This process led to the meticulous development of our database infrastructure, ensuring efficiency and precision throughout.

To install the [SQLAlchemy library](https://pypi.org/project/SQLAlchemy/), just use this command in your command prompt:
```bash
pip install SQLAlchemy
```
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

- [Farzaneh Soltanzadeh](https://github.com/FarzanehSoltanzadeh)
- [Milad Nooraei](https://github.com/MiladNooraei)
- [Zahra Honarvar](https://github.com/zahra-honarvar)
- [Ali Mousavi](https://github.com/Alimousavi48)
