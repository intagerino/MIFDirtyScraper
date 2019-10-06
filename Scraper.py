import CsvWriter
import Definitions
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import itertools
from MIFTeacherScraper import Scrapery
import uuid

webpage = urlopen(Definitions.url + "/mif/subjects/").read().decode('utf-8') 
content = BeautifulSoup(webpage, 'lxml')

tags = []
tData = []
cData = []

for tag in content.find_all('a'):
    url = tag.get('href')
    tData.append(tag.get_text('a'))
    if url.startswith("/mif/subjects/") and len(url) > 14:
        tags.append(url)

courses = tData[tData.index(" Ž") + 1:]
course_list = []
cId = None
num = 0
num_list = []
for course in courses:
    if course.find(",") != -1:
        full_name = course.split(",", 1)[0]
        name = full_name.encode('utf-8')
        type = course.split(",", 1)[1]
        if "rsitetinė" in type:
            type = "BUS"
        x = full_name + " " + type
        num += 1
        id = uuid.uuid5(uuid.NAMESPACE_X500, x)
        if cId == id:
            num_list.append(num)
            continue
        cId = id
        course_instance = Definitions.course(id, name[:-1], type)
        course_list.append(course_instance)

teacher_list = Scrapery.teacher_list

counter = 0
count = 0
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
funky_list = []
for link in tags:
    print ("parsing: " + link)
    if counter in num_list:
        count += 1
        counter += 1
        continue

    driver.get(Definitions.url + link)
    groupSet = set()
    teacherSet = set()
    time.sleep(0.5)
    p_elements = driver.find_elements_by_class_name("fc-content-skeleton")
    for p_element in p_elements:
        elements = p_element.find_elements_by_partial_link_text('')
        for element in elements:
            g = element.get_attribute("data-groups")
            t = element.get_attribute("data-academics")
            l = element.text
            
            if g != None and t != None:
                gs = set(re.findall("([A-Z]+\s[1-4][k])", g))
                ts = re.finditer("[A-ZČĖĘĮŲŪČŠŽ][a-ząčęėįųūčšž]+\s([A-ZČĖĘĮŲŪČŠŽ][a-ząčęėįųūčšž]+\s?)+", t)
                for m in ts:
                    tId = Definitions.teacherIdFinder.findId(m.group(0), teacher_list)
                    teacherSet.add(tId)
                    if l.lower() == "laboratoriniai darbai":
                        l = "pratybos"
                    if l.lower().find("ir") != -1:
                        for n in range(1):
                            d = l.lower().split(" ir ", 1)[n]
                            if d == "paskaitos":
                                d = "paskaita"
                            funky_list.append([tId, course_list[counter-count].id, d])
                    else:
                        funky_list.append([tId, course_list[counter-count].id, l.lower()])
                groupSet.update(gs)

    if groupSet == set():
        groupSet = None
        teacherSet = None
    courseExtra_instance = Definitions.courseExtra(groupSet,teacherSet)
    cData.append(courseExtra_instance)
    counter += 1
driver.close()
funky_object_list = []

new_k = []

for elem in funky_list:
    if elem not in new_k:
        new_k.append(elem)
funky_list = new_k

for funky in funky_list:    
    id = uuid.uuid4()
    #id = uuid.uuid5(uuid.NAMESPACE_X500, funky[0])
    funky_instance = Definitions.funky(id, funky[0], funky[1], funky[2])
    funky_object_list.append(funky_instance)

CsvWriter.write_csv(course_list)
CsvWriter.write_funky(funky_object_list)