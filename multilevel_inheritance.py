#class animal:
 #   def __init__(self,cat,dog,lion,tiger):
  #      self.cat=cat
   #    self.lion=lion
    #    self.tiger=tiger
#class dog(animal):
 #   def __init__(self,dog,labrador,golden_retriever):
  #      super().__init__(dog,)
   #     self.labrador=labrador
    #    self.golden_retriever=golden_retriever
#class labrador(dog):
 #   def __init__(self,labrador,weight,eye_clor):
  #      super().__init__(labrador)
   #     self.weight=weight
    #    self.eye_color=eye_color
class Animal:
    def __init__(self,is_mammal):
        self.is_mammal=is_mammal

class dog(Animal):
    def __init__(self,color,height,weight):
        self.color=color
        self.height=height
        self.weight=weight
        if is_mammal==True:
          return is_mammal
        else:
            return is_bird

class Labrador:
    def __init__