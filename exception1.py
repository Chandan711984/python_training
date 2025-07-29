# num = input("enter num1:")
# num2= input("enter num2:")
# try:
#     if num.isnumeric()==False:
#         raise("num1 is not a number")
#     elif num2.isnumeric()==False:
#         raise("num2 is not a number")
#     else:
#         res=int(num)+int(num2)
#         print(str(res))
# except Exception as e:
#     print(e)


# #
# a=int(input("enter the number:"))

# try:
#     if a>100:
#         raise("number is >100")
#     else:
#         print("number is less than 100")
# except Exception as e:
#     print(e)


##
n1= (input("enter the first num:"))
n2= (input("enter the second num:"))
n3= (input("enter the third num:"))

try:
    if n1.isnumeric()==False:
        
        raise TypeError("num1 is not a number")
        raise("num1 is not a number")
    elif n2.isnumeric()==False:
        
        raise TypeError("num2 is not a number")
        raise("num2 is not a number")
    elif n3.isnumeric()==False:
       
        raise TypeError("num3 is not a number")
        raise("num2 is not a number")
    else:
        if n1>n2 and n1>n3:
            print("first num is largest")
        elif n2>n1 and n2>n3:
            print("second num is largest")
        else:
            print("third num is largest")
            
except Exception as e:
    print(e)
  
    

        
    



