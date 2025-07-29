a=input("enter the text:")

from datetime import datetime

# Get current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

with open("code.txt",'w') as file:
    file.write("This is a new file")
    file.write(a)