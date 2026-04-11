import pandas as pd

df = pd.DataFrame({"Name": ["A", None, "C"], "Age": [20, None, 30]})
df = df.dropna()
print(df)