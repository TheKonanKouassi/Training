import csv
import pandas as pd

my_dict = []

with open('../data/titanic.csv', 'r') as titanic_csv:

    csv_reader = csv.reader(titanic_csv)

    for ind, line in enumerate(csv_reader):

        my_dict.append(line)

print(pd.DataFrame(my_dict).head())




