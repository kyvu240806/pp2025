from .entity import Entity

class Course(Entity):
   def __init__(self):
      super().__init__()
      self.__credits = 0

   def input(self):
      super().input()
      self.__credits = int(input("Number of credits: "))

   def getCredits(self):
      return self.__credits