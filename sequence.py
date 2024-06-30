


#---------------------|----------|-----------------------------------
#                     |   LIST   |
#---------------------|----------|-----------------------------------

# List :- list are used to store the multiple values in a single
#         variable

# 1. list are written in square bracket.
# 2. list is changeable or mutable.
# 3. list allow duplicate values.
# 4. Here we can enter multiple type of data.
# 5. list are indexed.
# 6. list are ordered.

# x = ["prince",34,55,6j,True,False]

# x =["Yogesh","Ansh","Simran","Vishwas"]

# print(x)
# print(type(x))  #Type
# print(len(x))   #Length of list



# Indexing :-It is used to extract the single text from the list.

# Type of indexing :- 1. Positive  2. Negative

# Slicing :- It is used to extract the range of text from the 
#            list.


# x = ["ansh","simran","vishwas","manjeet","yogesh","anshu","Harmeet"]

#manjeet

# print(x[3])
# print(x[-4])

#ansh

# print(x[0])
# print(x[-7])

#[manjeet,yogesh,anshu]

# print(x[3:6])
# print(x[-4:-1])


# Slicing :

# x = [1,2,3,4,5,6,7,8,9,10]

# print(x[0::2])


# Create a list and insert all name of month .

# x = ["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]

# Delete

# 1. Remove

# print(x)
# x.remove("jan")

# print("="*60)
# print(x)


# 2. pop

# print(x)
# print("===========================================================")

# x.pop()
# x.pop(2)
# print(x)

# 3. clear


# print(x)

# print("=======================================================")

# x.clear()
# print(x)


# 4. del

# del x[0]
# del x
# print(x)

#---------------------------------------------------------------
#---------------------------------------------------------------

# x = ["sun","mon","tue","wed","thu","fri","sat"]

# 1. Delete 3rd index of value .

# x.pop(3)
# print(x)

# 2. Extract["fri","sat"]

# print(x[-2:])

# 3. Extract "sun"

# print(x[0])

# 4. Delete "mon"

# del x[1]
#    or
# x.remove("mon")
# print(x)


# 5. Delete all the value from the list.

# x.clear()
# print(x)

# 6. Delete last value from the list.

# x.pop()
# print(x)


#------------------------------------------------------------

# Adding the values :

# 1. insert :- with the help of this formula we add the values
#              according to index.

# x = ["sun","mon","tue"]

# print(x)
# x.insert(1,"data")
# x.insert(0,"science")
# print(x)



# 2. append :- It is used to add the value end of the list.

# x = ["sun","mon","tue"]

# x.append("wed")
# print(x)
# x.append("thu")
# print(x)





# 3. extend :- It is used to add multiple values in list.

# x = ["sun","mon","tue"]

# x.extend(["wed","thu","fri"])
# print(x)


#------------------------------------------------------------

# x = ["sun","mon","tue"]
# y = ["wed","thu","fri"]

# x.extend(y)
# print(x)


# x = str(x)
# print(x.upper())


# x = [4,5,7,4,4,7,8,6,3,7]

# sort :- it is used to arrange the data in ascending or 
#         descending order.

# Ascending

# x.sort()
# print(x)

# Descending 

# x.sort(reverse=True)
# print(x)



# x = [12,45,78,89,56,10,60]

# 1. extract maximum value from the list.

# x.sort(reverse=True)
# print(x[0])
# x.sort()
# print(x[-1])



# 2. extract minimum value from the list.

# x.sort()
# print(x[0])

# 3. extract 3rd maximum value from the list.

# x.sort()
# print(x[-3])


# 4. extract 2nd minimum value from the list.
# x.sort()
# print(x[1])



# print(min(x))
# print(max(x))


# for finding index no.

# print(x.index(89))


# x = ["sun","mon","tue"]

# y = x.copy()
# x.clear()
# print(y)
# print(x)


# for i in y:
# 	i = i.upper()
# 	x.append(i)

# print(x)
# print(type(x))



# x = [45,78,89,12,45,56,23,10]

# print all the number which is less than 30.

# for i in x:
# 	if i<30:
# 		print(i)



# print all the number which is greater than 40.

# for i in x:
# 	if i>40:
# 		print(i)


# delete all the value that is less than 30:
# for i in x[:]:
# 	if i<30:
# 		x.remove(i)
# print(x)

#     OR

# y = x.copy()
# x.clear()

# for i in y:
# 	if i<30:
# 		continue
# 	else:
# 		x.append(i)
# print(x)





#Create a new blank list and add all the even values in list.


# y = [12,45,56,3,12,3,12,8,12]
# x = []

