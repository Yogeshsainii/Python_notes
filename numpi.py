
# ---------------------------------------------------------------------
# --------------------  NUMPY  ----------------------------------------
#----------------------------------------------------------------------

# What is Numpy ?
# Numpy is the Library of Python where we complete all the calculation 
# related to mathematics.

# Full form of numpy is :- Numerical Python.

# array
# Dimension

# How to install the numpy
# code :- pip install Numpy

# How to import numpy :-
# import numpy


import numpy as np

# x = np.array([[[[12,44,56,78]]]])
# print(x)
# print(type(x))


# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# x = [[1,2,3],[4,5,6],[7,8,9]]
# print(x)


# x = np.array((23,4,56,34))
# print(x)


# x = [12,45,78,89]
# ar = np.array(x)
# print(ar)

#--------------------------------------------------

# x =np.array([12,45.23,78,"SCIENCE",21j])

# print(x)

# print(type(x))     # It shows the data type of variable.

# print(np.ndim(x))  # It shows the number of dimension.

# print(x.shape)     # It shows the shape of array.

# print(x.dtype)     # High complexity of data in array.


# String  : u64
# complex : complex128  
# float   : float64
# int     : int64


#-----------------------------------------------------------

# Two dimension Array (2D Array)
# x = np.array([[12,45,78,89]])
# print(x)
# print("Type :- ",type(x))
# print("Data Type :- ",x.dtype)
# print("Number of dimension :- ",np.ndim(x))
# print("Shape of Array :- ",x.shape)


# Create a three Dimension Array and include all data
# 1. Check the type of variable .
# 2. Check the data type of array .
# 3. Check the length of array.
# 4. Show the number of dimenson.


# x = np.array([[[12,45.23,78,"SCIENCE",21j]]])

# print(x)
# print("Type :- ",type(x))
# print("Data Type :- ",x.dtype)
# print("Number of dimension :- ",np.ndim(x))
# print("Length of Array :- ",len(x))


#-------#--------#---------#-------#------#------#

# Create a matrix of 4 X 4.

# x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# ar = np.array(x)
# print(ar)

# print("Shape of the matrix :- ",ar.shape)
# print("Number of dimension :- ",np.ndim(ar))
# t = ar.shape
# print(f"There are {t[0]} Rows and {t[1]} Columns")


import numpy as np

# x = np.array([12,45,89,56])

# print(x)
# print(x[0])
# print(x[0:3])


# x = np.array([[12,45,56],[98,87,36]])

# print(x)

# Extract:
# 1. 45
# print(x[0][1])
# print(x[0,1])

# # 2. 36
# print(x[1][2])
# print(x[1,2])

# # 3. 87
# print(x[1][1])
# print(x[1,1])

# # 4. 45
# print(x[0][-2])
# print(x[0,-2])

# # 5. 12
# print(x[0][0])
# print(x[0,0])

# # 6. 98
# print(x[1][0])
# print(x[1,0])


# Extract :

# 1. 12,45
# 2. 87,36
# 3. 45,56


# print(x[0,0:2])
# print(x[1,1:])
# print(x[0,1:])



# What is NumPy?
# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra,
# fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an
# open source project and you can use it freely.

# NumPy stands for Numerical Python.


# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, 
# but most of the parts that require
# fast computation are written in C or C++.

# Data Types in NumPy
# NumPy has some extra data types, and refer to data types
# with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters
# used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
#--------------------------------------------------------------------
#--------------------------------------------------------------------

import numpy as np

# x = np.array([12,45,78,89,56])

# print(x)
# print(type(x))
# print(x.dtype)
# print(x.shape)
# print(np.ndim(x))
# print(len(x))


# Indexing & Slicing :


# Extract :

# 78
# print(x[2])

# 56
# print(x[4])

# 12
# print(x[0])



# create 3 dimension array :

# x = np.array([[[12,45,78,56,23]]])
# print(x)

# extract:

# 45

# print(x[0,0,1])

# 23
# print(x[0,0,-1])

# [12,45,78,56,23]
# print(x[0,0])

# [45,78]
# print(x[0,0,1:3])

#----------------------------------------------------------

# x = np.array([[[[12,45,10],[96,63,52],[9,8,7]]]])

# print(x)
# print(np.ndim(x))
# print(x.shape)



# Extract :

# # [12,45,10]
# print(x[0,0,0])


