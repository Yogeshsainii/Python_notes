


# LOOPS :- It is used to repeat the set of number.
# set iteratition 

# Loops 
# 1. While loop
# 2. for loop


# x = 10 
# y = 0
# while x>y:
# 	print("Hello world!",y)
# 	y+=1




# x = 10
# y = 1

# while x>y:
# 	print(x)
# 	x = x-1




# Print the counting from 1 to 50

# x = 50
# y = 1

# while x>=y:
# 	print(y)
# 	y+=1


# Back counting from 20 to 1:
# x = 20
# y = 1

# while x>=y:
# 	print(x)
# 	x=x-1


# Print the number from 10 to 40 but step size should be 2

# x = 40
# y = 10

# while x>=y:
# 	print(y)
# 	y+=2


# Print the even no. from 1 to 20

# x = 1
# y = 20
# while x<y:
# 	if x%2==0:
# 		print("even number :",x)
# 	x+=1


# x = int(input("Enter any no. :- "))
# y = 1
# while x>=y:
# 	if y%2==0:
# 		print("even number :-",y)
# 	y+=1



# Print the odd no. from 1 to 20:

# x = 20
# y = 1
# while x>=y:
# 	if y%2!=0:
# 		print("Odd number :-",y)
# 	y+=1


# Print the table of 5:

# x = 1
# t = int(input("Enter the table name :- "))
# while x < 11:
# 	print(x*t)	
# 	x+=1


# x = 1
# t = int(input("Enter the table name :- "))

# while x < 11:
# 	print(t,"X",x,"=",x*t)
# 	x+=1



# x = 1
# t = int(input("Enter the table name :- "))

# while x < 11:
# 	print(f"{t} X {x} = {x*t}")
# 	x+=1


#
# Count total number of even number from 1 to 20 :

# x = 1
# c = 0
# y = int(input("Enter the number :- "))
# while x<=y:
# 	x+=1
# 	if x%2==0:
# 		c+=1
# 		print("Even number :-",x)
# print("Total number of even number:- ",c)


#
# Count total number of odd number from 1 to 30 :

# y = int(input("Enter the number :- "))
# x = 0
# c = 0
# while x<=y:
# 	x+=1
# 	if x%2!=0:
# 		c+=1
# 		print("Odd number :-",x)
# print("Total Number of odd number :-",c)



# 
# print the odd number with the help of user input:

# y = int(input("Enter the number :- "))
# x = 0

# while x<y*2:
# 	x+=1
# 	if x%2!=0:
# 		print("Odd number :-",x)

#        # OR

# x = int(input("Enter the number :- "))
# y = 0
# z = 0

# while x > y:
# 	z+=1
# 	if z%2!=0:
# 		print("Odd number :-",z)
# 		y+=1




# statement :
# break
# continue


# x = 10
# y = 1
# while x >= y:
# 	print(y)
# 	if y==5:
# 		break
# 	y=y+1

## OR

# y = 1
# while y<=20:
# 	if y==10:
# 		break
# 	else:
# 		print(y)
# 	y+=1


# continue statement :

# x = 10
# y = 0

# while x>y:
# 	y+=1
# 	if y==5:
# 		continue
# 	else:
# 		print(y)
	
# Print the number from 1 to 15 and skip the number 7 and 10

# x = 0
# y = 15
# while x<y:
# 	x+=1
# 	if x==7 or x==10:
# 		continue
# 	else:
# 		print(x)




# Print the number from 1 to 10 and  break the loop where no. is 6

# x = 0
# y = 10

# while x<y:
# 	x+=1
# 	print(x)
# 	if x == 6:
# 		break

	
# Print the number from 20 to 30 and skip the number 26,28,30

# x = 20
# y = 30

# while x<y:
# 	x+=1
# 	if x==26 or x==28 or x==30:
# 		continue
# 	else:
# 		print(x)

# Print the back counting from 50 to 10 and break the loop where
# number is 20

# x = 50
# y = 10

# while x>y:
# 	x-=1
# 	print(x)
# 	if x==20:
# 		break

#----------------------------------------------------------------------

# Print back counting
# 10 --- 1

# x = 10
# y = 1
# while x>=y:
# 	print(x)
# 	x-=1


# 10 -- 20

