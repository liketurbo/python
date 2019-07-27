import csv

output_file = open('./dist/output.tsv', 'w')
output_writer = csv.writer(
    output_file, delimiter='\t', lineterminator='\n>>\n')

output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, World!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])

output_file.close()
