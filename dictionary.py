
# LIST :
# 1.  []
# 2.  ALLOW DUPLICATE
# 3.  ORDERED
# 4. changable OR Mutable
# 5. INDEXED
# 6. MULTIPLE DATA TYPE


# TUPLE
# 1. ()
# 2. ALLOW DUPLICATE
# 3. ORDERED
# 4. UNCHANGABLE
# 5. INDEXED
# 6. MULTIPLE DATA TYPE


# SET
# 1. {}
# 2. un-ordered
# 3. Un-indexed
# 4.NOT ALLOW DUPLICATE 
# 5. changable
# 6.MULTIPLE DATA TYPE ALLOW

#-------------------------------------------------------
#----------------------------------------------------


# Dictionary :- It is a collection of non repetitive 
#               values
#               It is always seen in key and values
#               pairs.

# 1. {}
# 2. key:values
# 3. ordered
# 4. unindexed
# 5. not allow duplicate values
# 6. changeable
# 7. store multiple type of data

# How to create a blank dictionary.

# dic  = dict()
# x = {}
# print(type(x))


# dic = {"Name" : "Yogesh saini","Department":"Data Science"}

# print(dic)
# print(type(dic))
# print(len(dic))


# car = {"Brand":"BMW","Model":"Model-20","Year":2021,
#        "Color":"Red","Fuel":"Petrol"}

# print("Total feature of car :- ",len(car))

# show the values according to keys .
# dict.keys

# a = car.keys()
# print(a)

# b = car["Brand"]
# print("Brand name is :- ",b)

# c = car["Fuel"]
# print("Type of fuel is :-",c)



# car = {"Brand":"BMW","Model":"Model-20","Year":2021,
#        "Color":"Red","Fuel":"Petrol"}


# x = str(input("Enter any keys :- ")).title()
# print(car[x])

#--------------------------------------------------------------------

# x = {1:"Simran",2:"Anshu",3:"Vishwas",4:"Ansh",5:"dolly",5:"dolly"}

# print(x)
# print(len(x))
# # print(x[1])


# x = {1:"Simran",2:"Anshu",3:"Vishwas",4:"Ansh",5:"dolly",6:"dolly"}
# print(x)
# print(len(x))

# x = {1:"Simran",2:"Anshu",3:"Vishwas",4:"Ansh",5:"dolly",2:"dolly"}
# print(x)


# Functions.

# 1. keys() :- It is used to shown the keys form the dict.

# x = {1:"Simran",2:"Anshu",3:"Vishwas",4:"Ansh",5:"dolly",6:"dolly"}
# a =  x.keys()
# print(a)
# print(type(a))

# 2. values() :- it is used to show the values from the dictionary.

# b = x.values()
# print(b)
# print(type(b))

# 3. items() :- It is used to show the list of tuple in key and values.

# c = x.items()
# print(c)
# print(type(c))

# 4. get() :- It filter the values according to keys.

# print(x[1])

# d = x.get(5)
# print(d)
# print(type(d))


#------------------------------------------------------------------

# how to add key and values in dictionary.

# x= {"Bihar":"Patna","Uttar Pradesh":"Lucknow","Assam":"Dispur"}
# print(x)
# print("-"*70)

# Add the values :
# Kolkata : "West bengal"
# Delhi : "New Delhi"
# Haryana: "Chandigarh"

# With Function :

# update() :- With the help of this funciton you can add single or
#             multiple key and values in a dictionary.

# x.update({"Haryana":"Chandigarh"})
# print(x)
# print("-"*70)

# y = {"Kolkata":"West Bengal","Delhi":"New Delhi"}
# x.update(y)
# print(x)
# print("-"*70)

# without Function

# x["Kolkata"] = "West Bengal"
# x["Delhi"] = "New Delhi"

# print("After the update")
# print("-"*70)

# print(x)
# print("-"*70)





# x = "python is a programming language"
# y = "Python is an object oriented programming language"

# Extract all uncommon text from the sentences.

# x = x.lower()
# y = y.lower()

# x = x.split()
# y = y.split()

