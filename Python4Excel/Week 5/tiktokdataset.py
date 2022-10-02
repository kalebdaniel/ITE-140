import pandas as pd

data = pd.read_excel("TikTok_songs_2022.csv")

df = pd.DataFrame(data)
print(df)

print(df.info())

df.index.name = "user_id"

print(df)
print(df.loc[18])

print(df)
