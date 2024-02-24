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
    if len(Instructordict) >= 1:
        key = str(int(list(Instructordict.keys())[-1]) + 1 )
    else:
        key = "1"
    Instructordict[key] = instructor(key,name,email,contact,degree,courses,debug)
def add_student(name,email,contact,major,dob,courses = {}):
    if len(Studentdict) >= 1:
        key = str(int(list(Studentdict.keys())[-1]) + 1 )
    else:
        key = "1"
    Studentdict[key] = student(key,name,email,contact,major,dob,courses)
    return key

def remove_student(id):
    del Studentdict[id]
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
    if len(coursesdict) >= 1:
        key = str(int(list(coursesdict.keys())[-1]) + 1 )
    else:
        key = "1"
    coursesdict[key] = Courses(key,name,instructorid,location,semesterID,semesterName,studentList)
    if instructorid != "":
        Instructordict[instructorid].AddCourse(coursesdict[key])
def dict_selector(tempdict,customopt = []):
    for i in tempdict.keys():
        print(f"{i}:{tempdict[i].get_name()}")
    for i in customopt:
        print(f"Other options: {i}")
    temp = input("please select one of the options: ")
    if temp in tempdict.keys() or temp in customopt:
        return temp
    else:
        return dict_selector(tempdict)
    
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
def del_student_from_course(course,student):
    student.DropCourse(course)
    course.removefromstudentlist(student.get_id())
    
    
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
          5. Classes submenu
          6.back
          """)
    temp = input("Please select out of the possible options ")
    if temp in ["1","2","3","4","5","6"]:
        if temp == "1":
            #putting the args here to make it easier to write
            #name,email,contact,major,dob
            tempid = add_student(input("Student name?: "),input("Student Email?: "),"Student contact?: ",input("Student's major?: "),input("Student's DOB?: "))
            print(Studentdict[tempid].displayinfo())
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu()
        if temp == "2":
            if len(Studentdict) > 1:
                tempid = dict_selector(Studentdict)
                remove_student(tempid)
            else:
                print("Number of students would be reduced to 0 during this operation. Please create a new student before destroying the last one ")
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu()
        if temp == "3":
            studenteditmenu()
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu()
        
        if temp == "4":
            tempid = dict_selector(Studentdict,["all"])
            if tempid.lower() == "all":
                printallstudentdetails()
            else:
                print(Studentdict[tempid].displayinfo())
                
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu()
    else:
        print("not a valid option ")
        studentmenu()
        

def studentclassmenu(editingid=""):
    if editingid == "":
        editingid = dict_selector(Studentdict)
    
    print("""
          Student Classes submenu
          1. Add course
          2. Del course
          3. View registered courses 
          4. Change course grades (PLEASE IMPLEMENT THIS I SWEAR)
          5. Back
          """)
    temp = input("Please select out of the possible option ")
    if temp == ["1","2","3","4","5"]:
        if temp == "1":
            add_student_to_course(coursesdict[dict_selector(coursesdict)],Studentdict[editingid])
        if temp == "2":
            del_student_from_course(coursesdict[dict_selector(Studentdict[editingid].returncourselist())],Studentdict[editingid])
            
    
def studenteditmenu(editingid=""):
    if editingid == "":
        editingid = dict_selector(Studentdict)
        #print(editingid)
    print(""" 
          Student editing submenu:
          1. Change name
          2. Change email
          3. Change contact 
          4. Change major 
          5. Change dob
          6. Back
          """)
    temp = input("Please select out of the possible option ")
    if temp in ["1","2","3","4","5","6"]:
        if temp == "1":
            Studentdict[editingid].set_name(input("Please enter new name: "))
            print(Studentdict[editingid].get_name())
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studenteditmenu(editingid)
        if temp == "2":
            Studentdict[editingid].set_email(input("Please enter new email: "))
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studenteditmenu(editingid)
        if temp == "3":
            Studentdict[editingid].set_contact(input("Please enter new contact details: "))
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studenteditmenu(editingid)
        if temp == "4":
            Studentdict[editingid].setMajor(input("Please enter new major: "))
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studenteditmenu(editingid)
        if temp == "5":
            Studentdict[editingid].setDOB(input("Please enter new DOB: "))
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studenteditmenu(editingid)
            
        if temp == "6":
            studentmenu()
    else:
        studenteditmenu(editingid)
def instructorsmenu():
    print("""
          Instructor submenu
          1. Add instructor 
          2. Remove instructor 
          3. Edit instructor 
          4. View Instructor 
          5. Back
          """)
    temp = input("Please select out of the possible options")
    
    

def classesmenu():
    print("""
          Courses submenu
          1. Add course 
          2. Remove course 
          3. Edit course
          4. View course 
          5. Back 
          
          """)
    temp = input("Please select out of the possible options")

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