# x = 10
# y = 20
# while x<=y:
# 	print(x)
# 	x+=1


# 10 --- 40 
# step size = 3

# x = 40
# y = 10
# while x>=y:
# 	print(y)
# 	y+=3


# Find the sum of first five number:

# x = 0
# s = 0
# while x<=5:
# 	s = s + x
# 	x = x + 1
# print("Total number of sum :-",s)


#
# x = 0
# s = 0
# while x<=10:
# 	s = s + x
# 	x = x + 1
# print("Total number of Sum :",s)


#
# Find the average of first 10 number:

# x = [1,2,3,4,5,6,7,8,9,10]

# a = 1+2+3+4+5+6+7+8+9+10

# avg = a/10

# x = 0
# y = 10
# s = 0
# while x<=y:
# 	s = s + x
# 	x+=1
# print("Average of first 10 number :-",s/y)


#1*2*3*4*5
# x = int(input("Enter the number :- "))
# y = 1
# z = 1
# while x>=y:
# 	z = z*y
# 	y+=1

# print(f"Factorial of {x} is : {z}")


# x = "Himachal Pradesh"

# z = len(x)
# y = 0
# while z>y:
# 	print(x[y],end=" ")
# 	y+=1


#---------------------------------------------------------------------------


# print(x) : It prints vertically.

# print(x,end="") : It prints horizontally.


#------------------------------------------------------------------


# x = 1
# while x<=200:
# 	print(x,end=" ")
# 	x+=1



# 20 times "hello world":

# x = "Hello world"
# y = 1
# z = 20
# while y<=z:
# 	print(x)
# 	z-=1


# x = "dAta SCIence"

# Extract only capital letters:

# y = len(x)
# z = 0
# while y>z:
# 	if x[z].isupper():
# 		print(x[z],end=" ")
# 	z+=1


#--------------------------------------------------------------
#--------------------------------------------------------------

## For loop :-

# Sequence data :- list, tuple, range

#while loop:
# 1 -- 20

# x = 20
# y = 1
# while x>=y:
# 	print(y)
# 	y+=1


# For loop:
# 1 --- 20

# for x in range (1,21):
# 	print(x)


#---------------------------------------------------------

# Print number from 1 to 100 :

# for x in range (1,101):
# 	print(x)


# Print number from 200 to 250 horizontally :

# for x in range (200,251):
# 	print(x,end=" ")


# Print all even number between 20 to 50 :
# for x in range (20,51):
# 	if x%2==0:
# 		print(x)


# Print back counting from 50 to 1 :
# for x in range (50,0,-1):
# 	print(x)

#--------------------------------------------------------------

# range (Starting point , ending point, step size)

#--------------------------------------------------------------

# Print the counting with the help of user input:

# x = int(input("Enter the number :- "))
# for i in range (x+1):
# 	print(i)


# Print and count the Leap year from 1947 to till now:

# c = 0
# for i in range(1947,2025):
# 	if i%4==0:
# 		print("Leap year :- ",i)
# 		c+=1
# print("Total number of Leap year :- ",c)



# Print the Table with the help of user input:


# t = int(input("Enter the table name :- "))
# for x in range (1,11):
# 	print(f"{t} X {x} = {x*t}" )


# x =  int(input("Enter the number :- "))
# c = 1
# for i in range (1,11):
# 	c = x*i
# 	print(x,"X",i,"=",c)


# Write a python program with the help of user input to 
# show the Factorial of any number:

# x = int(input("Enter the number :- "))
# c = 1
# for i in range (1,x+1):
# 	c = c*i
# print(f"The Factorial of {x} is : {c}")



# Print the reverse counting  from 50 to 10:

# for i in range (50,9,-1):
# 	print(i)


# Print the reverse counting from 100 to 50
# and step size should be 5

# for i in range (100,49,-5):
# 	print(i)



# x = "Himachal Pradesh"

#While loop :

# y = len(x)
# z = 0
# while y>z:
# 	print(x[z])
# 	z=z+1

#For loop :

# for i in x:
# 	print(i)


# import time

# for i in range (10):
# 	print(i)
# 	time.sleep(1)


# for i in range (30,0,-1):
# 	print(i,end="\r")
# 	time.sleep(1)

#--------------------------------------------------------

# Escape function:

