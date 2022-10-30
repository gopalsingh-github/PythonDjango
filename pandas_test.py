import pandas as pd

d = pd.read_csv("E:\\Book1.csv", na_values=['Null'])
df = pd.DataFrame(d)
print(df)