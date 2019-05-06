'''
Quadratic equation root calculator
'''


def roots(a, b, c):
  desc = (b**2 - 4 * a * c)**.5
  x_1 = (-b + desc) / (2 * a)
  x_2 = (-b - desc) / (2 * a)

  print('x1: {0}'.format(x_1))
  print('x2: {0}'.format(x_2))


a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')

roots(float(a), float(b), float(c))
