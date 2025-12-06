class Entity:
   def __init__(self):
      self.__id = ""
      self.__name = ""

   def input(self):
      self.__id = input("ID: ")
      self.__name = input("Name: ")

   def print(self):
      print("ID is ", self.__id)
      print("Name is ", self.__name)

   def getName(self):
      return self.__name