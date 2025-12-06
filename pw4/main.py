from input import inp
from output import outp
from domains.school import School

def main():
	c = School()
	c.input()
	c.calGPA()
	c.printStudents()

if __name__ == "__main__":
    main()