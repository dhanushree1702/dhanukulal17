import numpy as np
import pandas as pd
info=np.array([10,20,30,40])
s=pd.Series(info)
print(s)

a=pd.Series(4,index=[0,1,2,3])
print(a)

i=pd.Index([2,1,1,np.nan,3])
print(i.values_counts())

ser1=pd.series([10,1,3,6])
ser2=pd.series([10,5,6,9])
print(ser1)
print(ser2)