# print(x)
# print(y)
# print("-"*70)

# z = []
# for i in x:
# 	if i not in y:
# 		z.append(i)

# for i in y:
# 	if i not in x:
# 		z.append(i)

# z = " ".join(z)
# print(z)




# x = x.lower()
# y = y.lower()

# x = x.split()
# y = y.split()

# print(x)
# print(y)
# print("-"*70)

# z = []
# for i in x:
# 	if i in y:
# 		z.append(i)

# for i in y:
# 	if i in x:
# 		z.append(i)

# z = " ".join(z)
# print(z)


#--------------------------------------------------------------------
#--------------------------------------------------------------------

# Create a dict base of student and his marks
# add five students.


# x = {"Yogesh":99,"Ansh":68,"Shashank":70,
#      "Dolly":80,"Simran":90}

# 1. Add raman wiht his marks 78

# x.update({"Raman":78})
# print(x)

# 2. Add two students in dict suraj and kishan marks 45 and 56.

# x["Suraj"] = 45
# x["Kishan"] = 56
# print(x)




# show the state and and capital with the help of user input?

# #   state           =  capital
# x={"Andhra Pradesh" : "Amaravati",
# "Arunachal Pradesh" : "Itanagar",
# "Assam" : "Dispur",
# "Bihar" : "Patna",
# "Chhattisgarh" : "Raipur",
# "Goa" :	"Panaji",
# "Gujarat" :	"Gandhinagar",
# "Haryana" :	"Chandigarh",
# "Himachal Pradesh": "Shimla",
# "Jharkhand" : "Ranchi",
# "Karnataka" :	"Bengaluru",
# "Kerala" :	"Thiruvananthapuram",
# "Madhya Pradesh" :	"Bhopal",
# "Maharashtra":	"Mumbai",
# "Manipur":	"Imphal",
# "Meghalaya": "Shillong",
# "Mizoram" :	"Aizawl",
# "Nagaland" : "Kohima",
# "Odisha" :	"Bhubaneswar",
# "Punjab" :	"Chandigarh",
# "Rajasthan" :	"Jaipur",
# "Sikkim" : "Gangtok",
# "Tamil Nadu" :	"Chennai",
# "Telangana" :	"Hyderabad",
# "Tripura" : "Agartala",
# "Uttar Pradesh" :	"Lucknow",
# "Uttarakhand" :	"Dehradun", 
# "West Bengal" :	"Kolkata"}

# y = str(input("enter any state :-")).title()
# print(f"The capital of {y} is :  {x[y]}")

#-----------------------------------------------------------
#-----------------------------------------------------------

# dic = {"A":45,"F":56,"C":39,"E":89,"B":50}
# print(dic)


# 1. popitem = It is used to delete the key and values from the list.
# 2. pop     = It is used to delete the key and values according to keys.
# 3. clear   =
# 4. del     =


# a =dic.popitem()
# print(dic)

# dic.pop("B")
# print(dic)

# dic.clear()
# print(dic)

# del dic["A"]
# print(dic)

# del dic
# print(dic)


# Create a dictionary with the help of user input.
# x = int(input("Enter the length of the dictionary : "))
# a = {}
# for i in range(x):
# 	key = input("Enter the key : ")
# 	val = input("Enter the values : ")
# 	a[key] = val

# print(a)



# x = {'yogesh': '66', 'ansh': '78', 'simran': '67'}
# d = {}
# convert all the values in key and key to values.

# y = x.items()

# for i,j in y:
# 	d[j] = i

# print(x)
# print("-----------After the update--------------")

# print(d)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Sorting :
# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}
# print(x)

# y = sorted(x)

# print(y)

# Sort the dictionary base of keys

# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}

# y = x.items()
# z = sorted(y)
# x = dict(z)
# print(x)



# Sort the dictionary alphabetically(by values)

# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}
# y = x.copy()
# x.clear()
# y  = y.items()

# for i,j in y:
# 	x[j] = i

# print(x)
# x = sorted(x.items())
# x = dict(x)
# print(x)

# Sorting the dictionary by keys.

