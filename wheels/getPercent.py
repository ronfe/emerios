def getPerNum(molecule, denominator):
    m = float(molecule)
    d = float(denominator)
    num = ("%.2f")%(m/d*100)
    return num
# print(getPerNum(24,120))
