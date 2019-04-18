def x():
  global eggs
  eggs = 'local'


eggs = 'global'
x()
print(eggs)


def f():
  print(bacon)


bacon = 'global'
f()


def y():
  # print(eggs)  # ERROR!
  eggs = 'spam local'


eggs = 'global'
y()


def z():
  try:
    print(42 / 2)
    print(42 / 12)
    print(42 / 0)
    print(42 / 1)
  except ZeroDivisionError:
    print('Divided by zero')


z()
