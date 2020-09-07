
#Skriven av Arnab Nandi och Alexandros Simeonidis


import sys

from functions import statistik, inmatning, choice

print("Väderprogrammet" +"\n"
      "1 - Mata in nederbörd månadsvis under ett år" + "\n"
      "2 - Se statistik för detta år" + "\n"
      "3 - Avsluta")

data = []


while True:
    val = choice()
    if val == 1:
        data = inmatning()
        print()
    elif val == 2:
        if len(data) == 0 :
            print("Det finns ingen statistik att visa, försök igen")
            continue
        else:
            data = statistik(data)
            print("Medelvärde under året: " + str(data[0]) + "\n"
                  "Min nederbörd under en månad: " + str(data[1]) + "\n"
                  "Max nederbörd under en månad: " + str(data[2]) + "\n")
            continue
    else:
        sys.exit(0)
