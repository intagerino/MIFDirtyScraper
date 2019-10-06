import csv
import os
from datetime import datetime, date, time

desktop_path = os.path.expanduser(r'~\Desktop')

lst = []

with open(desktop_path + r'\Teacher_Activity.csv', mode='r') as csvFile:
    spamreader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in spamreader:
        lst.append(row)
csvFile.close()

tl = []

for item in lst:
    for t in item:
        #print(t)
        one = t.split(";")[0]
        two = t.split(";")[1]
        three = t.split(";")[2]
        four = t.split(";")[3]
        five = t.split(";")[4]
        if one == 'ï»¿Id':
            one = 'Id'
        if five == "paskaita":
            five = 1
        elif five == "pratybos":
            five = 2
        elif five == "seminaras":
            five = 3
        elif 'Type' in five:
            five = 'Type'
        else:
            five = 1
        tl.append([one,two,three,four,five])

#print(*tl)


with open(desktop_path + r'\bonkers\Teacher_Activity.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
    writer = csv.writer(csvFile)
    for item in tl:
        writer.writerow(item)

csvFile.close()
