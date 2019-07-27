import csv

example_reader_1 = csv.reader(open('./data/example.csv'))
for row in example_reader_1:
  print('Row #' + str(example_reader_1.line_num) + ' ' + str(row))

example_reader_2 = csv.reader(open('./data/example.csv'))
print(list(example_reader_2))