# print("Hello\tworld") -------  tab  
# print("Hello\nworld") -------  new line      
# print("Hello\r world")-------  replace       

#-------------------------------------------------------

# Print the each alphabet of "Hello world"
# with the help of for loop

# x = "Hello world"
# for i in x:
# 	print(i)

# Print 10 times your name with the help of for loop:

# x = "Yogesh saini"
# for i in range (1,11):
# 	print(x)


# statement :

# break 
# continue

# for i in range(1,1000):
# 	if i == 50:
# 		break
# 	else:
# 		print(i)

# for i in range(1,15):
# 	if i == 5 or i == 10:
# 		continue
# 	else:
# 		print(i)


# Write a python program to print the number from 4 to 50
# and exclude all the number which is divisible of 5 and 10:

# for i in range(4,51):
# 	if i%5==0 or i%10==0:
# 		continue
# 	else:
# 		print(i)

#---------------------------------------------------------------------


# Count the total no. of even number from 1 to 20:

# c = 0
# for i in range (1,21):
# 	if i%2==0:
# 		c+=1
# print("Total number of even number :- ",c)




# Find the sum of first 10 number
# s = 0
# for i in range (1,11):
# 	s=s+i
# print("sum of first 10 number :- ",s)



# Find the sum of first 10 even number 
# s = 0
# for i in range (2,21,2):
# 	s+=i
# print("Sum of first 10 even number :- ",s)


# Count the total number from 10 to 30 which is divisible of 2 and 3

# c = 0
# for i in range (10,31):
# 	if i%2==0 and i%3==0:
# 		c+=1
# print("Total number from 10 to 30 which is divisible of 2 and 3 :- ",c)

# x = "India1234@$%"

# for i in x:
# 	if i.isdigit():
# 		break
# 	else:
# 		print(i,end="*")


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# Strings function :::


# x = "Himachal Pradesh"
# import time

# for i in x:
# 	if i=="a":
# 		print(i)
# 		time.sleep(1)



# Show the index of all the alphabet :

# x  = "Himachal Pradesh"
# c = 0
# for i in x:
# 	print(i,c)
# 	c+=1
   
#     OR

# x  = "Himachal Pradesh"

# y = len(x)

# for i in range(y):
# 	print(x[i],"Index :- ",i)  


# Solve negative index also :

# x  = "Himachal Pradesh"
# y = len(x)

# for i in range(y):
# 	print(x[i],"Index :- ",i,"Negative index :- ",i-y)


# Show "a" with its index :

# x = "Himachal Pradesh"
# y = len(x)
# for i in range(y):
# 	if x[i]=="a":
# 		print(x[i]," : ",i)




# x = "data123science@#$4"
# c = 0

# Count total number of alphabet 

# for i in x:
# 	if i.isalpha():
# 		c+=1
# print("Total number of alphabet",c)



# Count total number of digit

# for i in x:
# 	if i.isdigit():
# 		c+=1
# print("Total number of digit :- ",c)


# Count total number of special character 

# for i in x:
# 	if i.isalpha() or i.isdigit():
# 		continue
# 	else:
# 		c+=1
# print("Total number of special character :- ",c)

#         OR

# for i in x:
# 	if i.isalnum():
# 		continue
# 	else:
# 		c+=1
# print("Total number of special character :- ",c)



# x = "data123science@#$4"

# n = 0
# c = 0
# s = 0

# for i in x:
# 	if i.isdigit():
# 		n=n+1
# 	elif i.isalpha():
# 		c+=1
# 	else:
# 		s+=1

# print("Total number of alphabet :- ",c)
# print("Total number of digit :- ",n)
# print("Total number of special character :- ",s)

#---------------------------------------------------------------------------

# Nested loop :- Loop inside the another loop it is called nested
#                loop.


# x = "data"

# for i in range(1,6):
# 	print("------------")
# 	for j in range(1,5):
# 		print(j)


# for i in range (10):
# 	for j in range(i):
# 		print(j,end=" ")
# 	print()


# for i in range(10):
# 	for j in range(10-i):
# 		print(j,end=" ")
# 	print()



# for i in range(10):
# 	for j in range(10-i):
# 		print("*",end=" ")
# 	print()



# x = ["apple","mango","Guava"]

# for i in x:
# 	for j in i:
# 		print(j)



