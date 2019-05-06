'''
Multiplication table printer
'''


def multi_table(num):
  for i in range(1, 11):
    print('{0:.0f} × {1} = {2:.0f}'.format(num, i, num * i))


num = float(input('Enter a number: '))
multi_table(num)
