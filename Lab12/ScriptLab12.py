# 1.	Create a new script called Script12Lab.py.
# 2.	Create an array from a range of values from 1 to 20 incrementing by 2
import numpy

NumRange = numpy.array(range(1, 20, 2))
print(NumRange)
# 3.	Print the data type of the array created in #2.
print(NumRange.dtype)
# 4.	Print the size of the array created in #2.
print('Size: ' + str(len(NumRange)))
# 5.	Reshape the array created in #2 to 5 Rows and 2 columns
reshape = NumRange.reshape(5, 2)
print(reshape)
# 6.	Find and print the MAX / MIN / AVG / SUM of each row
rowmax = numpy.max(reshape, axis=0)
print('Row Max')
print(rowmax)

rowmin = numpy.min(reshape, axis=0)
print('Row Min')
print(rowmin)

rowmean = numpy.mean(reshape, axis=0)
print('Row Avg')
print(rowmean)

rowsum = numpy.sum(reshape, axis=0)
print('Row Sum')
print(rowsum)

# 7.	Find and print the MAX / MIN / AVG / SUM of each column
colmax = numpy.max(reshape, axis=1)
print('Col Max')
print(colmax)

colmin = numpy.min(reshape, axis=1)
print('Col Min')
print(rowmin)

colmean = numpy.mean(reshape, axis=1)
print('Col Avg')
print(rowmean)

colsum = numpy.sum(reshape, axis=1)
print('Col Sum')
print(colsum)

# 8.	Create a multi-dimensional array consisting of 2 instances of 4 rows and 4 columns full of 0’s.

twoisntance = numpy.zeros((2,4,4))
print(twoisntance)
# 9.	Create a multi-dimensional array consisting of 4 instances of 5 rows and 3 columns full of random numbers.
fourinstance= numpy.random.random((4,5,3))
print(fourinstance)