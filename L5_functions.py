import numpy as np

def read_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        syror = f.readlines()
    return syror

def syrorStripped(syror):
    syrorList = []
    for syra in syror:
        stripSyra = syra.strip().split()
        syrorList.append(stripSyra)

    syrorList =np.array(syrorList)

    return syrorList


def sortera_syror(matris, val):
    if val == 1:
        sorterad_matris = sorted(matris, key=lambda item: item[0])

    elif val == 2:
        sorterad_matris = sorted(matris, key=lambda item: item[1])

    elif val == 3:
        sorterad_matris = sorted(matris, key=lambda item: item[2])

    else:
         sorterad_matris = sorted(matris, key=lambda item: float(item[3]))

    return sorterad_matris

def check_code(kod,dictionary):
    for i in kod:
        if i not in dictionary:
            print(i + " finns inte som aminosyra, försök igen")
            return False
    return True



