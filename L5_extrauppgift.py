from functions_LP6test import *



class Peptider2:
    def __init__(self, koder, scientificNames):
        self.koder = koder
        self.scientificName = scientificNames


        for k in range(len(self.koder)):
            self.namn = []
            self.sekvens = self.koder[k]

            for e in list(self.sekvens):
                self.namn.append(d.get(e))

            self.namn = "-".join(self.namn)

            print(self.scientificName[k])
            print(self.sekvens + ": " + self.namn)


            self.forekomst()
            print("\n")


    def forekomst(self):
        uni_kod = []
        seq = list(self.sekvens)
        seq = sorted(seq, key=seq.count, reverse=True)

        for i in seq:
           if i not in uni_kod:
            uni_kod.append(i)

        for j in uni_kod:
            ggr = seq.count(j)
            print(d.get(j) + " förekommer " + str(round(ggr / len(seq)* 100, 2)) + "%")



matris = syrorStripped(read_txt("aminosyror.txt"))
amino_matris = matris[:, :2]
d = dict(amino_matris)

print("Hej, välkommen till att skapa peptider." + "\n"
        "Skapa peptider genom att skriva in sekvensen " + "\n"
        "för de aminosyrorna som peptiden ska bestå av. " +"\n"
        "Avsluta genom att skriva in Z.")

i = 1

koder = []
scientificName = []
while True:
    print("Peptid " + str(i) + ": ", end="")
    svar = input().upper()
    if svar == "Z":
        break
    potentiella_koder = list(svar)
    if check_code(potentiella_koder, d) is False:
        continue
    else:
        koder.append(svar)
        scientificName.append(input("Ange namn för peptiden: "))

        i += 1



print("**Dina skapta peptider**")

Peptider2(koder, scientificName)
















