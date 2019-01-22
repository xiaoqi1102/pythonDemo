import numpy as np
array = [1, 2, 3, 9]
testCount = [2, 3]
boolean = np.isin(array, testCount)
reverse = ~np.isin(array, testCount)
mean = np.mean(array)
median = np.median(array)
max = np.max(array)
min = np.min(array)
print(boolean)
print(reverse)
print(np.nan)
print('mean:', mean)
print('median:', median)
print('max:', max)
print('min:', min)