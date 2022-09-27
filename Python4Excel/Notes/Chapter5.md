import pandas as pd
pd.read_excel("xl/course_participants.xlsx")

data = [["Mark", 55, "Italy", 4.5, "Europe"],
                ["John", 33, "USA", 6.7, "America"],
                ["Tim", 41, "USA", 3.9, "America"],
                ["Jenny", 12, "Germany", 9.0, "Europe"]]
        df = pd.DataFrame(data=data,
                          columns=["name", "age", "country",
                                   "score", "continent"],
                          index=[1001, 1000, 1002, 1003])
        df
df.info(<class 'pandas.core.frame.DataFrame'>
Int64Index: 4 entries, 1001 to 1003
Data columns (total 5 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   name       4 non-null      object
 1   age        4 non-null      int64
 2   country    4 non-null      object
 3   score      4 non-null      float64
 4   continent  4 non-null      object
dtypes: float64(1), int64(1), object(3)
memory usage: 192.0+ bytes)     

