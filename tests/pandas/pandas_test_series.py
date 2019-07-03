import pandas as pd

ages = pd.Series([18, 21, 20, 16, 32, 22], name="ages")
print(ages)
ages.index=['a', 'b', 'c', 'd', 'e', 'f']
print(ages)

ages2 = pd.Series([18, 21, 20, 16, 32, 22],
                  index=['a', 'b', 'c', 'd', 'e', 'f'],
                  name="ages2")
print(ages2)

class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
class_name = pd.Series(class_name)
print(class_name,'\n')