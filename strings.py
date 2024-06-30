


# Strings :- strings always written in single or double quotation.

# x = "Data science"
# print(type(x))

# x = "1234"
# print(type(x)

# y = int(x)
# print(type(x))



# Indexing and Slicing :-

# Indexing :- It is used to extract the one alphabet from the text.

# Types if indexing :

# 1. Positive indexing
# 2. Negative indexing

# x = "India"

#        0  1  2  3  4 :- Positive indexing
#        I  N  D  I  A
#       -5 -4 -3 -2 -1 :- Negative indexing


# x = "India"
# extract the first and last alphabet from the text:

# print(x[0],x[-1])


#---------------------------------------------------------------------

# 1. 
# x = "Himachal pradesh"

# Extract the second a from the text.
# Extract the last alphabet from the text.
# Extract the i from the text.
# Extract the l from the text.
# Extract c from the text with the help of Negative indexing.
# Extract e from the text.

# With Positive indexing:

# print(x[6])

# print(x[15])

# print(x[1])

# print(x[7])

# print(x[4])

# print(x[13])

# With Negative indexing:
# print("---------------------")

# print(x[-10])

# print(x[-1])

# print(x[-15])

# print(x[-9])

# print(x[-12])

# print(x[-3])

#-------------------------------------------------------------------------

# Slicing :- It is used to extract the text from the sentence.
#                                OR
#            It is used to extract the range of alphabet from the text.


# Extract the first three alphabet from the text :

# x = "Himachal pradesh"

# print(x[0:3])
# print(x[-4:])

# Extract the following:

# 1. Chal
# print(x[4:8])

# 2. ma
# print(x[2:4])

# 3. pradesh
# print(x[-7:])

# 4. mac
# print(x[2:5])

# 5. hi
# print(x[0:2])

# 6. rade
# print(x[-6:-2])

# 7. rad
# print(x[-6:-3])

# 8. al
# print(x[6:8])

#------------------------

# x = "HIMACHAL PRADESH"
# print(x[0::2])

# x[starting point : ending point : step size]

#--------------------------

# x = "programmings"

# # print the alternate text start to end :
# print(x[0::2])

# # pg
# print(x[0:4:3])

# # pri
# print(x[0:9:4])
# print(x[0::4])

# y = "Ramayana"

# # maya
# print(y[2:6])

# # aaaa
# print(y[1::2])

#---------------------------------------------------------

# x = "India"

# print(x[-1::-1]) : reverse the strings

#        0  1  2  3  4 
#        I  N  D  I  A
#       -5 -4 -3 -2 -1 

#---------------------------------------------------------------

# Strings formulas :

# Upper() :- It is used to capitalize the each word from the text.

# x = "data science"
# print(x)
# print("After the update :- ")
# x = x.upper()
# print(x)


# lower() :- It is used to convert the text in small letter

# x = "DATA SCIENCE"
# print(x)
# print("After the update :- ")
# x = x.lower()
# print(x)

# title() :- it converts the first starting of alphabet in capital letter.

# x = "PRINCE SHARMA"
# x = x.title()
# print(x)


# Write a python program to check the place name is Delhi or not.

# x = str(input("Enter place name :- "))
# x = x.upper()
# if x =="DELHI":
# 	print("Yes")

# else:
# 	print("No")

#      OR

# x = str(input("Enter place name :- ")).upper()
# if x =="DELHI":
# 	print("Yes")

# else:
# 	print("No")

#      OR

# x = str(input("Enter place name :- "))

# if x.upper() =="DELHI":
# 	print("Yes")

# else:
# 	print("No")



# x = "arunachal pradesh"

# count() :- It is used to count the alphabet from the text.

# y = x.count("a")
# print("Total number of a :- ",y)


# Count total number of alphabet from the text:

# x = "arunachal pradesh"
# y = len(x)-x.count(" ")
# print(y)

