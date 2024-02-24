from Courses import Courses
from Instructor import instructor 
from student import student

Instructordict = {}
Studentdict = {}
coursesdict = {}
def add_instructor(name,email,contact,degree,courses=[],debug=False):
    Instructordict[str(len(Instructordict.keys())+1)] = instructor(str(len(Instructordict.keys())+1),name,email,contact,degree,courses)
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

def changer_instructor_for_class(course,instructor):
    #PLEASE MAKE THESE STRINGS. IT WOULD BE A PAIN IF YOU DIDN't
    Instructordict[course.getInstructor()].DropCourse(course)
    instructor.AddCourse(course)
    
    
    
    

add_instructor("Jane doe","John@john.com","123-498-1087","micro-johnery")
add_instructor("John doe","John@john.com","123-498-1087","macro-johnery",[],True)
add_student("Janie bill","Janie@janie.com","123-abc","Macro johnery","12/19/1")
add_course("Microjohning 101",Instructordict["2"],"John town","123","Summer")
for i in Instructordict.keys():
    print(Instructordict[i].displayinfo([]))
for i in coursesdict.keys():
    print(coursesdict[i].displayinfo())
print(coursesdict)
print(Instructordict)
changer_instructor_for_class(coursesdict["1"],Instructordict["1"])
for i in Instructordict.keys():
    print(Instructordict[i].displayinfo(coursesdict))
for i in coursesdict.keys():
    print(coursesdict[i].displayinfo())

