def comma_code(arr):
  out = ''

  for i in range(len(arr)):
    if (i == len(arr) - 1 and len(arr) != 1):
      out += ' and '
    elif (out != ''):
      out += ', '

    out += arr[i]

  return out


arr = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(arr))
