import re


def strip(string: str, chars=' '):
  start_index = 0
  end_index = len(string)

  start_index_l = start_index
  while (True):
    start_index_l = string.find(
        chars, start_index_l, start_index + len(chars))

    if start_index_l == -1:
      break

    start_index_l += len(chars)
    start_index = start_index_l

  end_index_l = end_index
  while (True):
    end_index_l = string.find(chars, end_index_l - len(chars), end_index_l)

    if end_index_l == -1:
      break

    end_index = end_index_l
    end_index_l -= len(chars)

  return string[start_index:end_index]


def strip_r(string: str, chars=' '):
  reg = re.compile(r'^(' + chars + r')*(.*?)(' + chars + r')*$')
  return reg.search(string).group(2)


print('START|', end='')

print(strip_r(' Ramzan '), end='')
print(strip_r('  Ramzan   '), end='')
print(strip_r('     Ramzan '), end='')
print(strip_r('--Ramzan---', chars='---'), end='')

print('|END')
