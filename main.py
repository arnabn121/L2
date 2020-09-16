class Country:
    def __init__(self, name, population, area, density=0):
        self.name = name
        self.population = population
        self.area = area
        self.density = self.calcDensity()

    def __str__(self):
        return f"{self.name} {self.population} {self.area} {self.density}"

    def calcDensity(self):
        density = self.population/self.area
        return density



def readCountries(filename):
    with open(filename, "r", encoding="utf8") as f:
            countries = f.readlines()
    return countries


def getCountryObjects(countries):
    objectlist = []
    for country in countries:
        stripCountry = country.strip().split(",")
        objectlist.append(Country(stripCountry[0], float(stripCountry[2]), float(stripCountry[1])))
    return objectlist



countries=readCountries("europa.txt")
for c in getCountryObjects(countries):
    print(c)