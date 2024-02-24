from Courses import Courses
from Instructor import instructor 
from student import student

Instructordict = {}
Studentdict = {}
coursesdict = {}
def add_instructor(name,email,contact,degree,courses=[]):
    Instructordict[str(len(Instructordict.keys())+1)] = instructor(len(Instructordict.keys())+1,name,email,contact,degree,courses)
def add_student(name,email,contact,major,dob,courses = {}):
    Studentdict[str(len(Studentdict.keys())+1)] = student(len(Studentdict.keys())+1,name,email,contact,major,dob,courses)
def add_course(name,instructor,location,semesterID,semesterName,studentList=[]):
    if instructor != "undefined": 
        try:
            instructorid = instructor.get_id()
        except:
            print("This doesn't seem to be an instructor object")
            return()
    else: 
        print("GIven undefined instructor command. Assuming you have yet to build the teacher for this class.")
        instructorid = ""
    coursesdict[str(len(coursesdict.keys())+1)] = Courses(len(coursesdict.keys())+1,name,instructorid,location,semesterID,semesterName,studentList)
    

add_instructor("Jane doe","John@john.com","123-498-1087","micro-johnery")
add_instructor("John doe","John@john.com","123-498-1087","macro-johnery")
add_student("Janie bill","Janie@janie.com","123-abc","Macro johnery","12/19/1")
add_course("Microjohning 101",Instructordict["2"],"John town","123 ?","Summer")
for i in Instructordict.keys():
    print(Instructordict[i].displayinfo([]))
for i in Studentdict.keys():
    print(Studentdict[i].displayinfo())
for i in coursesdict.keys():
    print(coursesdict[i])
