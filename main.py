from functions_LP6test import sortera_syror, syrorStripped, read_txt

class Aminosyror:
    def __init__(self, kod, namn, grupp, vikt):

        self.kod = kod
        self.namn = namn
        self.grupp = grupp
        self.vikt = vikt

    def __str__(self):
        return f"{self.kod} {self.namn} {self.grupp} {self.vikt}"


print("reading aminoacids..." + "\n"
    "...done." + "\n"
    "1 - print table of aminoacids sorted by code" + "\n"
    "2 - print table of aminoacids sorted by name" + "\n"
    "3 - print table of aminoacids sorted by group" + "\n"
    "4 - print table of aminoacids sorted by mass" + "\n"
    "Ditt val (1-4): ", end="")
val = 0
while True:
    try:
        val = int(input())
    except:
        print("Felaktig input, försök igen")
        continue
    if val < 1 or val > 4:
        print("Ditt val måste vara mellan 1-4" + "\n"
            "Försök igen")
        continue
    break

matris = sortera_syror(syrorStripped(read_txt("aminosyror.txt")), val)

def SyrorObjekt(matris):
    syrorObjekt = []
    for syra in matris:
        syrorObjekt.append(Aminosyror(syra[0], syra[1], syra[2], syra[3]))
    return syrorObjekt


for i in SyrorObjekt(matris):
    print(i)


















