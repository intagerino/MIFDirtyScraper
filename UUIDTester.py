import csv
import os
from datetime import datetime, date, time

desktop_path = os.path.expanduser(r'~\Desktop\bonkers\b')


with open(desktop_path + r'\Teacher_Activity.csv', mode='r') as csvFile:
     spamreader = csv.reader(csvFile, delimiter=',', quotechar='|')
     for row in spamreader:
         print(', '.join(row))
csvFile.close()