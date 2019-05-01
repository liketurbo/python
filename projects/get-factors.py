'''
Find the factors of an integer
'''


def get_factors(num):
  for i in range(1, num + 1):
    if num % i == 0:
      print(i)


num = float(input('Enter your number: '))

if num > 0 and num.is_integer():
  get_factors(int(num))
else:
  print('Please enter a positive integer')
