from MIFTeacherScraper import CsvWriter
import uuid
from MIFTeacherScraper import Definitions
from bs4 import BeautifulSoup
from urllib.request import urlopen

webpage = urlopen(Definitions.url).read().decode('utf-8')
content = BeautifulSoup(webpage, features="html.parser")

tags = []

for tag in content.find_all('a'):
    tags.append(tag.get_text('a'))

#print(*tags)

teachers = tags[tags.index(" Ž") + 1:]
teacher_list = []

for teacher in teachers:
    if teacher.find(",") != -1:
        full_name = teacher.split(",", 1)[0]
        name = full_name.split(" ")[0].encode('utf-8')
        surname = full_name.split(" ")[1].encode('utf-8')
        rank = teacher.split(",", 1)[1]
        guid = uuid.uuid5(uuid.NAMESPACE_X500, full_name + rank + "MIF")
        description = ""

        for r in enumerate(Definitions.ranks):
            (index, s_rank) = r
            if rank.find(s_rank) != -1:
                teacher_instance = Definitions.Teacher(guid, name, surname, description, Definitions.standard_ranks[index], "MIF")
                teacher_list.append(teacher_instance)
                break

CsvWriter.write_csv(teacher_list)


