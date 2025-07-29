class Person():
    CityName = "mumbai"

    def printName(self,name):
        print(name)

class ECStudent1(Person):
    def printDetails(self):
        print("some message")

class ECStudent2(Person):
    def printDetails(self):
        print("some message")

obj = ECStudent1()
obj.CityName = "new city"
obj.printName("ECStudent1")

obj = ECStudent2()
obj.CityName = "london"
obj.printName("ECStudent2")