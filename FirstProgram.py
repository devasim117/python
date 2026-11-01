# /********************************** Print Value **********************************/
# print("Hello world", "Hi")
# print(23)
# print(20 + 5)
# /********************************** End Print Value **********************************/


# /********************************** Variables and Data types **********************************/
# name = "Danish"
# age = 25
# age2 = age
# price = 20.90
# boolean = True
# none = None

# print("My name is :", name)
# print("My age is :", age)

# print(type(name))
# print(type(age))
# print(type(price))
# print(type(boolean))
# print(type(none))
# /********************************** End Variables and Data types **********************************/


# /********************************** Pint Sum **********************************/
# a = 5
# b = 10
# sum = a+b

# print(sum)
# /********************************** End Pint Sum **********************************/


# /********************************** Types Of Operators **********************************/
# # /*** Arithmetic Operators ***/
# a = 10
# b = 5

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b) #remainder
# print(a ** b) #a^b


# # /*** Relational Operators ***/
# a = 10
# b = 5

# print(a == b)
# print(a != b)
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)


# # /*** Assignment Operators ***/
# num = 10
# # num += 10
# # num -= 10
# # num *= 10
# # num /= 10
# # num %= 10
# num **= 10

# print(num)


# # /*** Logical Operators ***/
# a = 50
# b = 30
# print(not False)
# # print(not (a > b))


# val1 = True
# val2 = False
# print("AND Operator:", val1 and val2)
# print("OR Operator:", val1 or val2)
# /********************************** End Types Of Operators **********************************/


# /********************************** Type Conversion and Casting **********************************/
# # /*** Type Conversion ***/
# a = 2
# b = 4.25

# sum = a + b #2.0 + 4.25 => 6.25
# print(sum)


# # /*** Type Casting ***/
# # a = int("2")
# # a = float("2")
# a = str("2")
# b = 4.25

# print(type(a))
# print(a + b)

# /********************************** End Type Conversion and Casting **********************************/


# /********************************** Input Value **********************************/
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# marks = float(input("Enter marks: "))

# print("Welcome", name)
# print("age =", age)
# print("marks =", marks)
# /********************************** End Input Value **********************************/


# /********************************** Practice question **********************************/
# ## (1) Write a program to input 2 numbers and print their sum ##
# a = int(input("Type First number: "))
# b = int(input("Type Second number: "))
# print("Sum = ", a + b)


# ## (2) Write a program to input side of a square and print its area ##
# side = float(input("Type the value of side: "))
# # print("Area of square = ", side * side)
# print("Area of square = ", side ** 2)


# ## (3) Write a program to input 2 floating point numbers and print their average ##
# a = float(input("Type First number: "))
# b = float(input("Type Second number: "))
# print("Average = ", (a + b)/2)


## (4) WAP to input 2 int numbers, a and b and  print true if a is greater than or equal to b. if not print false ##
# a = int(input("Type First number: "))
# b = int(input("Type Second number: "))
# print(a >= b)
# /********************************** End Practice question **********************************/


# /********************************** String and Conditional statements **********************************/
# # /*** Strings type ***/
# str1 = "This is a string."
# str2 = 'Apna college'
# str3 = """ Apna college """



# # /*** Strings add new line, tab space ***/
# # str1 = "This is a string. \nWe are creating in python"
# str1 = "This is a string. \tWe are creating in python"
# print(str1)


# # /*** Add 2 Strings ***/
# str1 = "This is a string."
# str2 = ' Apna college'
# final_str = str1+str2
# print(final_str)


# # /*** Find String Length ***/
# str1 = "Apna"
# len1 = len(str1)
# print(len1)

# str2 = 'College'
# len2 = len(str2)
# print(len2)

# final_str = str1+" "+str2
# print(final_str)
# print(len(final_str))


# # /*** Find String Value by index ***/
# str = "Apna College"
# print(str[0])


# # /*** Slicing Positive String ***/
# str = "Apna College"
# print(str[1:4])
# print(str[5:len(str)])
# print(str[:4])
# print(str[5:])


