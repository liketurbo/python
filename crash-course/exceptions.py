def divide_numbers_with_raise(a, b):
  if b == 0:
    raise Exception('Raise: Second argument cannot be zero')
  return a / b


def divide_numbers_with_assert(a, b):
  assert b != 0, 'Assert: Second argument cannot be zero'
  return a / b


try:
  print(divide_numbers_with_raise(1, 1))
  divide_numbers_with_raise(1, 0)
except Exception as err:
  print(str(err))

try:
  print(divide_numbers_with_assert(1, 1))
  divide_numbers_with_assert(1, 0)
except Exception as err:
  print(str(err))
