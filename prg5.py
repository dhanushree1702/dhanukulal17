#Program5
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Sum of the array =",a.sum())
print("Maximum of the array =",a.max())
print("Maximum of the array from each axis =",a.max(axis=1))
print("Minimum of the array from each axis =",a.min(axis=1))
print("Cumilative sum of the array =",a.cumsum())
print("Cumilative sum of the array from each axis =",a.cumsum(axis=1))
print("Average of the array =",a.mean())
