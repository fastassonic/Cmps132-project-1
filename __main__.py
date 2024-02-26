from Courses import Courses
from Instructor import instructor 
from student import student
#Global declerations 
Instructordict = {}
Studentdict = {}
coursesdict = {}
Finished = False
#Global methods
def dict_selector(tempdict,customopt = None,allowback=False):
    if customopt == None:
        customopt = []
    #TODO Eventually setup a method to back out of this and have all associated methods deal with the result, shouldn't be to hard to insert a return "No-choice you meatwad"
    for i in tempdict.keys():
        print(f"{i}:{tempdict[i].get_name()}")
    for i in customopt:
        print(f"Other options: {i}")
    if allowback:
        print("Enter \"Back\" to return to the previous menu")
    temp = input("please select one of the options: ")
    if temp in tempdict.keys() or temp in customopt or (temp.lower() == "back" and allowback):
        return temp
    else:
        return dict_selector(tempdict,customopt,allowback)


def add_instructor(name,email,contact,degree,courses=None,debug=False): 
    if courses == None:
        courses = list()
    if len(Instructordict) >= 1:
        key = str(int(list(Instructordict.keys())[-1]) + 1 )
    else:
        key = "1"
    Instructordict[key] = instructor(key,name,email,contact,degree,courses,debug)
    return key
def add_student(name,email,contact,major,dob,courses = None):
    if courses == None:
        courses = {}
    if len(Studentdict) >= 1:
        key = str(int(list(Studentdict.keys())[-1]) + 1 )
    else:
        key = "1"
    Studentdict[key] = student(key,name,email,contact,major,dob,courses)
    return key

def remove_student(id):
    for i in Studentdict[id].returncourselist():
        coursesdict[i].removefromstudentlist(id)
    del Studentdict[id]
    printallcoursesdetails()
def remove_instructor(id):
    del Instructordict[id]
    printallinstructorsdetails()
def add_course(name,instructor,location,semesterID,semesterName,date,time,studentList=None):
    #Note, python is awkward. This is to prevent list sharing, hence why studentlist != [] initially
    if studentList == None: 
        studentList = []
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
    coursesdict[key] = Courses(key,name,instructorid,location,semesterID,semesterName,studentList,date,time)
    if instructorid != "":
        Instructordict[instructorid].AddCourse(coursesdict[key])

def changer_instructor_for_class(course,instructor):
    #pass in the objects. theres logic to manage the rest
    Instructordict[course.getInstructor()].DropCourse(course)
    instructor.AddCourse(course)
    course.setInstructor(instructor.get_id())
    for i in course.getStudentList():
        Studentdict[i].returncourse(course.getClassID()).setInstructor(instructor.get_id())
    
def del_course(courseid):
    for i in coursesdict[courseid].getStudentList():
        Studentdict[i].DropCourse(coursesdict[courseid])
    del coursesdict[courseid]
def add_student_to_course(course,student):
    print(course)
    student.AddCourse(coursesdict[course])
    coursesdict[course].AddTooStudentList(student.get_id())
def del_student_from_course(course,student):
    student.DropCourse(course)
    course.removefromstudentlist(student.get_id())

def updateallstudentcourse(course):
    for i in course.getStudentList():
        Studentdict[i].updatecourse(course)
        
    
    
def printallinstructorsdetails():
    for i in Instructordict.keys():
        print(Instructordict[i].displayinstructorinfo(coursesdict))

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
          Welcome to the penn state beaver student lead Student management system
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
            tempid = add_student(input("Student name?: "),input("Student Email?: "),input("Student contact?: "),input("Student's major?: "),input("Student's DOB?: "))
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
                tempid = dict_selector(Studentdict,allowback=True)
                if tempid.lower() != "back":
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
        if temp == "4":
            tempid = dict_selector(Studentdict,["all"],allowback=True)
            if tempid.lower() == "all":
                printallstudentdetails()
            elif tempid.lower() == "back":
                return()
            else:
                print(Studentdict[tempid].displayinfo())
        if temp == "5":
            studentclassmenu()
        if temp=="6":
            mainmenu()
    else:
        print("not a valid option ")
        studentmenu()
        

def studentclassmenu(editingid=""):
    if editingid == "":
        editingid = dict_selector(Studentdict,allowback=True)
    if editingid.lower() != "back":
        print("""
            Student Classes submenu
            1. Add course
            2. Del course
            3. View registered courses 
            4. Change course grades 
            5. Back
            """)
        temp = input("Please select out of the possible option ")
        if temp in ["1","2","3","4","5"]:
            if temp == "1":
                print("Toggled one")
                tempcourse = dict_selector(coursesdict)
                print(f"Tempcourse is {tempcourse}")
                add_student_to_course(tempcourse,Studentdict[editingid])
            if temp == "2":
                tempcourse = coursesdict[dict_selector(Studentdict[editingid].returncourselist())]
                del_student_from_course(tempcourse,Studentdict[editingid])
            if temp == "3":
                for i in Studentdict[editingid].returncourselist():
                    i.displayinfo()
            if temp == "4":
                coursesid = dict_selector(Studentdict[editingid].returncourselist(),allowback=True)
                if coursesid.lower() != "back":
                    tempgrade = ""
                    while not tempgrade.isnumeric():
                        try:
                            tempgrade = input("Enter in the new grade")
                        except:
                            tempgrade = ""
                    Studentdict[editingid].gradechange(coursesid,int(tempgrade))
            if temp == "5":
                studentmenu()
    else:
        studentmenu()    
            
    
