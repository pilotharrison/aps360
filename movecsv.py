'''
Quick script to isolate validated samples from extracted dataset
'''
import csv, shutil, os

with open('samples.csv', 'r', encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    data = list(reader)

    for f in data:
        f = str(*f)
        shutil.move(f, 'D:\Samples')
        print(f,' moved to folder')
