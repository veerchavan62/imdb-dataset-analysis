import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imdb_top_1000.csv")

print(df.head())
print(df.info())
plt.hist(df["IMDB_Rating"], bins=20)
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Movies")
plt.title("Distribution of IMDb Ratings")
plt.show()
df["Runtime"] = df["Runtime"].str.replace(" min", "", regex=False)
df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")
df = df.dropna()
plt.scatter(df["Runtime"], df["IMDB_Rating"], alpha=0.5)
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDb Rating")
plt.title("Runtime vs IMDb Rating")
plt.show()
df = df[["Series_Title", "IMDB_Rating", "Released_Year"]]
df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors="coerce")
df = df.dropna()
top_movies = df.sort_values(
    by="IMDB_Rating",
    ascending=False
)
 