# show the square of each value from 1 to 20:

# for i in range(1,21):
# 	print(i,"=",i**2)


# Show the cube of the number from 1 to 20:

# for i in range(1,21):
# 	print(i,"=",i**3)


# Reverse the given integer :

# input = 7894
# output = 4987

# x = 7894
# print(x)

# print("After the update")
# y = str(x)
# y = y[-1::-1]

# x = int(y)
# print(x)


# 1.  print the hello world 10 times with the help of While loop

# x = 1
# while x < 11:
# 	print("hello World")
# 	x+=1


# 2.  find the all Number from 50 to 100 that is divisibe of 7 and 9.

# for i in range (50,101):
# 	if i%7==0 and i%9==0:
# 		print(i)




# 3.  Count the all Number form 30 to 80 that is divisible of 6 and 8

# c = 0 
# for i in range (30,81):
# 	if i%6==0 and i%8==0:
# 		print(i)
# 		c+=1
# print("Total number between which is divisible of 6 and 8 :- ",c)


# 4.  Write a python program to count the all even Number from 20 to 40 ?

# c = 0
# for i in range (20,41):
# 	if i%2==0:
# 		print(i)
# 		c+=1
# print("Total number of even number from 20 to 40 :- ",c)



# 5.  Write a python program to sum the total value from 10 to 20 ?

# s = 0
# for i in range (10,21):
# 		s=s+i 
# 		print(i)
# print("Total sum of total values from 10 to 20 :- ",s)



# 6.  write a python program to count the all even and Odd Number from 10 to 35 ?


# e = 0
# o = 0
# for i in range (10,36):
# 	if i%2==0:
# 		e+=1
# 	else:
# 		o+=1
# print("Total number of even number :- ",e)
# print("Total number of odd number :- ",o)


# 7.  write a python Program to show the factorial of Any number according to
#     the help of user input ?

# x = int(input("Enter the number :- "))
# f = 1
# for i in range(1,x+1):
# 	f = f*i 
# print("Factorial of",x,"is",f)


# 8.  find the Average of the first 10 Number with the help of while loop ?

# x = 0
# s = 0
# while x<=10:
# 	s = s + x
# 	x+=1
# print("Average of the first 10 Number :- ",s/10)


# 9.  Reverse the Number from 80 to 50 with help of for  and while Loop ?


# while loop :

# x = 81
# y = 50
# while x>y:
# 	x-=1
# 	print(x)

# for loop :

# for i in range(80,49,-1):
# 	print(i)




# 10. print your name of alphabet with the help of while loop ?

# x = "Yogesh saini"
# z = 0
# y = len(x)
# while z<y:
# 	print(x[y])
# 	z+=1



# 11. print the reverse name with the help of while loop.

# x = "Yogesh saini"
# z = 0
# y = len(x)
# while z<y:
# 	y-=1
# 	print(x[y],end="")




# 12. write a python program to show the square root from 1 to 15

# for i in range(1,16):
# 	print(i,"=",i**(1/2))




# 13. write a python program to show the number between 100 to 150 that
#     is divisible of 5 and 9 and 3

# for i in range (100,151):
# 	if i%3==0 and i%5==0 and i%9==0:
# 		print(i)




#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



# x = "I want to become a data scientist"

# find the length of the x without space ?

# c = 0
# for i in x:
# 	if i.isspace():
# 		continue
# 	else:
# 		c+=1
# print("the length of the x without space :- ",c)


# write a python program to print the All odd Number from 1 to 30 ?

# for i in range (1,31):
# 	if i%2!=0:
# 		print(i)



# Write a python Program to print the Number from 1 to 10 and 
# skip the Number 5,4 and 3 ?


# x = [3,4,5]
# for i in range(1,11):
# 	if i in x:
	# if i == 5 or i==4 or i==3:     #or
	# 	continue
	# else:
	# 	print(i)



# write a python program to check the Numeber is divisible of
# 12 and 10 ?

# x = int(input("Enter the number :- "))
# if x%12==0 and x%10==0:
# 	print(x,"is a divisible of 12 and 10")
# else:
# 	print(x,"is not a divisible of 12 and 10")


# Write a python program to whether a number is divisible by 2 and 3 both ?

