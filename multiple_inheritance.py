class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

class Staff:
    def __init__(self,department,name):
        self.department=department
        self.name=name

    def get_staff_details(self):
        return "{} {}".format(self.department,self.name)


class Principal(Teacher,Staff):
    def __init__(self,deparment,name):
        Staff.__init__(self,deparment,name)
shoaib=Principal("admin","shoaib")
print(shoaib.get_staff_details())