# # [8,7]
# print(x[0,0,-1,-2:])

# # [[12,45,10],[96,63,52]]
# print(x[0,0,0:2])

# # 63
# print(x[0,0,1,1])

# # 10
# print(x[0,0,0,-1])

# # 96
# print(x[0,0,1,0])

# # 45
# print(x[0,0,0,1])


# # [[12,45,10],
# # [96,63,52],
# # [9,8,7]]
# print(x[0,0])


# # [10,45,12]
# print(x[0,0,0,-1::-1])

# # [63,96]
# print(x[0,0,1,-2::-1])

# # [12,10]
# print(x[0,0,0,0::-2])

# # [9,7]
# print(x[0,0,-1,0::2])

# # [7,8]
# print(x[0,0,-1,-1:-3:-1])


#-------#--------#---------#-------#------#------#-------#

# ndmin = minimum number of dimension .

# x = np.array([12,45,78,89],ndmin=5)
# # print(x)


# # replace all values:

# # 1. 45 to 100
# x[0,0,0,0,1] = 100 
# print(x)

# # 2. 89 to 200
# x[0,0,0,0,-1] = 200
# print(x)

# # 3. 12 to 300
# x[0,0,0,0,0] = 300
# print(x)


#-----------------------------------------------------------------
#-----------------------------------------------------------------


# Array :- It is a container where we store the values in ascending or 
#          descending order.


# Numpy :

# 1 . Arrange 
# 2 . reshape
# 3 . zero
# 4 . one
# 5 . dtype
# 6 . Full
# 7 . sum
# 8 . mean
# 9 . median
# 10. std 
# 11. variance
# 12. concatenate
# 13. transpose or T
# 14. argmin
# 15. argmax
# 16. flatten
# 17. astype
# 18. diagflat
# 19. flip

#-------#--------#--------#-------#-------#-------#-------#

import numpy as np

# x = np.array([12,45,78,56],ndmin = 10)

# print(x)

#-------#--------#--------#-------#-------#-------#-------#
# dtype :- when you use this formula in array it is used to
#          convert the data type in another format.
#-------#--------#--------#-------#-------#-------#-------#


# x = np.array([12,45,78,56],dtype="f") # "float" or "f","int" or "i"
# #                                        ,"str"

# print(x)
# print(x.dtype)
# print(np.ndim(x))

#-------#--------#--------#-------#-------#-------#-------#-------#
# Arange function :- It is used to print the number in sequence 
#                     according to range.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.arange(1,11)
# print(x)

# x = np.arange(1,20)
# print(x)

# x = np.arange(1,20,3)
# print(x)
# print(type(x))
# print(x.dtype)
# print(np.ndim(x))
# print(len(x))
# print(x.shape)


# Creating Dimension with range function :

# x = np.arange(1,11,dtype = "float")
# print(x)

# y = np.array(x,ndmin = 5)
# print(y)


# Print reverse number from 40 to 35 :

# x = np.arange(40,34,-1)
# print(x)

#-------#--------#--------#-------#-------#-------#-------#-------#
# Reshape :- It is used to convert from array to matrix with
#            combination.
#-------#--------#--------#-------#-------#-------#-------#-------#


# x = np.array([1,2,3,4,5,6,7,8,9])
# print(x)

# y = x.reshape(3,3)
# print(y)


# x = np.arange(1,100,4)
# print(x)
# print(len(x))

# y = x.reshape(5,5)
# print(y)


# x = np.arange(8)
# print(x)

# x = np.arange(1,9)
# print(x)

# y = x.reshape(2,2,2)
# print(y)
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = int(input("Enter the number :- "))
# c = 0
# for i in range(x+1):
# 	for j in range(x+1):
# 		if i*j== x:
# 			c+=1
# 			print(f"{i} X {j} = {i*j}")
# print("Total number of combination :- ",c)


#-------#--------#--------#-------#-------#-------#-------#-------#
# Concatenate :- It is used to join the array.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([12,34,5,7])
# y = np.arange(10,15)

# print(x)
# print(y)

# z = np.concatenate((x,y))
# print(z)

#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.arange(1,10)
# y = np.arange(10,20)

# x = np.array([[1,2,3],[4,5,6]])

# print(x)
# print("+"*20)
# print(x.transpose())


# x = np.array([np.arange(1,10)])
# print(x.transpose())

