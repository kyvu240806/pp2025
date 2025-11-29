n = int(input("Number of students: "))
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
c = [0 for _ in range(n)]
for i in range(n):
   a[i] = input("ID: ")
   b[i] = input("Name: ")
   c[i] = input("DoB: ")

nc = int(input("Number of courses: "))
ac = [0 for _ in range(nc)]
bc = [0 for _ in range(nc)]
for i in range(nc):
   ac[i] = input("Course ID: ")
   bc[i] = input("Course name: ")

mark = [[0 for _ in range(n)] for _ in range(nc)]
for i in range(n):
   for j in range(nc):
      mark[i][j] = float(input(f"{bc[j]} mark of {b[i]}: "))

def list_courses():
   for i in range(nc):
      print(bc[i])

def list_students():
   for i in range(n):
      print(b[i])

def get_all_marks(course_index):
   for i in range(n):
      print(f"The {bc[course_index]} mark of {b[i]} is {mark[i][course_index]}")


list_courses()
list_students()
get_all_marks(1)


