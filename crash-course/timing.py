import time


def calc_period():
  product = 1

  for i in range(1, 100000):
    product *= i

  return product


for i in range(3, 0, -1):
  print(i)
  time.sleep(1)

print('Start')

start_time = time.time()
res = calc_period()
end_time = time.time()

print('The result is %s digits long' % len(str(res)))
print('Took %s second to calculate.' % round(end_time - start_time, 2))
