import pandas as pd
import numpy as np

dict1 = {"2018-10-28":123,"2018-11-04":123,"2018-11-11":123,"2018-11-18 " :123}
dict2= {"2018-10-28":123,"2018-11-04":np.NaN,"2018-11-11": 123}
df1 = pd.Series(dict1)
df2 = pd.Series(dict2)

df = pd.DataFrame()
df["1"]=df1
df["1"] = df["1"].add(df2, fill_value = 1)

print(df)