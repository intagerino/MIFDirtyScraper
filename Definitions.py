url = "https://tvarkarasciai.vu.lt"

class course:

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def print_parameters(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("Type:", self.type)

class courseExtra:

    def __init__(self, groups, teachers):
        self.groups = groups
        self.teachers = teachers

    def print_parameters(self):
        print("Groups:",*self.groups)
        print("Teachers:", *self.teachers)

class courseFull:

    def __init__(self, name, type, groups, teachers):
        self.name = name
        self.type = type
        self.groups = groups
        self.teachers = teachers

    def print_parameters(self):
        print("Name:", self.name)
        print("Type:", self.type)
        if self.groups != None:
            print("Groups:",*self.groups)
        else:
            print("Groups: None")
        if self.teachers != None:
            print("Teachers:", *self.teachers)
        else:
            print("Teachers: None")

class t_c_data:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def print_parameters(self):
        print("Teacher Id:", self.name)
        print("Course Name:", self.course)

class g_c_data:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def print_parameters(self):
        print("Group Name:", self.name)
        print("Course Name:", self.course)

class funky:

    def __init__(self, id, tId, course, role):
        self.id = id
        self.tId = tId
        self.course = course
        self.role = role

    def print_parameters(self):
        print("Id:", self.id)
        print("Teacher Id:", self.tId)
        print("Course:", self.course)
        print("Role:", self.role)

class teacherIdFinder:
    def findId (name, teacher_list):
        #print("HERE BE ! " + name)
        for teacher in teacher_list:
            #print("THERE IS ! " + (teacher.name.decode('utf-8') + " " + teacher.surname.decode('utf-8')))
            if (teacher.name.decode('utf-8') + " " + teacher.surname.decode('utf-8')) == name:
                return teacher.guid
        return None