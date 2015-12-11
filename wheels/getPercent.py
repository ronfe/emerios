def getPerNum(molecule, denominator):
    if molecule == 0 or denominator == 0:
        return str("比值不能为零")
    m = float(molecule)
    d = float(denominator)
    num = ("%.2f")%(m/d*100)
    return num
# print(getPerNum(24,120))
