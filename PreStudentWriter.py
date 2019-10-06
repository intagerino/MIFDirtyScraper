import csv
import os
from datetime import datetime, date, time
import uuid

desktop_path = os.path.expanduser(r'~\Desktop')

with open(desktop_path + r'\students.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
    writer = csv.writer(csvFile)
    row = ['Id', 'FirstName', 'LastName', 'Studies', 'Faculty', 'Description']
    listas = [["Samuelis", "Petraitis", "EKO 1k", "MIF", "Exists"],["Jonas", "Silinskas", "PKI 1k", "MIF", "Exists"],["Samanta", "Juodaitė", "ISI 2k", "MIF", "Exists"],["Eleonora", "Mackėvič", "FDM 4k", "MIF", "Exists"]]
    writer.writerow(row)
    for item in listas:
        x = item[0]+item[1]+item[2]
        id = uuid.uuid5(uuid.NAMESPACE_X500, x)
        writer.writerow([id, item[0], item[1], item[2], item[3],item[4]])

csvFile.close()

with open(desktop_path + r'\comments.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
    writer = csv.writer(csvFile)
    row = ['Id', 'StudentId', 'CommentOnId', 'CommentOnType', 'Content', 'Likes', 'DateCreated']
    listas = [["", "", "StudentProfile", "Smart", 5, datetime(2019, 10, 6)],["", "", "TeacherProfile", "Bad", 2, datetime(2019, 10, 6)],["", "", "TeacherProfile", "Good", 25, datetime(2019, 10, 6)],["", "", "Course", "Best", 1, datetime(2019, 10, 6)]]
    writer.writerow(row)
    for item in listas:
        x = item[0]+item[1]+item[2]
        id = uuid.uuid4()
        writer.writerow([id, item[0], item[1], item[2], item[3],item[4], item[5]])

csvFile.close()