# for i in y:
# 	if i%2==0:
# 		x.append(i)
# print(x)



# 3. Print all duplicate values.

# y = [12,45,56,3,12,3,12,8,12]

# for i in y:
# 	if y.count(i)>1:
# 		print(i,end=" ")



# 4. Print all unique number.

# y = [12,45,56,3,12,3,12,8,12]

# x = []

# for i in y:
# 	if i not in x:
# 		x.append(i)
# print(x)



# 5. Print Negative and Positive index of all number in list.		

# y = [12,45,56,3,12,3,12,8,12]

# x = len(y)

# for i in range (x):
# 	print(y[i] ,"Negative index : ",i-x,",","Positive index : ",i)



# 6.

# x = ["jan",45,"aug",42.9,"sun",True,21j]

# Write a python query to extract all the values in a new list but 
# exclude text from the list.

# y = []

# for i in x:
# 	if type(i)!=str:
# 		y.append(i)
# print(y)


#     OR


# for i in x:
# 	if type(i)==str:
# 		x.remove(i)

# print(x)



#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Nested list :-

# x = [21,43,[45,67,8,100],200]

# print(x)
# print(type(x))
# print(len(x))

# x = [12,[45,78,89,100,200,456],789]

#extract values

# 12 

# print(x[0])

# 45

# print(x[1][0])

# 200

# print(x[1][-2])

# 789

# print(x[-1])

# 89

# print(x[1][2])

# INDEXING :

# x = [100,200,[300,400,[500,600,700],800,900],1000]


# 800

# print(x[2][-2])


# 600

# print(x[2][2][1])

# 300

# print(x[2][0])


# 200
# print(x[1])

# 1000
# print(x[-1])




# x = [[12,78,[[14,10,11],23,56,[89,96,25]],63,[23,100],123]]
# print(x)

# Extract all Number from the List


# 1.  10

# print(x[0][2][0][1])

# 2.  11

# print(x[0][2][0][2])

# 3.  12

# print(x[0][0])


# 4.  56

# print(x[0][2][2])

# 5.  100

# print(x[0][-2][-1])
# 

# 6.  63

# print(x[0][3])

# 7.  14

# print(x[0][2][0][0])


# 8.  89

# print(x[0][2][-1][0])

# 9.  96

# print(x[0][2][-1][1])

# 10. 78

# print(x[0][1])

# 11. 123

# print(x[0][-1])


# x = [12,45,56,89,12,56,12,10,12]


# Find the index of all 12.
# y = len(x)
# for i in range(y):
# 	if x[i]==12:
# 		print(x[i],"Index : ",i)

# Find the sum of all the number with the help of loop.
# s = 0
# for i in x:
# 	s = s+i

# print("Sum of all the number : ",s)


# x = [1,2,4,1.2,5.9,10.8,"a","b","c",True,21j]

# 3. Count total Numebr of text from the list

# c = 0
# for i in x:
# 	if type(i)==str:
# 		c+=1
# 		print(i)

# print("Total no. of text :",c)


# 4. count all Mumerical Data from the list.

# c = 0

# for i in x:
# 	if type(i)==int or type(i)==float or type(i)==complex:
# 		print(i)
# 		c+=1
# print("Total number of Numerical data : ",c)


# -------------------------------------------------
#            :  TUPLES  :
#------------------------------------------------------------

# Tuples : Tuples are used to store the multiple values in
#          a single variable.


# 1. Tuples are written in round bracket.
# 2. Tuples are unchangeable.
# 3. Tuples allow duplicate values.
# 4. Tuples are ordered.
# 5. Tuples are indexed.
# 6. Tuples allow multiple type of data.


# How to create a blank tuple :

# x = ()
# y = tuple()

# print(x)
# print(y)

# Blank list :

# x = []
# y = list()

# print(x)
# print(y)


# x = ("a","b","c","d","e",1,2,3,4,True,21j)

# print(x)
# print(type(x))
# print(len(x))


# x = list(x)
# print(x)


# x = 120
# y = str(x)

# a,b = y,"10"

# print(a+b)


#----------------------------------------------------------------

# Packing and unpacking:

# Packing a tuple :

# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple.

# Unpacking a tuple :

# When we create a tuple, we normally assign values to multiple
# variable from a tuple,this called unpacking.



# x = ("First","Second","Third")

# a,b,c = x

# print(a)
# print(c)
# print(b)


# x = ("a","b","c","d","e")

# print(x)

# m,*n = x

# print(m)
# print(n)



# x = (45,78,89,56)

# a,*b,c = x

# print(c)



# x = ("sun","mon","tue","wed","thu")

# a,b,*c,d = x