# # /*** Slicing Negative String ***/
# str = "Apple"
# print(str[-3:-1])
# print(str[-5:-2 ])


# # /*** EndsWith() of String ***/
# str = "I am Danish"
# print(str.endswith("ish"))


# # /*** Capitalize() of String ***/
# str = "i am Danish"
# print(str.capitalize())


# # /*** Replace() of String ***/
# str = "i am Danish"
# print(str.replace("Danish","Mohin"))


# # /*** Find() of String ***/
# str = "i am Danish"
# # print(str.find("Am")) #if word does not exist then it will return "-1"
# print(str.find("am"))


# # /*** Count() of String ***/
# str = "i am Danish"
# print(str.count("am"))


# # /*** Conditional Statements (if, elif, else) ***/
# light = "green"
# if (light == "red"):
#     print("stop")  #Indentation(Print se pehle tab ke jitna space dena zaroori hai)
# elif (light == "green"):
#     print("go")
# elif (light == "yellow"):
#     print("look")
# else:
#     print("light is broken")


# # /*** Conditional Statements (if, elif, else) for marks ***/
# marks = int(input("Enter student marks : "))
# if (marks >= 90):
#     grade = "A"
# elif (marks >= 80 and marks < 90):
#     grade = "B"
# elif (marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("Grade of the student : ", grade)


# # /*** Conditional Statements Nesting ***/
# age = 95
# if(age >= 18):
#     if(age>=80):
#         print("Cannot drive nesting")
#     else:
#         print("Can drive")
# else:
#     print("Cannot drive")
# /********************************** End String and Conditional statements **********************************/


# /********************************** Practice question **********************************/
# ## (1) WAP to input user's first name and print its length ##
# name = input("Type First name: ")
# print(len(name))


# ## (2) WAP to find the occurence of "$" in a string ##
# name = "Danish $$"
# print(name.count("$"))


# ## (3) WAP to check if a number entered by the user is odd or even ##
# number = int(input("Enter the number : "))
# reminder = number%2
# if(reminder==0):
#     print("even")
# else:
#     print("odd")


# ## (4) WAP to find the greatest of 3 numbers entered by the user ##
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# if(a>=b and a>=c):
#     print("first number is largest",a)
# elif(b>=c):
#     print("second number is largest",b)
# else:
#     print("third number is largest",c)


## (5) WAP to check if a number is a multiple of 7 or not ##
# x = int(input("Enter number : "))
# if(x%7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")
# /********************************** End Practice question **********************************/


# /********************************** List & Tuple **********************************/
# # /*** List ***/
# student = ["Karan", 95.4, 17, "Delhi"]
# print(student[0])
# student[0] = "Arjun" #not change in string
# print(student)


# # /*** List Slicing ***/
# marks = [10, 20, 30, 40, 50]
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])


# # /*** List Methods ***/
# marks = [100, 20, 30]
# # marks = ["a","b","c"]
# # marks.append(40)
# # marks.sort()
# # marks.sort(reverse=True)
# # marks.reverse()
# # marks.insert(1,80)
# # marks.remove(20)
# marks.pop(2)
# print(marks)


# # /*** Tuples ***/
# tup = (1,2,3,4,4)
# # print(type(tup))
# # print(tup)
# # print(tup[1:3])
# # print(tup.index(4))
# print(tup.count(4))
# /********************************** End List & Tuple **********************************/



# /********************************** Practice question **********************************/
# # (1) WAP to ask the user to enter names of their 3 favorite movies and store them in a list ##
# movies = []
# a = input("Type First movie: ")
# b = input("Type Second movie: ")
# c = input("Type Third movie: ")
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)


# # (2) WAP to check if a list contains a palindrome of elements. (Hint: use copy() method) ##
# # list1 = ["m","a","a","m",]
# list1 = [1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # (3) WAP to count the number of students with the "A" grade in the following tuple. ##
# grade = ["C","D","A","A","B","B","A"]
# print(grade.count("A"))


# # (4) Store the above values in a list & sort them from "A" to "D" ##
# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)
# /********************************** End Practice question **********************************/
