import csv
import os
from datetime import datetime, date, time

desktop_path = os.path.expanduser(r'~\Desktop')


def write_csv(course_list):

    with open(desktop_path + r'\courses.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        row = ['Id', 'Name', 'Type', 'Credits', 'Faculty']
        writer.writerow(row)
        for course in course_list:
            writer.writerow([course.id, course.name.decode('utf-8'), course.type, 5, "MIF"])

    csvFile.close()

def write_csv1(t_c_list):

    with open(desktop_path + r'\teacher_course_list.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        row = ['Teacher Name', 'Course Name']
        writer.writerow(row)
        for item in t_c_list:
            writer.writerow([item.name, item.course.decode('utf-8')])

    csvFile.close()

def write_csv2(g_c_list):

    with open(desktop_path + r'\group_course_list.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        row = ['Group Name', 'Course Name']
        writer.writerow(row)
        for item in g_c_list:
            writer.writerow([item.name, item.course.decode('utf-8')])

    csvFile.close()

def write_funky(funky_list):

    with open(desktop_path + r'\Teacher_Activity.csv', mode='w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        row = ['Id', 'TeacherId', 'CourseId', 'DateStarted', 'Type']
        writer.writerow(row)
        for item in funky_list:
            writer.writerow([item.id, item.tId, item.course, datetime(2019, 9, 1), item.role])

    csvFile.close()
