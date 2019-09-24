class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showname(self):
        print(self.name)

    def showage(self):
        print(self.age)

class Student:

    def __init__(self,student_id):
        self.student_id=student_id

    def getid(self):
        print(self.student_id)

class Principal(Person,Student):

    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        Student.__init__(self,student_id)
Resident1= Principal("john",30,"102")
print(Resident1.showname(),Resident1.showage(),Resident1.getid())