# y = sorted(x.items(),key = lambda x:x[0])
# y = dict(y)

# print(y)


# sorting the dictionary by values.

# z = sorted(x.items(),key = lambda a:a[1])

# z = dict(z)
# print(z)


# Sort the dictionary base of keys descending order.

# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}

# y = x.items()
# z = sorted(y,reverse=True)
# x = dict(z)
# print(x)


# x = "Programming"

# output = PrOgRaMmInG

# y = len(x)
# for i in range (y) :
# 	if i%2!=0:
# 		print(x[i].lower(),end="")
# 	else:
# 		print(x[i].upper(),end="")


# x = [-1,-2,4,6,12]

# print(min(x))

# y = sorted(x)
# print(x[1])




# x = "Programming"
# output = "P*o*r*m*i*g"

# y = ""

# for i in range(len(x)):
# 	if i%2==0:
# 		y+=x[i]
# 	else:
# 		y+="*"

# print(y)
# print(type(y))


# x  =[2,8,12,6,10]

# y = len(x)
# z = []
# for i in range(y):
# 	if x[i] == x[0]:
# 		z.append(x[-1])
# 	elif x[i] == x[-1]:
# 		z.append(x[0])
# 	else:
# 		z.append(x[i])
# print(z)


# x[0],x[-1] = x[-1],x[0]

# print(x)

#----------------------------------------------------------------------

# x = {1:"A",5:"D",3:"F",2:"G"}

# Sort the values base of keys.

# y = dict(sorted(x.items(),key=lambda a:a[0]))
# print("Sorted by key :- ",y)

# sort the dict base of values.

# y = dict(sorted(x.items(),key = lambda a:a[1]))
# print("Sorted by values :- ",y)



#-----------------------------------------------------------------------
#---------------------Nested dictionary----------------------
#-------------------------------------------------------------------

# Nested Dictionary :- We use dictionary inside another dictionary is
#                      called nested dictionary.



# a = {"Name" : "Rohit","Age":25,"City":"Delhi"}
# b = {"Name" : "Raja","Age":45,"City":"Noida"}
# c = {"Name" : "Ram","Age":21,"City":"Jaipur"}
# d = {"Name" : "Virat","Age":55,"City":"Chennai"}

# x = {1:a,2:b,3:c,4:d}

# print(x)
# print("-"*70)
# print(x.keys())
# print(x.values())
# print(x[1]["Age"])

# 1. Show the values of roll no.3.

# print(x[3].values())

# 2. Show the all keys of roll no.2.

# print(x[2].keys())

# 3. Show the city of virat.

# print(x[4]["City"])


# 4. Show the name of roll no. 1.

# print(x[1]["Name"])

# 5. Show all keys of roll no.4.

# print(x[4].keys())

# 6. Find the age of roll no. 4 with get formula.

# print(x[4].get("Age"))


# add Marks in roll no. 3.

# x[3]["Marks"] = 256

# print(x[3])

# x[2].update({"Marks":367,"State" : "UP"})

# print(x[2])

#-----------------------------------------------------------------

# x = {"Car":{"Brand":["Kia","Honda","BMW"],
# 			"Color":["red","Black","White"],
# 			"Model":["BS6","BS4","BS6"],
# 			"Year":[2015,2018,2016]},
# 	"Bike":{"Brand":["Tvs","Bajaj","Hero"],
# 			"Model":["A150","Pulser150","110"],
# 			"Color":["red","black","white"],
# 			"Year":[2019,2018,2020]}
# }

# print(x)

# a = x["Car"]

# print(a)

# d  =  a["Brand"]

# print(d)

# print(d[-1])

#       OR

# print(x["Car"]["Brand"][-1])


#---------------------------------------------------------

# Add Fuel in bike  = ["Petrol","CNG"]

# x["Bike"]["Fuel"]= ["Petrol","CNG"]

# print(x["Bike"])

# Add color in bike green.

# x["Bike"]["Color"].append("Green")

# print(x["Bike"]["Color"])


# delete The year from car.

# x["Car"].pop("Year")

# print(x["Car"])


