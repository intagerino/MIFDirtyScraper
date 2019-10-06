import csv
import os

desktop_path = os.path.expanduser(r'~\Desktop')


def write_csv(teacher_list):

    with open(desktop_path + r'\teachers.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, dialect=csv.excel, delimiter=',')
        writer.writerow(['Id', 'FirstName', 'LastName', 'Description', 'Rank', 'Faculty'])
        for teacher in teacher_list:
            writer.writerow([teacher.guid, teacher.name.decode('utf-8'), teacher.surname.decode('utf-8'), teacher.description, teacher.rank, teacher.faculty])

    file.close()
