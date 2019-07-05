from fractions import Fraction

frac = Fraction(3, 4)
frac = Fraction('2/4')
print(frac)

comp = 2 + 2j
comp = complex('3-3j')
comp.real
comp.imag
comp.conjugate()  # 2 - 3j
abs(comp)  # magnitude