# print(c)
# print(b)



# x = (12,45,78,89,5,23,10,18,45)

# 1. STORE ALL EVEN NUMBER FROM NEW List
# y = []
# print(y)
# for i in x:
# 	if i%2==0:
# 		y.append(i)

# print("Even numbers : ",y)


# 2. STORE ALL ODD NUMBER FROM NEW List

# y = []

# for i in x:
# 	if i%2!=0:
# 		y.append(i)

# print("Odd numbers : ",y)



# x = (23,34,4,45,5,6,56,6,7,6,3,3,23)

# i = x.index(4)

# print(i)

# s = sum(x)
# print("Total sum : ",s)

# m = max(x)
# print("Maximum value : ",m)

# n = min(x)
# print("Minimum value : ",n)


# s = sorted(x)
# print("Sorted :- ",s)


# s = sorted(x,reverse=True)
# print("Sorted :- ",s)


# s =tuple(sorted(x))
# print("Sorted :- ",s)



#    sort and sorted :

# Sort :

# 1. It is used in list only.
# 2. Here i am not taking any variable.

# Sorted :

# 1. Sorted is used in list tuple set dict .
# 2. Here we are taking another variable.


# x = ["Ram","Sita","Krishna"]

# x[0] = "Ramayana"
# print(x)


# x.pop(0)
# x.insert(0,"Rama")

# print(x)



# x = ("Ram","Sita","Hamnuman")

# Sita = Krishna

# x = list(x)
# x[1] = "Krishna"
# print(tuple(x))


# x = list([23,45,23,12,78,10])
# print(x)

# x = (78,89,45,56,78,52,62,10)


# 1. Find the 2nd index of 78.

# a = x.index(78)
# b = x.index(78,a+1)

# print(b)

# y = x.index(78,2)
# print(y)


# 2. Find the sum of last 3 number.
# a = x[-3:]
# b = sum(a)

# print("Sum of last 3 numbers :- ",b)

#     or


# s = sum(x[-3:])
# print(s)


# 3. reverse the tuple.

# y = list(x)
# y.reverse()
# print(tuple(y))

#     or 

# y = list(x)

# print(tuple(x[-1::-1]))


# 4. Create a list with the help of user input.

# x = list()
# y = int(input("Enter the length of the list :- "))

# for i in range(y):
# 	val = int(input("Enter number in list :- "))
# 	x.append(val)

# print("List :",x)


# 5. Create a tuple with the help of user input.

# x = list()
# y = int(input("Enter the length of the tuple :- "))

# for i in range(y):
# 	val = int(input("Enter number in tuple :- "))
# 	x.append(val)

# print("tuple :",tuple(x))



# x = list()
# y = int(input("Enter the length of the list :- "))

# # 1 = Integer
# # 2 = Float
# # 3 = String
# # 4 = Complex


# for a in range(y):
# 	print("1.Integer\n2.Float\n3.String\n4.Complex")
# 	DT = input("Select the data type :- ")
# 	if DT == "1":
# 		z = input("Enter number in list :- ")
# 		z = int(z)
# 		x.append(z)
# 	elif DT == "2":
# 		z = input("Enter number in list :- ")
# 		z = float(z)
# 		x.append(z)
# 	elif DT == "3":
# 		z = input("Enter number in list :- ")
# 		z = str(z)
# 		x.append(z)
# 	elif DT == "4":
# 		z = input("Enter number in list :- ")
# 		z = complex(z)
# 		x.append(z)

# print("List : ",x)


# 1. Write a program with the help of user input to display the last digit of a number

# x =  int(input("enter the number :- "))

# print("Last digit of number "x%10)






# 2. write a program to caluculate the electricity bill
#   if number of unit is less than 200 then 5 rupees per unit 
#   else 10 rupees per unit

# x = float(input("Enter the units : "))

# if x<200:
# 	print("Electricity Bill :- ",x*5)
# else :
# 	print("Electricity Bill :- ",x*10)

# 3. Write a program with the help of use input to check the Number is 
#    divisible of 57 and 9 or Not ?

# x = int(input("Enter the number :- "))

# if x%5 == 0 and x%9==0  and x%7== 0:
# 	print("It is a divisible of 57 and 9 ")
# else:
# 	print("It is not a divisible of 57 and 9")


# 4. print the statement 
# 	HOnesty is the best Policy ---- if strings  is vowel
# 	else print Consonent


# x = input("Enter the alphabet :- ")
# y = ["a","e","i","o","u"]
# if x in y:
# 	print("Honesty is the best policy ")
# else:
# 	print("Consonent")







