import pandas as pd

data = [['A', 20], ['B', 29], ['c', 24], ['d', 26]]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=['name', 'age'])
print(df)

