# print("Chandan")
# age = int (input("enter your age:"))
# print("your age is :",age)
# print(type(age))
# if(age<10):
#     print("child")
# else:
#     print("not child")
# num=int(input("enter the range :"))
# for i in range(1,num+1):
#     print(i)
#     if(i%2==0):
#         print("even")
#     else:
        # print("odd")

        
# array=[1,2,"bmw"]
# print(len(array))
# print(array[2])
# x =len(array)

# for i in range(x):
#     print(array[i],"\n")

# for i in array:
#     print(i)

# WRITE A PROGRAM TO CHECK IF NUMBER IS EVEN OR ODD
# num=int(input("enter the range :"))
# for i in range(1,num+1):
#     print(i)
#     if(i%2==0):
#         print("even")
#     else:
#         print("odd")

# 
# a=int(input ("enter first number :"))
# b=int(input ("enter seond number :"))
# sum =a+b
# print ("sum=",sum)

# # 



# #
# num = input("enter num1:")
# num2= input("enter num2:")

# if num.isnumeric()==False:
#     print("num1 is not a number")
# elif num2.isnumeric()==False:
#     print("num2 is not a number")
# else:
#     res=int(num)+int(num2)
#     print(str(res))


# 
# num=int(input("enter the number :"))
# if(num<0):
#     print("number is negative")
# elif(num>0):
#     print("number is positive")
# else:
#     print("number is Zero")


# CONVERT INT TO FLOAT AND VICE VERSA
# x=8
# y=float(x)
# print(y)

# g=8.6
# h=int(g)
# print(h)


# PERFORM ALL ARITHMETIC OPERATIONS
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))

# print("Addition:",a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)

# FIND THE LARGEST OF THREE NUMBERS
# n1= int(input("enter the first num:"))
# n2= int(input("enter the second num:"))
# n3= int(input("enter the third num:"))

# if n1>n2 and n1>n3:
#         print("first num is largest")
# elif n2>n1 and n2>n3:
#     print("second num is largest")
# else:
#     print("third num is largest")


# # GET THE ABSOLUTE VALUE OF A NUMBER
# print(abs(n1))
# print(abs(n2))
# print(abs(n3))


# COUNT THE CHARACTER IN STRING 
# char_count={};

# name = "hi how are you "

# for c in name:
#     if c not in char_count:
#         char_count[c]=1
#     else:
#         char_count[c]+=1

# print(char_count)

# #
# def add(): #function 
#     print ("this is add")

# add()

#CONCATINATION
# name="jfhudh"
# age=37;
# print(f"Name is {name},and his age is {age}.")
# text = f"Name is {name},and his age is {age}."
# print(text)

#
# def print_user_info(name,city):
#     text = f"Name is {name},and his city  is {city}."
#     print (text)

# name=input("enter the name:")
# city=input("enter the city name:")

# print_user_info("Chandan","Banglore")
# print_user_info(name,city)


#PRINT DATE AND TIME USING PYTHON 

# from datetime import datetime
# def printTime():
# # Get current date and time
# current_datetime = datetime.now()
# print("Current Date and Time:", current_datetime)

# printTime()


#CALCULATE YOUR CURRENT AGE  
def calculate_age(dob_str):
    from datetime import datetime
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Take DOB input from user
user_dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
print("Your age is:", calculate_age(user_dob))