# 5. write a program with the help of two user input if the sum of two Number
#    is even then print even Number with the value of sum
#    else print number is odd with values.

# x = int(input("Enter the first number : -"))
# y = int(input("Enter the second number :- "))

# if (x+y)%2==0:
# 	print("sum :",x+y)
# 	print("It is even")
# else:
# 	print("Sum :",x+y)
# 	print("It is odd")


# 6. If Number is between the 100 to 200 and 400 to 600 then Print
#    Done else print Not Done

# x = int(input("Enter the number :- "))

# if x >=100 and x<=200 :
# 	print("Done")
# elif x>=400 and x<=600:
# 	print("Done")
# else:
# 	print("Not done")

# 7.  write a program with the help of user input and print the Number
# 	 if Number is divisible of 2,4 and 6 else print Number is not
# 	 divisible of 2,4 and 6


# x = int(input("Enter the number :- "))

# if x %2==0 and x%4==0 and x%6==0:
# 	print("Number is divisible of 2,4 and 6")
# else:
# 	print("Number is not divisible of 2,4 and 6")




# -----------------------------------------------------------------------------------------------------------
# 8. Write a python program to show if length of text is greater than 5 then
#    show the last 2 alphabet
#    else show beginning of 2 alphabet.

# x = str(input("Enter the text :- "))

# if len(x)>5:
# 	print(x[-2:])
# else:
# 	print(x[0:2])
 
# 9. Write a python program to print the number from 1 to 50 
#    who is divisible of 5 and 4.

# for i in range(1,51):
# 	if i%5==0 and i%4==0:
# 		print(i) 



# 10. Write a python program wiht the help of user input to compare three number 
#     and show the largest number .




# Print the total even number between 1  to 15 :

# for i in range(1,16):
# 	if i%2==0:
# 		print(i)

# Count all the odd number 1 to 20:

# c = 0
# for i in range(1,21):
# 	if i%2!=0:
# 		c+=1
# print("Total odd numbers between 1 to 20 : ",c)


# find the average of first 5 number :

# c = 0
# s = 0

# for i in range (1,6):
# 	s  = s + i
# 	c+=1
# print("Sum :-",s)
# print("Average of first 5 numbers :- ",s/c)

#----------------------------------------------------------------------------
#-----------------------------------------------------------------------

# Print the number from 1 to 10 with help of while 
# loop and skip 4,6 and 8.

# x = 0
# while x<10:
# 	x+=1
# 	if x == 4 or x == 6 or x==8:
# 		continue
# 	else:
# 		print(x)

#    OR

# for i in range(1,11):
# 	if i in (4,6,8):
# 		continue
# 	else:
# 		print(i)

#     OR

# x = 0
# while x<10:
# 	x+=1
# 	if x in (4,6,8):
# 		continue
# 	else:
# 		print(x)



# Print the table with the help of user input ?

# for loop:

# x = int(input("Enter the table name :- "))

# for i in range(1,11):
# 	print(f"{x} x {i} = {x*i}") 


# while loop:

# x  = int(input())
# y = 0

# while y<10:
# 	y+=1
# 	print(f"{x} x {y} = {x*y}")


# x ="data310science23"

# 1 . Print all number from text.

# for i in x:
# 	if i.isdigit():
# 		print(i,end="")


# 2. Print all alphabet form the text.

# for i in x:
# 	if i.isalpha():
# 		print(i,end="")


# x = "df34@##sd$%"

# extract all special character from text.

# for i in x:
# 	if i.isalnum():
# 		continue
# 	else:
# 		print(i,end="")

#    OR

# for i in x:
# 	if i.isalpha() or i.isdigit():
# 		continue
# 	else :
# 		print(i,end="")


# x  = [34,5,56,6,7,71,12,45,78]

# 1. replace second value 5 at the place of 100.

# x[1] = 100

# print(x)


# 2. print all even number from the list.

# z = []
# for i in x:
# 	if i%2==0:
# 		z.append(i)
# print(z)


# y = [i for i in x if i%2==0]
# print(y)

# 3. delete the 3rd index of value.

# x.pop(3)
# print(x)

# 4. count all odd number.

# c = 0

# for i in x:
# 	if i%2!=0:
# 		c+=1
# print("total odd number :",c)



# x =(12,45,7,89,65)

# 1. sort in ascending order.

# y = sorted(x)
# print(tuple(y))


# 2. sort in  descending order.

# y = sorted(x,reverse=True)
# print(tuple(y))


# reverse the tuple.
# 
# y = reversed(x)
# print(tuple(y))



# show the index of 7.

# print(x.index(7))



# x ="data science"

# Find the second index of a.

# print (x.find("a",2))

