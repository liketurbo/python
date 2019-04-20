def print_table(data):
  if (len(data) == 0):
    return

  for j in range(len(data[0])):
    for i in range(len(data)):
      max_length = 0
      for w in data[i]:
        max_length = len(w) if len(w) > max_length else max_length
      offset = (max_length - len(data[i][j])) + len(data[i][j])

      print(data[i][j].rjust(offset), end=' ')
    print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
