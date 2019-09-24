class Employee:
    def __init__(self,id,first_name,last_name,designation,pay,email):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.designation=designation
        self.pay=pay
        self.email=email

    def full_name(self):
        return self.first_name + self.last_name


class Developer(Employee):
    pass
dev_1= Developer(id,first_name,last_name,designation,pay,email)

