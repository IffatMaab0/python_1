import csv
example_file = open('example3.csv')
example_reader = csv.reader(example_file)

print(example_reader)
print (type(example_reader))
example_file.close

