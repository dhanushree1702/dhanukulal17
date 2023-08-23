import pandas as pd
import numpy as np

dict={'First score':[10,20,np.nan,30],
      'Second score':[np.nan,10,20,30],
      'Third score':[np.nan,20,30,np.nan]}
data=pd.Dataframe(dict)
print(data)

print(data.isnull())
print(data.notnull())

print(data.fillna(20))
print(data.fillna(method='pad'))
print(data.fillna(method='bill'))
print(data.replace(to_replace=np.nan,value=-99))
