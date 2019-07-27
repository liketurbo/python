import csv
import os

os.makedirs('./dist/header-removed', exist_ok=True)

for csv_filename in os.listdir('data'):
  if not csv_filename.endswith('.csv'):
    continue

  print('Removing header from %s...' % csv_filename)

  csv_rows = []

  # Reading
  csv_file = open(os.path.join('data', csv_filename))
  csv_reader = csv.reader(csv_file)

  for row in csv_reader:
    if csv_reader.line_num == 1:
      continue
    csv_rows.append(row)

  csv_file.close()

  # Writting
  csv_file = open(os.path.join('./dist/header-removed', csv_filename), 'w')
  csv_writer = csv.writer(csv_file)

  for row in csv_rows:
    csv_writer.writerow(row)

  csv_file.close()
