import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/chand/Desktop/titanic.csv",index_col='Name')
print(data)

print(data.shape)
print(data.info())
print(data.head(10))
print(data.head(5))
print(data[['Age','Sex']])
print(data.loc['Allen, Mr. William Henry'])
print(data.loc[data['Age']>50])
print(data.iloc[1:10,1:2])
