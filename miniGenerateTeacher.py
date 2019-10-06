import csv
import os
from datetime import datetime, date, time
import uuid

name = "Tatjana"
surname = "Čėsnienė"
full_name = name + " " + surname
rank = "Docent"

guid = uuid.uuid5(uuid.NAMESPACE_X500, full_name + rank + "MIF")

print(guid)
print(full_name+" "+rank)