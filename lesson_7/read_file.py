import json
import csv

with open('datafile.json') as file:
    dictionary = json.load(file)

with open('new_datafile.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['Id', 'Имя', 'Возраст', 'Телефон'])
    for ide, data in dictionary.items():
        name, age = data
        write.writerow([ide, name, age])