#-------------------------------------------------------------
#-------------------------------------------------------------


# dic = {
#       "Prince"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Yogesh"  :{"Eng":83,"Hnd":90,"Mth":69,"Sci":63,"Sst":68},
#       "Shashank":{"Eng":89,"Hnd":69,"Mth":83,"Sci":75,"Sst":87},
#       "Simran"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Vishwas" :{"Eng":76,"Hnd":67,"Mth":89,"Sci":73,"Sst":77},
#       "Ansh"    :{"Eng":83,"Hnd":84,"Mth":75,"Sci":66,"Sst":71},
#       "Dolly"   :{"Eng":81,"Hnd":89,"Mth":74,"Sci":87,"Sst":73},
#       "Manjeet" :{"Eng":78,"Hnd":70,"Mth":69,"Sci":61,"Sst":88},
#       "Kshitij" :{"Eng":84,"Hnd":79,"Mth":75,"Sci":84,"Sst":83},
# 	    "Harsh"   :{"Eng":80,"Hnd":82,"Mth":70,"Sci":62,"Sst":73}
# }

# print(dic)
#---------------------------------------------------------------
#----------------------------------------------------------------

# while True:
# 	result = {
# 	      "Prince"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
# 	      "Yogesh"  :{"Eng":83,"Hnd":90,"Mth":69,"Sci":63,"Sst":68},
# 	      "Shashank":{"Eng":89,"Hnd":69,"Mth":83,"Sci":75,"Sst":87},
# 	      "Simran"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
# 	      "Vishwas" :{"Eng":76,"Hnd":67,"Mth":89,"Sci":73,"Sst":77}
# 	}


# 	print("-"*70)
# 	roll_no = {1:"Prince",2:"Yogesh",3:"Shashank",4:"Simran",5:"Vishwas"}

# 	# print(result)

# 	r = int(input("Enter Roll Number :- "))
# 	if r not in roll_no.keys():
# 		print("Not Found")
		
# 	x = roll_no[r]



# 	y = result[x]

# 	v = sum(y.values())
# 	# print(v)

# 	per = v/5

# 	per = round(per,1)
# 	p = str(per) + "%"

# 	if per>=60:
# 		div  = "First div"
# 	elif per >= 45:
# 		div = "Second div"
# 	elif per >= 33:
# 		div = "Third div"
# 	else:
# 		div = "Fail"

# 	print("Student Name :- ",x)

# 	print("Total marks :- ",500)

# 	print("Obtained marks:- ",v)

# 	print("Percentage of Marks :- ",p)

# 	print("Division :- ",div)
# 	print("-"*70)


# 	var = int(input("Press 1 for Next Student \n Press 0 for exit "))
# 	if var == 1:
# 		continue
# 	else:
# 		break



#------------------------------------------------------------------------
#------------------------------------------------------------------------


#--------FUNCTION----------#

# What is function?
# A function is a back of a code which only runs when it is called .
# You can pass data, Known as parameter, into a function.
# A function can return data as result.


# Creating a FUNCTION 

# There are mainly two Functions :

# 1. User defined function :- the user defined function user 
#                           perform the specific task

# 2. Built in function :- The built in function are those function are
#                         those function that are predefined in python 
#                         ex:- sum min max sorted len type


# def x():
# 	print("Hello World")


# Calling the function :
# x()


# def yogesh(x):
# 	s = 0
# 	for i in x:
# 		s+=i
# 	print("Total sum :- ",s)



# x = [43,54,66,76,5,4,65,56]

# yogesh(x)



# def abc (x,y):
# 	z = x + y
# 	print("Total sum :- ",z)


# calling the function :

# x = 56
# y = 44

# abc(x,y)


# Create a function to find the cube value of any Number
# with the help of user input:


# def cube(x):
# 	print(f"Cube value of {x} is :- {x**3}")


# x = int(input("Enter Any Number :- "))
# cube(x)


# Create a text function to show the last three alphabet
# of any text

# def text(x):
# 	print(x[-3:])

# x= input("Enter the Text :- ")
# text(x)