# x = int(input("Enter the number :- "))
# if x%2==0 and x%3==0:
# 	print("Number is divisible by 2 and 3")
# else:
# 	print("Number is not divisible by 2 and 3")



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



# x = "Himachal Pradesh"

# extract the text given Below
# 1. chal

# print(x[4:8])


# 2. desh

# print(x[12:])

# 3. ma

# print(x[2:4])

# 4. him

# print(x[0:3])

# 5. reverse the Text

# print(x[-1::-1])

# 6. print the all text and step size should be 3

# print(x[0::3])


# 7. join the first and last text

# x = x.split()
# y = "".join(x)
# print(y)


# 8. count "a" how many times repeated

# y = len(x)
# c = 0
# for i in range(y):
# 	if x[i] == "a":
# 		c+=1
# print("Total number of a :- ",c)



# 9. find the index of the space

# for i in x:
# 	if i == " ":
# 		print(x.find(" "))



# 10. convert into a list

# y = x.split()
# print(y)


#------------------------------------------------------------------------
#------------------------------------------------------------------------



# x = ["apple","air","onion","tiger","egg","ball","bus"]

# 1.  print the value whose name start with a

# for i in x:
# 	if i.startswith("a"):
# 		print(i)


# 2.  print the name whose name end with e

# for i in x:
# 	if i.endswith("e"):
# 		print(i)


# 3.  print the name whose length is less than 5

# for i in x:
# 	if len(i)<5:
# 		print(i)



# 4.  print the name whose name startwith alphabet sound





# 5.  Remove air  from the list

# for i in x:
# 	if i=="air":
# 		continue
# 	else:
# 		print(i)



# 6.  convert the list in to string without any seperators

# y = "".join(x)
# print(y)


# 7.  insert the value "tanishka" at the place of "ball".

# y = " ".join(x)
# z = y.replace("ball","tanishka")
# s = z.split(" ")
# for i in s:
# 	print(i)



# 8.  Python program to interchange first and last elements in a list









# 9.  Python program to swap two elements in a list




# 10. Reverse the list





# 11. find the 2nd maximum Number in python
# 12.

# x = [12,45,10,[56,89,[10,100,200,[500,400]]]]



# 100
# 400
# 10
# 89



# write a python program to check the amount after the discount 
# if amount is greater than 3000 than give 30% discount
# if amount is greater than 2000 than give 15% discount
# if amount is less equal to than 2000 than give 5% discount

# x = int(input("Enter the amount :- "))

# if x>3000:
# 	print("Total amount after discount :- ",x-(x*0.3))
# elif x>2000:
# 	print("Total amount after discount :- ",x-(x*0.15))
# else:
# 	print("Total amount after discount :- ",x-(x*0.05))


# Write a Python program that checks whether a given letter is a vowel or a consonant ?

# y = str(input("Enter any alphabet :- ")).upper()
# x = ["a","e","i","o","u"]

# if y in x:
# 	print(y,"is a vowel")
# else:
# 	print(y,"is not a vowel")



# print the back counting from 50 to 1 in while loop ?

# y = 0
# x = 50

# while x>y:
# 	print(x)
# 	x-=1



# Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed 
# to '$', except the first char itself.

# Sample String : 'restart'
# Expected Result : 'resta$t'

# x = "restart"

# x = input("Enter any word :- ")
# y = len(x)
# z = x[0]

# print(z,end="") 
# for i in range(1,y):
# 	if x[i] == z:
# 		print("$",end="")
# 	else:
# 		print(x[i],end="")
		


# Write a Python program to change a given string to a newly
# string where the first and last chars have been exchanged.

# x = input("Enter any word :- ")
# y = len(x)
# a = x[0]
# b = x[-1]
# for i in range(y):
# 	if i==0:
# 		print(b,end="")
# 		# break
# 	elif x[i]==x[-1]:
# 		print(a,end="")
# 		# break
# 	else:
# 		print(x[i],end="")





# Write a Python program to remove characters that have odd
# index values in a given string.

# x = "Databases"

# y = len(x)

# for i in range(y):
# 	if i%2!=0:
# 		continue
# 	else:
# 		print(x[i],end="")




# Write a Python program to check whether a string starts 
# with specified characters.

# x = input("Enter any text :- ")
# y = len(x)

