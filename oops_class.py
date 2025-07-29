class Person:
    def print_name(self,name):
        print("My name is " +name)
    
    def add(self,a,b):
            return a+b

person  = Person()
person.print_name("John")
result = person.add(3,5)
print(result)