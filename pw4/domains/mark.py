class Mark: #not used
   def __init__(self):
      self.__studentID = 0
      self.__courseID = 0
      self.__mark = 0.0

   def input(self):
      self.__studentID = int(input("Student ID to get mark: "))
      self.__courseID = int(input("Course ID to get mark: "))
      self.__mark = float(input("Mark: "))