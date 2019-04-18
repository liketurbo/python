def collatz_sequence(num):
  if (num % 2 == 0):
    return num // 2
  else:
    return 3 * num + 1


print("Enter number:")
while (True):
  value = input()
  try:
    num = int(value)
    print(collatz_sequence(num))
  except ValueError:
    if (value == 'exit'):
      print('Exiting from program...')
      exit()
    else:
      print('Try again, but this time use numbers, if you done type exit')
