import pandas as pd

data = {"Sales": [100, 200, 300]}
df = pd.DataFrame(data)

print("Total:", df["Sales"].sum())
print("Average:", df["Sales"].mean())