# create a function to print who is eligible for vote or not.

# def Vote(x):
# 	if x>=18:
# 		print("Eligible for vote")
# 	else:
# 		print("Not eligible for vote")

# x = int(input("Enter the age :- "))
# Vote(x)



# Create a function to calculate the average of any numbers :

# def Average(x):
# 	l = len(x)
# 	s = sum(x)
# 	Avg = s/l
# 	print("Average of numbers :- ",Avg)


# x = [5,4,3,2,1]

# Average(x)


# Create a function to show the first two alphabet and the last
# two alphabet in capital letter and the rest alphabets in small letter


# def  text(x):
# 	y = len(x)
# 	for i in range(y):
# 		if i < 2 or i == (y-2) or i == (y-1):
# 			print(x[i].upper(),end="")
# 		else:
# 			print(x[i].lower(),end="")

# OR Without Loop :

# def text(x):
# 	a = x[0:2].upper()
# 	c = x[-2:].upper()
# 	l = len(x)-4

# 	b = x[2:l+2]
# 	print(type(a+b+c))

# x = input("Enter the text :- ")

# text(x)

#--------------------------------------------------------------
#--------------------------------------------------------------

# Create a function the second highest number from the list.

# def sechigh(x):
# 	x.sort()
# 	print("Second Highest number is :- ",x[-2])

# x = [45,65,43,68,82,22]
# sechigh(x)


# Create a Function to show the index of second 
# repetative alphabet from the string .

# def rep(a,b):
# 	x = a.lower()
# 	f = x.find(b)+1
# 	f2 = x.find(b,f)
# 	print(f2)

# x = "Rameshwaram"
# rep(x,"a")



# By default Parameter :- 

# def st(x,y,z = "Patna"):
# 	print(f"Hello {x} \nMy name is {y} \nI live in {z}")


# x = "Good Morning"
# y = "Yogesh"
# z = "Delhi"
# st(x,y,z)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# Parameter or Arguments ?
# The terms Parameter and Arguments can be used tfor the same thing 
# information that are passed into a function .



# Arbitrary Arguments : *args

# If you do not know how many Arguments that will be passed into your function ,
# add astrick * before the parameter name in the function definition .



# def abc(*x):
# 	print("Welcome to ",x[0])
# 	print("My name is ",x[1])
# 	print("Pyhton cost is ",x[2])


# abc("Python","Yogesh",34556)


# def abx(x,*y):
# 	print(x)
# 	print(y[0])
# 	print(y[1])
# abx("Good Morning ","Welcome","To Python")



# Arbitrary Keyword Arguments : **Kwargs

# If you do not know how many arguments will be passed into your 
# function ,add two astrick ** before the parameter anme in the function definition.

# This way function will receive a dictionary of arguments ,and can 
# access the items accordingly  


# def x(**a):

# 	print("My Name is",a["name"])
# 	print("I study in class",a["Class"])
# 	print("My age is",a["age"],"year")


# Calling the function 

# x(name="Yogesh",age="23",Class="xth")


# 1. create a function to delete the last 3 value from the list.


# def del3(x):
# 	del(x[-3:])
# 	return(x)

# x = [23,45,64,33,223,44]
# print(del3(x))



# OR 

# def last(x):
# 	return x[:-3]

# x = [23,45,64,33,223,44]
# print(last(x))

# 2. Create a function to capitalize each text from the list.

# def caps(x):
# 	y = []
# 	for i in x:
# 		if type(i) == str():
# 			y.append(i.title())
# 		else:
# 			y.append(i)
# 	return(y)


# x = [56,78j,"yogesh","vishwas",45,55,66,"harsh","simran",]
# print(caps(x))



# 3. Create a fucntion to calculate all the arithmatic operation on two number.


# def cal(x,y):
# 	return x+y,x-y,x*y,x/y,x%y,x//y,x**y

# a,b,c,d,e,f,g =  cal(34,9)

# print("Addition :- ",a)
# print("Substraction :- ",b)
# print("Multiplication :- ",c)
# print("Division :- ",d)
# print("Modulus :- ",e)
# print("Floor :- ",f)
# print("Exponentation :- ",g)


