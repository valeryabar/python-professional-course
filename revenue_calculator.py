from collections import Counter
import csv
import json

files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
cnt_products = Counter()
total = 0

for file in files:
    with open(file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for obj in reader:
            prod, *months = obj.values()
            cnt_products[prod] += sum(map(int, months))

with open('prices.json', encoding='utf-8') as file:
    data = json.load(file)
    for prod, price in data.items():
        total += cnt_products[prod] * price

print(total)