def studenteditmenu(editingid=""):
    if editingid == "":
        editingid = dict_selector(Studentdict,allowback=True)
        #print(editingid)
    if editingid.lower() != "back":
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
    if temp in ["1","2","3","4","5"]:
        if temp=="1":
            print("Adding Instructor")
            tempid = add_instructor(input("Instructor's name?: "), input("Instructor's Email?: "), input("Instructor's contact?: "),input("Instructor's degree?: "))
            print(Instructordict[tempid].displayinstructorinfo(coursesdict))
            print(""" 
                Would you like to resume?
                1. Yes
                2. No
                """)
            if input("") == "1":
                instructorsmenu()
        if temp == "2":
            if len(Instructordict) > 1:
                tempid = dict_selector(Instructordict, allowback=True)
                if tempid.lower() != "back":
                    remove_instructor(tempid)
            else:
                print("Number of instructors cannot be zero")
            print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
            if input("") == "1":
                    instructorsmenu()
        if temp == "3":
            instructoreditmenu()
        if temp == "4":
            tempid = dict_selector(Instructordict, ["all"], allowback=True)

            if tempid.lower() == "all":
                printallinstructorsdetails()
            elif tempid.lower() == "back":
                return ()
            else:
                print(Instructordict[tempid].displayinstructorinfo(coursesdict))
        if temp == "5":
            mainmenu()
    else:
        print("not a valid option ")
        instructorsmenu()


def instructoreditmenu(editingid=""):
    if editingid == "":
        editingid = dict_selector(Instructordict, allowback=True)
    if editingid.lower() != "back":
        print(""" 
            Instructor editing submenu:
            1. Change name
            2. Change email
            3. Change contact 
            4. Change degree
            5. Back
            """)
        temp = input("Please select out of the possible option ")
        if temp in ["1", "2", "3", "4", "5"]:
            if temp == "1":
                Instructordict[editingid].set_name(input("Please enter new name: "))
                print(Instructordict[editingid].get_name())
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(editingid)
            if temp == "2":
                Instructordict[editingid].set_email(input("Please enter new email: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(editingid)
            if temp == "3":
                Instructordict[editingid].set_contact(input("Please enter new contact details: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(editingid)
            if temp == "4":
                Instructordict[editingid].set_degree(input("Please enter new degree: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(editingid)
            if temp == "5":
                instructorsmenu()
        else:
            instructoreditmenu(editingid)
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
    if temp in ["1","2","3","4","5"]:
        if temp == "1":
            print("Instructor selection")
            instructorid = dict_selector(Instructordict,["undefined"],True)
            if instructorid.lower() != "back":
                instructor = Instructordict[instructorid]
                add_course(input("Course name: "),instructor,input("Course Location: "),input("Semester id: "),input("Semester name: "),input("Dates (Please use the mtwrf format): "),input("Please include the time this class occurs"))
                printallcoursesdetails()
        if temp == "2":
            courseid = dict_selector(coursesdict,allowback=True)
            if courseid.lower() != "back":
                del_course(courseid)

                printallcoursesdetails()
        if temp == "3":
            courseeditmenu()
        if temp == "4":
            tempid = dict_selector(coursesdict,["all"],allowback=True)
            if tempid.lower() == "all":
                printallcoursesdetails()
            elif tempid.lower() == "back":
                return()
            else:
                print(coursesdict[tempid].displayinfo())
        if temp=="5":
            mainmenu()

def courseeditmenu(courseid=""):
    if courseid=="":
        courseid = dict_selector(coursesdict)
    if courseid.lower() != "back":
        print(""" 
            Course editing submenu:
            1. Change name
            2. Change instructor
            3. Change location 
            4. Change semesterid
            5. Change semestername
            6. Change date
            7. Change time
            8. Back
            """)
        temp = input("Please select out of the possible option ")
        if temp in ["1","2","3","4","5","6","7","8"]:
            if temp == "1":
                coursesdict[courseid].setClassName(input("Please enter new name: "))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "2":
                instructorid = dict_selector(Instructordict)
                changer_instructor_for_class(coursesdict[courseid],Instructordict[instructorid])
                
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "3":
                coursesdict[courseid].setLocation(input("Please enter new loccation: "))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "4":
                coursesdict[courseid].setSemesterId(input("Please enter new semester Id"))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "5":
                coursesdict[courseid].setSemesterId(input("Please enter new semester Id"))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
                
            if temp == "6":
                coursesdict[courseid].setDate(input("Please enter new dates in mtwrf format"))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "7":
                coursesdict[courseid].setTime(input("Please enter new starttime"))
                updateallstudentcourse(coursesdict[courseid])
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
                
            if temp == "8":
                classesmenu()
    else:
        courseeditmenu(courseid)
    
    
    
            

#Demo students/instructors/courses
add_instructor("Jane doe","John@john.com","123-498-1087","micro-johnery",[],True)
add_instructor("John doe","John@john.com","123-498-1087","macro-johnery",[],True)
add_student("Janie bill","Janie@janie.com","123-abc","Macro johnery","12/19/1")
#name,instructor,location,semesterID,semesterName,date,time,studentList=None
add_course("Microjohning 101",Instructordict["2"],"John town","123","Summer","MWF","12pm")



printallstudentdetails()
#
changer_instructor_for_class(coursesdict["1"],Instructordict["1"])
printallstudentdetails()



#runtime loop
while not Finished:
    Finished = mainmenu()


