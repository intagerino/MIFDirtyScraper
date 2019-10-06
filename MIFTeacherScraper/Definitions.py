url = "https://tvarkarasciai.vu.lt/mif/employees/"

ranks = ["Doc.", "Dok.", "Vyresn. M.", "Vyr. M", "M. Darbuot.", "Prof.", "Asist.", "Habil.", "Lekt.", "Lab."]
standard_ranks =["Docent", "PhD Student", "Senior Research Doctor", "Senior Research Doctor", "Research Doctor",
                 "Professor", "Assistant", "Habilitated Professor", "Lecturer", "Assistant"]


class Teacher:

    def __init__(self, guid, name, surname, description, rank, faculty):
        self.guid = guid
        self.name = name
        self.surname = surname
        self.description = description
        self.rank = rank
        self.faculty = faculty

    def print_parameters(self):
        print("GUID:", self.guid)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Description", self.description)
        print("Rank:", self.rank)
        print("Faculty:", self.faculty)
