import pandas as pd

ages = pd.Series([18, 21, 20, 16, 32, 22], name="ages")
print(ages)
ages.index=['a', 'b', 'c', 'd', 'e', 'f']
print(ages)

ages2 = pd.Series([18, 21, 20, 16, 32, 22],
                  index=['a', 'b', 'c', 'd', 'e', 'f'],
                  name="ages2")
print(ages2)