# x = "pyt hon"
# y = len(x)-x.count(" ")
# print(y)

# x = "Python is a programming Language"

# 1. Count total number of "g"

# x = x.count("g")
# print(x)


# 2. Count total number of space and "a"

# x = x.count(" ") + x.count("a")
# print(x)

# 3. Count total number of alphabet but exclude the "a" and "g".

# y = len(x) - (x.count("a") + x.count("g"))
# print(y)


# x = "data science"
# print(x[1],x[3])

# find() :- Its show index number of from the text

# y = x.find("a")
# or
# y = x.index("a")
# print(y)

# Find the second "a" from the text :

# x = "data science"
# y = x.find("a",2)
# print(y)



# x = "DAta Analyst".lower()

# count total no. of "a"

# x = x.lower()
# y = x.count("a")
# print(y)




# print "aaaa" by slicing :

# print(x[1:8:2])

#------------------------------------------------------------------

# x = "Ramayana"

# 1. Show the position of third "a"
# y = x.index("a",)
# print(y)


# 2. Show the position of m with positive and Negative.

# y = x.find("m")
# print(y)

# a = x.index("a")
# b = len(x)
# print(a-b)



# 3. Extract "Rama" with positive and Negative indexing.

# print(x[0:4].upper())
# print(x[-8:-4].upper())


# 4. Extract the "MAYA" with Negative indexing.

# print(x[2:6].upper())
# print(x[-6:-2].upper())

#--------------------------------------------------------------

# replace() :- It is used to replace the text or alphabet old text
#              to new text


# x = "Ramayana"
# y = x.replace("a","*")
# print(y)

# Count the total number of text without "a" with len and replace 
# function.

# y = x.replace("a","")
# z = len(y)
# print(z)

#---------------------------------------------------------------

# startswith and endswith :

# x = "data"
# x = x.upper()
# print(x.startswith("D"))

# print(x.endswith("A"))

#---------------------------------------------------------------

# strip : It is used to delete the extra space from only starting 
#		  of the text and ending of the text.

# x = "    prince   "
# print(len(x))

# print("After the update")
# x = x.strip()
# print(len(x))


# split :It is used to convert the string to list.

# x = "Hi this is prince sharma"
# y = x.split()

# print(y)


# x = "ramayana"
# print(x.split("a"))

#--------------------------------------------------------------

#   isdigit :- 

# x = "345"
# y = x.isdigit()
# print(y)


#   isalpha :-

# x = "datascience1"
# y = x.isalpha()
# print(y)

#   isalnum :-

# x = "dsdj345"
# y = x.isalnum()
# print(y)

#   islower :-

# x = "datascience"
# y = x.islower()
# print(y)

#   isupper :-

# x = "MACHINE LEARNING"
# y = x.isupper()
# print(y)

#   isspace :-

# x = "      "
# y = x.isspace()
# print(y)

#---------------------------------------------------------
# 1.
# Write a python program to check the string is text then print 
# "string contain A to Z"
# If string contain any number then print "mix number and text"
# If string is special charactor then print "special character"
# If string is number then print "string is number"


# x = str(input("Enter any text :- "))

# if x.isalpha():
# 	print("string contain A to Z")
# elif x.isdigit():
# 	print("String is number")
# elif x.isalnum():
# 	print("Mix number and text")
# else:
# 	print("special character")


# 2.
# Write a python program to check
# If text is capital letter then print "yes"
# If text is small letter then print "Not"


# x = str(input("Enter any text :- "))
# if x.isupper():
# 	print("Capital letter")
# elif x.islower():
# 	print("Small letter")
# else:
# 	print("Other text")


# 3.
# If text startswith i then print "Yes"
# else print "No"

# x = str(input("Enter any text :- ")).lower()

# if x.startswith("i"):
# 	print("Yes")
# else:
# 	print("No")

# 4.
# Check the text if string start with "A","I","T" 
# Then print "Yes" else "No"

