class City:
    def addCityDetails(self,name,country):
        self.name  = name
        self.country = country

    def printCityDetails(self):
        print("City Name:" + self.name)
        print("Country Name:" + self.country)

delhi = City()
delhi.addCityDetails("Delhi","India")
delhi.printCityDetails()


mumbai = City()
mumbai.addCityDetails("Mumbai","India")
mumbai.addCityDetails("london","India")
mumbai.printCityDetails()