# sci

# print(x[-7:-4])

# ta
# print(x[2:4])

# last three alphabet

# print(x[-3:])


# x = (12,45,78,45,12,45,56,89,45,12)
# y = []

# extract all duplicate values.

# for i in x:
# 	if x.count(i) >=2:
# 		y.append(i)
# print(tuple(y))



# for i in x:
# 	if x.count(i) >=2:
# 		if i in y:
# 			continue
# 		else:
# 			y.append(i)

# print(tuple(y))

# extract unique values.

# for i in x:
# 	if i not in y:
# 		y.append(i)
# print(tuple(y))

# change the data type in string in tuple of all values.

# y = list()

# for i in x:
# 	y.append(str(i))
# print(tuple(y))


# ------------------------------------------------
# ---------------- SET ---------------------------
# ------------------------------------------------

# set :- set are used to store the multiple values in a single
#        variable.
# 1. set are written in curly bracket.
# 2. set are un-ordered.
# 3. set are un-indexed.
# 4. set not allow duplicate values.

# blank set.
# x = set()


# x  ={"data",45,56.25,34j,True}

# print(x)
# print(type(x))
# print(len(x))

# x = {44,44,5,5,5,6,4,55,55}
# print(x)

# x = (2,3,3,44,5,6,6,7,2)
# y = set(x)

# print(tuple(y))


# x = {34,56,76,43,45,34,34}
# print(x)

# un-indexed :
# print(x[0])

# how to add the values in set.

# x = {23,34,45,23}

# print(x)

# add :- with the help of this you can add the value in set.

# x.add(100)
# x.add(41)
# print(x)

#--------------------------------------------------
# how to delete the value from set.

# 1. remove
# 2. pop
# 3. clear
#--------------------------------------------------

# x = {12,45,78,56,12,12,12}
# print(x)

# x.remove(12)
# print(x)


# x.pop()
# print(x)


# x.clear()
# print(x)


# x = {"state","capital","Capital","State"}

# print(x)
# y = list()

# for i in x:
# 	i = i.title() 
# 	y.append(i)
# print(set(y))


# x = {"sunday","MONDAY","WEDNESDAY","friday"}

# delete all capital letter text.

# y = list(x)
# z= list()

# for i in y:
# 	if i.isupper():
# 		continue
# 	else:
# 		z.append(i)
# print(set(z))

#   OR

# y = list(x)
# for i in y:
# 	if i.isupper():
# 		x.remove(i)
# print(x)


# x = {1,2,3}
# y = {4,5,6}

# combine the two sets.
# x = x.union(y)
# print(x)

# OR

# x = list(x)
# y = list(y)
# print(set(x+y))

#   OR

# x.extend(y)

# x= set(x)
# print(x)

#----------------------

# 4. difference()

# x = {1,2,3}
# y = {4,2,1}

# z = y.difference(x)
# print(z)



# add()	                        : Adds an element to the set
# clear()                       :Removes all the elements from the set
# copy()					    :Returns a copy of the set
# difference()				    :Returns a set containing the difference between
#                                two or more sets
# difference_update()		    :Removes the items in this set that are also included 
#                                in another, specified set
# discard()					    :Remove the specified item
# intersection()			    :Returns a set, that is the intersection of two 
#                                other sets
# intersection_update()		    :Removes the items in this set that are not present
#                                in other, specified set(s)
# isdisjoint()				    :Returns whether two sets have a intersection or not
# issubset()					:Returns whether another set contains this set or not
# issuperset()				    :Returns whether this set contains another set or not
# pop()						    :Removes an element from the set
# remove()					    :Removes the specified element
# symmetric_difference()		:Returns a set with the symmetric differences of two sets
# symmetric_difference_update() :inserts the symmetric differences from this set and another
# union()					    :Return a set containing the union of sets
# update()					    :Update the set with the union of this set and others



# difference_update():Removes the items in this set that are also included 
#                     in another, specified set


# x = {1,2,3}
# y = {4,2,1}


# x.difference_update(y)
# print(x)


# discard() :Remove the specified item

# x = {1,2,3}




# intersection() :Returns a set, that is the intersection of two 
#                 other sets
# x = {1,2,3}
# y = {3,2,6}
# z = x.intersection(y)

# print(z)

# intersection_update():Removes the items in this set that are not present
#                       in other, specified set(s)

# x = {3,5,7}
# y = {7,5,2}

# x.intersection_update(y)
# print(x)


# symmetric_difference():Returns a set with the symmetric differences of two sets

# x = {3,5,7}
# y = {7,5,2}

# a = x.symmetric_difference(y)
# print(a)