# for i in range(y):
# 	if i==0:
# 		if x[i].isalnum():
# 			print("No,its not starts with specified characters")
# 		else:
# 			print("Yes,it starts with specified characters")


# 1. write a python program to show discounted amount
# if amount is between 4k to 6k then 40%
# if amount is between 2k to 4k then 30%
# if amount is between 1k to 2k then 20%
# else 10%

# x = float(input("Enter the amount :- "))

# if x>=4000 and x<=6000:
# 	d = x*0.4
# 	a = x-d
# elif x<4000 and x>2000:
# 	d = x*0.3
# 	a =x-d
# elif x<2000 and x>=1000:
# 	d = x*0.2
# 	a = x-d
# else:
# 	d = x*0.1
# 	a = x-d
# print("MRP            : ",x)
# print("Discount       : ",d)
# print("After discount : ",a)



# 2.
# write a python to show the grade of the student 
# if student marks is >=90 then show A+
# if student marks is >=85 then show A
# if student marks is >=80 then show B+
# if student maarks is >=70 then show B
# if student marks is >=60 then show C
# if student marks is >=50 then show D
# else show E

# x = int(input("Enter the marks :- "))

# if x>=90:
# 	print("Grade :- A+")
# elif x>=85:
# 	print("Grade :- A")
# elif x>=80:
# 	print("Grade :- B+")
# elif x>=70:
# 	print("Grade :- B")
# elif x>=60:
# 	print("Grade :- C")
# elif x>=50:
# 	print("Grade :- D")
# else:
# 	print("Grade :- E")



# 3.
# write a python program to exchange the values
# in other variables

# x = 10
# y = 20
# z = 30
# output :-
# x = 30
# y = 10
# z = 20


# x,y,z=z,x,y

# print("x = ",x)
# print("y = ",y)
# print("z = ",z)




# x = "Data Science"

# y = len(x)

# for i in range(y):
# 	print(x[i],i,i-y)



# x = "hjg5345v34h6v6h3v3h635hh"

# for i in x:
# 	if i.isalpha():
# 		print(i,end="")


# x = "hjg5345v34h6v6h3v3h635hh"
# y = ""
# for i in x:
# 	if i.isalpha():
# 		y+=i


# print(y)
# print(type(y))

# n = ""
# for i in x:
# 	if i.isdigit():
# 		n = n+i
# print(n)
# n = int(n)
# print(n)
# print(type(n))




# write a python program to count all number who is divisible of 5 and 7
# from 1 to 100
# c = 0
# for i in range (1,101):
# 	if i%5==0 and i%7==0:
# 		c+=1
# 		print(i)

# print("Total number who is divisible of 5 and 7 from 1 to 100 :",c)



# print backward counting from 50 to 1

# for i in range (50,0,-1):
# 	print(i)

# x = "Data Science"

# reverse this text

# print(x[-1::-1])

# or

# y = len(x)

# for i in range (y):
# 	y-=1
# 	print(x[y],end="")

# or

# y = len(x)
# for i in range(y-1,-1,-1):
# 	print(x[i],end="")


# or 

# y = len(x)
# for i in range(1,y+1):
# 	print(x[-i],end="")



# x = "Data Science"

# x = x.split()
# x = x[-1::-1]
# x = " ".join(x)
# print(x)


#----------------------------------------------------------------------
#----------------------------------------------------------------------


# x = ["a","b","c","d"]
# y = ["g","c","d","a","r","o"]

# for i in x:
# 	for j in y:
# 		if i==j:
# 			print(j,end=" ")


# for i in y:
# 	if i in x:
# 		print(i)




# Count the total prime number from 1 to 50:

# x = int(input("Enter the number :-"))
# c = 0

# for a in range(2,x+1):
# 	if a>1:
# 		for i in range(2,(a//2)+1):
# 			if a%i==0:
# 				break
# 		else:
# 			print(a,"is a prime number")
# 			c+=1
# print("Total no. of prime number :- ",c)



# Write a python program to display all the prime number from 
# 25 to 50 :

# x = int(input("Enter the number :-"))

# if x>1:
# 	for i in range(2,(x//2)+1):
# 		if x%i==0:
# 			print(x,"is not a prime number")
# 			break
# 	else:
# 		print(x,"is a prime number")
# else:
# 	print(x,"is not a prime number")
