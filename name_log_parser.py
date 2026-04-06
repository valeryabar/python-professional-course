from collections import Counter
import csv

with open('name_log.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cnt_names = Counter()
    for row in reader:
        cnt_names[row['email']] += 1

    for email, cnt in sorted(cnt_names.items()):
        print(f'{email}: {cnt}')