# x = input("Enter any text :- ").upper()
# if x.startswith("A") or x.startswith("I") or x.startswith("T"):
# 	print("Yes")
# else:
# 	print("No")


# 5.
# Check the string whose name endswith  "E" Or "A"
# Then print "Yes" else "No"

# x = input("Enter any text :- ").upper()
# if x.endswith("E"):
# 	print("Yes")
# elif x.endswith("A"):
# 	print("Yes")
# else:
# 	print("No")

#             OR 

# x = input("Enter any text :- ").upper()
# if x.endswith("E") or x.endswith("A"):
# 	print("Yes")
# else:
# 	print("No")


#----------------------------------------------------------------

# join :- it is used to convert the list into string.

# x = ["welcome","to","python","classes"]
# print(type(x))
# print(x)
# print("After the update")

# y = " ".join(x)

# print(type(y))
# print(y)

#---------------------------------------------------------------

# concatenate :- It is used to join the two or  more than two 
#                strings 

# x = "data"
# y = "science"

# print(x+" "+y)

#----------------------------------------------------------------

# Format :- It is used to assign the values in a particular values.

# x = "Hello World {}"
# print(x)
# print(x.format("welcome"))

# x = "Hii My name is : {}"

# y = input()
# print(x.format(y))


# x = """
# I kindly request your approval for this leave and assure you of my commitment to 
# fulfilling any pending responsibilities. Thank you for your understanding and 
# support during my absence. Please feel free to contact me at {} or {} for any
#  further information.
# Thank you for your attention to this matter.

# Yours sincerely,
# {}
# """


# 1 mobile
# 2 email
# 3 full name

# y = x.format("887747xxxx","yogeshsaini98200@gmail.com","Yogesh saini")

# print(y)

#---------------------------------------------------------------------------------

# 1. 
#  WRITE A PYTHON PROGRAM TO CHECK THE TEXT 
#  IF STRINGS START AND ENDSWITH ("I" AND "A") THEN PRINT YES ELSE PRINT NO

# x = str(input("Enter any text :- ")).upper()

# if x.startswith("I") and x.endswith("A"):
# 	print("Yes")
# else:
# 	print("No")






# 2. 
#   WRITE A PYTHON PROGRAM TO SHOW THE TEXT ACCORDING TO Condition
# 	if length of text is less than 6 then show first 3 alphabet of text
# 	if length of text is between 6 to 12 then show first 5 alphabet of text
# 	else show last three alphabet of text


# x = str(input("Enter any text :- "))
# if len(x)<6:
# 	print(x[0:3])
# elif len(x)<=12:
# 	print(x[0:5])
# else:
# 	print(x[-3:])


# 3.
# Reverse the Strings
# x  = "My Name is Ansh"
	
# 	output :-"Ansh is name my"

# y = x.split()
# y = y[-1::-1]


# y = " ".join(y)

# print(y)





# 4. 
#    Write a python program to check if space is repeated more than 3 time the
#    print the "more than three times"
#  	else print "less than equal to three times" 

# x = "Virat Kohli is the greatest player of all time"
# y = x.count(" ")

# if y > 3:
# 	print("Greater than 3 ")
# else:
# 	print("Less than 3 ")





# 5. 
# Remove the space from the text.
# X = "A P P L E"

# X = X.replace(" ","")
# print(X)




# x = '''Data Analyst is the Person Who Extract the insightsful Information 
#      from the data'''.lower()
# 6. convert into list
# Y = X.split()
# print(Y)



# 7. count total number of a 
# y = x.count("a")
# print(y)



# 8. replace the "" at place of space
# y = x.replace(" ","")
# print(y)



# 9. show position of second a
# y = x.find("a",2)
# print(y)


# 10. Swap the values from upper to lower and lower to upper

# x = "DAta scIENce"

# output :- "daTA SCienCE"

# x= x.swapcase()
# print(x)