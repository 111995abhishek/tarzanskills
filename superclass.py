#class employee:
 #   def __init__(self):
       # pass
#class subclass(employee):
 #   def __init__(self):
  #      super()
class computer:

    def __init__(self,computer, ram, ssd):
        self.computer=computer
        self.ram=ram
        self.ssd=ssd

class laptop(computer):

    def __init__(self,computer,ram,ssd,model):
        super().__init__(computer,ram,ssd)
        self.model=model

lenovo=laptop('lenovo',3,512,1240)
print("the laptop is: ",lenovo.computer)
print("the ram is: ",lenovo.ram)
print("the ssd is",lenovo.ssd)
print("the model is",lenovo.model)