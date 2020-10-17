from decimal import*
getcontext().prec=20
d=Decimal(10)/3
print(d)
from fractions import*
frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 +frac2
print(frac3)
print(type(frac3))