#-------#--------#--------#-------#-------#-------#-------#-------#
#--------------   ZEROS & ONES & FULL   --------------------------#
#-------#--------#--------#-------#-------#-------#-------#-------#

import numpy as np

# x = np.arange(10,20)
# print(x)

# x = np.zeros((4,5))
# print(x)

# x = np.zeros((3,5,5))
# print(x)

#-------------------------------
# x = np.ones((4,5),dtype="str")
# print(x)

#----------------------------------
# x = np.full((4,5),10)
# print(x)


#-------#--------#--------#-------#-------#-------#-------#-------#
# Random.randint() :- It is used to generate the random number 
#                     according to user.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.random.randint(1,10,5)
# print(x)

# x = np.random.randint(-200,-100,10)
# # print(type(x))
# x = set(x)
# print(x)


#-------#--------#--------#-------#-------#-------#-------#-------#
# linspace :- It is used to generate the number in sequence in 
#             same distance according to user.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.linspace(1,10,10)
# print(x)

# x = np.linspace(1,2,100)
# print(x)



#-------#--------#--------#-------#-------#-------#-------#-------#
# Flattten :- It is used to reduce the dimension of array.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([[12,45,78,89],[10,20,30,40],[96,74,85,23]])
# print(x)

# x = x.flatten()
# print(x)


#-------#--------#--------#-------#-------#-------#-------#-------#
# Diagflat :- It is used to convert the matrix in show all values
#             in Diagonal.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([[1,2,3,4],[2,6,7,2]])

# a =  np.diagflat(x)
# print(a)

# b = np.diag(a)
# print(b)

# x = np.arange(1,20)
# y = np.diagflat(x)
# print(y)

#-------#--------#--------#-------#-------#-------#-------#-------#
# Flip :- It is used to reverse the array.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x =  np.array([[12,45,78,56]])
# print(x)


# print(np.fliplr(x))
# print(np.flip(x))
# print(np.sort(x))

#-------#--------#--------#-------#-------#-------#-------#-------#

# Mean     :- Sum of all number divided by total number.
# median   :- It shows the mid value.
# std      :- It is a square root value of variance
# variance :- It shows the spread between the datapoint to mean value.

#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([12,45,89,56,23,18,40])

# print("Average value :- ",np.mean(x))

# print("Median :- ",np.median(x))

# print("Standard deviation :- ",np.std(x))

# print("Variance :- ",np.var(x))

# print("Sum of total number :- ",np.sum(x))




#-------#--------#--------#-------#-------#-------#-------#-------#
# np.nditer :- With the help of this function we can reduce the 
#              dimension of array and iterate with loop.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([[[[12,45,78],[89,56,78]]]])

# x = x.flatten()

# # for i in x:
# # 	print(i)

# for i in np.nditer(x):
# 	print(i)

#-------#--------#--------#-------#-------#-------#-------#-------#
#-------#--------#--------#-------#-------#-------#-------#-------#

import numpy as np

#-------#--------#--------#-------#-------#-------#-------#-------#
# argmin :- It shows the index number of maximum value.
# argmax :- it shows the index of minimum value.
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([12,45,78,89,56])

# print(np.argmin(x))
# print(np.argmax(x))

# print(np.max(x))
# print(np.min(x))

#-------#--------#--------#-------#-------#-------#-------#-------#
# lcm
# hcf
# filter
#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([48,56,60,80])
# print(np.lcm.reduce(x))

# x = np.array([125,225])
# print(np.gcd.reduce(x))

# x = np.array([15,10,8])
# print(np.prod(x))

# x = np.array([12,45,78,89,56])
# print(np.cumsum(x))


#-------#--------#--------#-------#-------#-------#-------#-------#

# x = np.array([45,78,89,56,23,12,45,78])

# 1. Filter the value whose value is less than 50.

# a = x[x<50]
# print(x<50)
# print(a)



# y = []
# for i in x:
# 	if i < 50:
# 		y.append(i)

# print(np.array(y))

#-------#--------#--------#-------#-------#-------#-------#-------#
# and = &
# or  = |
#-------#--------#--------#-------#-------#-------#-------#-------#


# 2. Filter the number between 50 to 80.

# y = x[(x>=50)&(x<=80)]
# print(y)


# 3. Filter all even number.

# z = x[x%2==0]
# print(z)

# 4. Filter all number which is divisible of 5 or 3.

# k = x[(x%5==0) | (x%3==0)]
# print(k)

































































