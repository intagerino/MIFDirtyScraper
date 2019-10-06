import csv
import os
from datetime import datetime, date, time

desktop_path = os.path.expanduser(r'~\Desktop')

lst = []

with open(desktop_path + r'\DbData\z\Teacher_Activity.csv', mode='r') as csvFile:
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
        if five == '1':
            five = "paskaita"
        elif five == '2':
            five = "pratybos"
        elif five == '3':
            five = "seminaras"
        elif five == 'Type':
            five = 'Type'
        else:
            five = "paskaita"
        tl.append([one,two,three,four,five])

#print(*tl)


with open(desktop_path + r'\bonkers\b\Teacher_Activity.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
    writer = csv.writer(csvFile)
    for item in tl:
        writer.writerow(item)

csvFile.close()
