
#Skriven av Arnab Nandi och Alexandros Simeonidis


def choice():
    while True:
        try:
            print("Ditt val (1-3): ", end="")
            val = int(input())
        except:
            print("Felaktig input, försök igen")
            continue
        if val < 1 or val > 3:
            print("Felaktig input, försök igen")
            continue
        break
    return val

def inmatning():
    data = []
    i = 1
    while True:
        if i == 13:
            break
        print("Ange för månad " + str(i)+ ": ", end="")
        try:
            nederbörd = float(input())
        except :
            print("Felaktig input")
            continue
        if nederbörd<0:
            print("Felaktig input")
            continue
        data.append(nederbörd)
        i = 1 + i
    return data


def statistik(data):
    return [round(sum(data) / len(data),2), min(data), max(data)]