#------------------------------------------------------------------------
#-----------------------------------------------------------------------
 
# sum = lambda x,y : x+y

# print(sum(3,4))

#-----------------------------------------------------------
#-----------------------------------------------------------

# Exception Handling :

# When an error occurs ,or exception as we call it ,python will 
# normally stop and generate an error message,these exceptions
# can be handled useing the try statement.

#  Block of Exception Handling:

# 1. try  2. Exception  3.else   4. finally

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code , regardless of the 
# result of try and except block.



# try:
# 	x = int(input("Enter any Number :- "))

# 	if x%2==0:
# 		print("Even Number")
# 	else:
# 		print("Odd Number")

# except:
# 	print("Please Enter Number only")




# Write a python program to show the values base of 
# user input by index.
# Exception :- please enter Number less than the length of text

# try :
# 	x = "Yogesh"
# 	y = int(input("Enter the index :- "))

# 	print(x[y])
# except:
# 	print("Please enter number less than the length of text")


# try :
# 	x = 10
# 	y = 5
# 	print(y/x)
# except ZeroDivisionError:
# 	print("-"*60)
# 	print("ZeroDivisionError :Division by Zero")

# else:
# 	print("-"*60)
# 	print("Code is working properly")

# finally:
# 	print("-"*60)
# 	print("Done")
# 	print("-"*60)



# Write a python program to find the sum of all odd number
# and sum of all even number from 1 to 20 
# in exception handling:

#--------------
# While loop :
#--------------
# try:
# 	x = 0
# 	e = 0
# 	o = 0
# 	while x<20:
# 		x+=1
# 		if x%2==0:
# 			e += x
# 			# print(x)
# 		else:
# 			o+=x
# 			# print(x)
# 	print("-"*60)		
# 	print("Sum of all even Number from 1 to 20:- ",e)
# 	print("-"*60)
# 	print("Sum of all odd number from 1 to 20:- ",o)
# except:
# 	print("-"*60)
# 	print("Error")
# else:
# 	print("-"*60)
# 	print("Code is working properly")
# finally:
# 	print("-"*60)
# 	print("❁´◡`❁🌜🌜Thanks🌛🌛❁´◡`❁")
# 	print("-"*60)

#--------------
# for loop:
#--------------

# try:
# 	e = 0
# 	o = 0
# 	for i in range(1,21):
# 		if i%2==0:
# 			e += i
# 			# print(x)
# 		else:
# 			o+=i
# 			# print(x)
# 	print("-"*60)		
# 	print("Sum of all even Number from 1 to 20:- ",e)
# 	print("-"*60)
# 	print("Sum of all odd number from 1 to 20:- ",o)
# except:
# 	print("-"*60)
# 	print("Error")
# else:
# 	print("-"*60)
# 	print("Code is working properly")
# finally:
# 	print("-"*60)
# 	print("❁´◡`❁🌜🌜Thanks🌛🌛❁´◡`❁")
# 	print("-"*60)



# Create a function to print even number with the help of user input.

# x = int(input("Enter the number :- "))

# for i in range(1,2*x+1):
# 	if i%2==0:
# 		print(i)


# Create a new list show the data type of all value that given in list.

# x = ["ram",45,"mamta",45.4,True,21j]
# y = []
# for i in x:
# 	y.append(type(i))
# print(y)


# print all numerical data from the list.

# x = ["ram",45,"mamta",45.4,True,21j]
# y = []
# for i in x:
# 	if type(i) == str or type(i)== bool:
# 		continue
# 	else:
# 		y.append(i)

# print(y)


# Convert from nested list to simple list.

# x = [[[[12,45,[45,89,[18,21],22],78]]]]	

# # output :- [12,45,45,89,18,21,22,78]

# x = str(x)
# x = x.replace("[","")
# x = x.replace("]","")
# x = x.split(",")
# print(y)

# x = [int(i) for i in x]
# print(x)

#   OR

# y =  []
# for i in x:
# 	y.append(int(i))

# print(y)




























