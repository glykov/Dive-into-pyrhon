import os
import csv
import json


list_to_save = []
for root, dirs, files in os.walk("D:\\geekbrains\\dive_into_python"):
    for name in files:
        p = os.path.join(root, name)
        str_to_save = f'{p} {os.path.getsize(p)} Kb\n'
        list_to_save.append(str_to_save)

csv_writer = csv.writer(open("data.csv", "w", encoding="utf-8"))
csv_writer.writerow(list_to_save)

json.dump(list_to_save, open("data.json", "w", encoding="utf-8"))

