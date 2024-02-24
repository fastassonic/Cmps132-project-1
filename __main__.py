from Courses import Courses
from Instructor import instructor 
from student import student
#Global declerations 
Instructordict = {}
Studentdict = {}
coursesdict = {}
Finished = False
#Global methods
def add_instructor(name,email,contact,degree,courses=[],debug=False):
    Instructordict[str(len(Instructordict.keys())+1)] = instructor(str(len(Instructordict.keys())+1),name,email,contact,degree,courses,debug)
def add_student(name,email,contact,major,dob,courses = {}):
    Studentdict[str(len(Studentdict.keys())+1)] = student(str(len(Studentdict.keys())+1),name,email,contact,major,dob,courses)
def add_course(name,instructor,location,semesterID,semesterName,studentList=[]):
    if instructor != "undefined": 
        try:
            instructorid = str(instructor.get_id())
        except:
            print("This doesn't seem to be an instructor object")
            return()
    else: 
        print("Given undefined instructor command. Assuming you have yet to build the teacher for this class.")
        instructorid = ""
    coursesdict[str(len(coursesdict.keys())+1)] = Courses(str(len(coursesdict.keys())+1),name,instructorid,location,semesterID,semesterName,studentList)
    if instructorid != "":
        Instructordict[instructorid].AddCourse(coursesdict[str(len(coursesdict.keys()))])

def changer_instructor_for_class(course,instructor):
    #pass in the objects. theres logic to manage the rest
    Instructordict[course.getInstructor()].DropCourse(course)
    instructor.AddCourse(course)
    course.setInstructor(instructor.get_id())
    for i in course.getStudentList():
        Studentdict[i].returncourse(course.getClassID()).setInstructor(instructor.get_id())
    

def add_student_to_course(course,student):
    student.AddCourse(course)
    course.AddTooStudentList(student.get_id())
    
def printallinstructorsdetails():
    for i in Instructordict.keys():
        print(Instructordict[i].displayinfo(coursesdict))    

def printallcoursesdetails():
    for i in coursesdict.keys():
        print(coursesdict[i].displayinfo())

def printallstudentdetails():
    for i in Studentdict.keys():
        print(Studentdict[i].displayinfo())
#menu functions 

def mainmenu():
    menudict = {"1":studentmenu,"2":instructorsmenu,"3":classesmenu}
    print("""
          Welcome to the pen state beaver student lead Student management system
          (Note Students are not responsible for any \"Accidental Penn testing that occurs in this system\")
          1. Students 
          2. Instructors
          3. Classes
          4. Finished
          """)
    temp = input("Please select out of the possible options")
    if temp in ["1","2","3","4"]: 
        print("Good boy!")
        if temp == "4":
            print("Bye bye")
            return True
        else:
            menudict[temp]()
            return False
    else: 
        print("Wow, a contrarian!")
        return False

def studentmenu():
    print("""
          Student submenu 
          1. Add student 
          2. Remove student 
          3. Edit student 
          4. View student
          5. Back 
          """)
    

def instructorsmenu():
    print("""
          Instructor submenu
          1. Add instructor 
          2. Remove instructor 
          3. Edit instructor 
          4. View Instructor 
          5. Back
          """)

def classesmenu():
    print("""
          Courses submenu
          1. Add course 
          2. Remove course 
          3. Edit course
          4. View course 
          5. Back 
          
          """)

#Demo students/instructors/courses
add_instructor("Jane doe","John@john.com","123-498-1087","micro-johnery")
add_instructor("John doe","John@john.com","123-498-1087","macro-johnery",[],True)
add_student("Janie bill","Janie@janie.com","123-abc","Macro johnery","12/19/1")
add_course("Microjohning 101",Instructordict["2"],"John town","123","Summer")



printallstudentdetails()
changer_instructor_for_class(coursesdict["1"],Instructordict["1"])
printallstudentdetails()



#runtime loop
while not Finished:
    Finished = mainmenu()


