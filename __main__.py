from Courses import Courses
from Instructor import instructor 
from student import student
from queue import LifoQueue
from collections import deque
from Tree import TreeNode
#Global declerations
#TODO WHEN YOUR DONE, MAKE THIS FALSE. IT PRINTS DEBUG INFO
debug = False
Instructordict = {}
Studentstack = LifoQueue()
coursesdict = deque()
Finished = False

college = TreeNode("College")




def AddChild(node,name):
    allreadythere = False
    for i in node.children:
        if i.value == name:
            allreadythere = True
    if not (allreadythere):
        node.add_child(TreeNode(name))
    else:
        print("Department allready exists")

def RemoveChild(node,name):
    allreadythere = False
    for i in node.children:
        if i.value == name:
            allreadythere = True
    if allreadythere:
        node.remove_child(college.returnchild(name))
    else:
        print("Department doesn't exist")


def treechildselector(node,customopt = None,allowback=False):
    defaultoptions = []
    if customopt == None:
        customopt = []
    for i in range(len(node.children)):
        print(f"{i}:{node.children[i].value}")
        defaultoptions.append(str(i))
    for i in customopt:
        print(f"Other options: {i}")
    if allowback:
        print("Enter \"Back\" to return to the previous menu")
    temp = input("please select one of the options: ")
    if temp in defaultoptions or temp in customopt or (temp.lower() == "back" and allowback):
        return temp
    else:
        return treechildselector(node,customopt,allowback)

def returnchild(node,id):
    #I Should implement a value check for this but I won't. if this errors out you've done something wrong.
    return node.children[id]


def printallchildvalues(node):
    print(f"Children for {node.value}")
    for i in range(len(node.children)):
        print(f"    Semseter {i}: {returnchild(node,i).value}")
    


        
    

#Global methods
def dict_selector(tempdict,customopt = None,allowback=False):
    if customopt == None:
        customopt = []
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

def stack_selector(tempstack,customopt = None,allowback=False):
    if customopt == None:
        customopt = []
    templist = []
    idlist = []
    while not Studentstack.empty():
        tempobj = Studentstack.get()
        print(f"{tempobj.get_id()}:{tempobj.get_name()}")
        templist.append(tempobj)
        idlist.append(str(tempobj.get_id()))
    templist.reverse()
    for i in customopt:
        print(f"Other options: {i}")
    if allowback:
        print("Enter \"Back\" to return to the previous menu")
    temp = input("please select one of the options: ")
    for i in templist:
        Studentstack.put(i)
    if temp in idlist or temp in customopt or (temp.lower() == "back" and allowback):
        return temp
    else:
        return stack_selector(tempstack,customopt,allowback)

def course_selector(tempcourses,customopt = None,allowback=False):
    if customopt == None:
        customopt = []
    idlist = []
    for i in tempcourses:
        print(f"{i.getClassID()}: {i.get_name()}")
        idlist.append(str(i.getClassID()))
    for i in customopt:
        print(f"Other options: {i}")
    if allowback:
        print("Enter \"Back\" to return to the previous menu")
    temp = input("please select one of the options: ")
    if str(temp) in idlist or temp in customopt or (temp.lower() == "back" and allowback):
        return str(temp)
    else:
        return course_selector(tempcourses,customopt,allowback)
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
    if Studentstack.qsize() >= 1:
        key = Studentstack.qsize() + 1 
    else:
        key = "1"
    Studentstack.put(student(key,name,email,contact,major,dob,courses))
    return key
def returncourse(id):
    returnobj = None
    for i in coursesdict:
        if str(i.getClassID()) == str(id):
            returnobj = i

    return returnobj
def returnstudent(id):
    print(f"id is {id}")
    templist = []
    found = False
    while Studentstack.qsize() > 0 and not found:
        returnobj = Studentstack.get()
        if debug:
            print(returnobj.get_id())
        if str(returnobj.get_id()) == str(id):
            found = True
        templist.append(returnobj)
    templist.reverse()
    for i in templist:
        Studentstack.put(i)
    if found:
        return returnobj
    else:
        return None
        


def remove_student(id):
    foundstudent = returnstudent(id)
    if foundstudent !=None:
        for i in foundstudent.returncourselist():
            coursesdict[i].removefromstudentlist(id)
        templist = []
        while not Studentstack.empty():
            tempobj = Studentstack.get()
            if tempobj.get_id() != id:
                templist.append(tempobj)
        templist.reverse()
        for i in templist:
            Studentstack.put(i)
        if debug:
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
        key=len(coursesdict)+1
    else:
        key=1
    coursesdict.append(Courses(key,name,instructorid,location,semesterID,semesterName,studentList,date,time))


def changer_instructor_for_class(course,instructor):
    #pass in the objects. theres logic to manage the rest
    #TODO talk to max about how to implement this
    Instructordict[course.getInstructor()].DropCourse(course)
    instructor.AddCourse(course)
    course.setInstructor(instructor.get_id())
    for i in course.getStudentList():
        returnstudent(i).returncourse(course.getClassID()).setInstructor(instructor.get_id())
    
def del_course(courseid):
    coursesdict.remove(returncourse(str(courseid)))

    
def add_student_to_course(course,student):
    print(course)
    student.AddCourse(coursesdict[course])
    coursesdict[course].AddTooStudentList(student.get_id())
def del_student_from_course(course,student):
    student.DropCourse(course)
    course.removefromstudentlist(student.get_id())

def updateallstudentcourse(course):
    for i in course.getStudentList():
        returnstudent(i).updatecourse(course)
        
    
    
def printallinstructorsdetails():
    for i in Instructordict.keys():
        print(Instructordict[i].displayinstructorinfo(coursesdict))

def printallcoursesdetails():
    for i in range(len(coursesdict)):
        print(coursesdict[i].displayinfo())

def printallstudentdetails():
    templist = []
    while not Studentstack.empty():
        tempobj = Studentstack.get()
        print(tempobj.displayinfo())
        templist.append(tempobj)
    templist.reverse()
    for i in templist:
        Studentstack.put(i)
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
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu()
        if temp == "2":
            if Studentstack.qsize() > 1:
                #TODO Dict_selector implementation
                tempid = stack_selector(Studentstack,allowback=True)
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
            #TODO Dict_selector implementation
            tempid = stack_selector(Studentstack,["all"],allowback=True)
            if tempid.lower() == "all":
                printallstudentdetails()
            elif tempid.lower() == "back":
                return()
            else:
                print(returnstudent(tempid).displayinfo())
        if temp == "5":
            studentclassmenu()
        if temp=="6":
            mainmenu()
    else:
        print("not a valid option ")
        studentmenu()
        

def studentclassmenu(editingid=""):
    if editingid == "":
        #TODO Dict_selector implementation
        editingid = stack_selector(Studentstack,allowback=True)
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
                tempcourse = course_selector(coursesdict)
                print(f"Tempcourse is {tempcourse}")
                add_student_to_course(tempcourse,returnstudent(editingid))
            if temp == "2":
                tempcourse = coursesdict[dict_selector(returnstudent(editingid).returncourselist())]
                del_student_from_course(tempcourse,returnstudent(editingid))
            if temp == "3":
                for i in returnstudent(editingid).returncourselist():
                    i.displayinfo()
            if temp == "4":
                coursesid = dict_selector(returnstudent(editingid).returncourselist(),allowback=True)
                if coursesid.lower() != "back":
                    tempgrade = ""
                    while not tempgrade.isnumeric():
                        try:
                            tempgrade = input("Enter in the new grade")
                        except:
                            tempgrade = ""
                    returnstudent(editingid).gradechange(coursesid,int(tempgrade))
            if temp == "5":
                studentmenu()
    else:
        studentmenu()    
            
    
def studenteditmenu(editingid=""):
    if editingid == "":
        editingid = stack_selector(Studentstack,allowback=True)
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
                returnstudent(editingid).set_name(input("Please enter new name: "))
                print(returnstudent(editingid).get_name())
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(editingid)
            if temp == "2":
                returnstudent(editingid).set_email(input("Please enter new email: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(editingid)
            if temp == "3":
                returnstudent(editingid).set_contact(input("Please enter new contact details: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(editingid)
            if temp == "4":
                returnstudent(editingid).setMajor(input("Please enter new major: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(editingid)
            if temp == "5":
                returnstudent(editingid).setDOB(input("Please enter new DOB: "))
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
            courseid = course_selector(coursesdict,allowback=True)
            if courseid.lower() != "back":
                del_course(courseid)

                printallcoursesdetails()
        if temp == "3":
            courseeditmenu()
        if temp == "4":
            tempid = course_selector(coursesdict,["all"],allowback=True)
            if tempid.lower() == "all":
                printallcoursesdetails()
            elif tempid.lower() == "back":
                return()
            else:
                print(coursesdict[(int)(tempid)-1].displayinfo())
        if temp=="5":
            mainmenu()

def courseeditmenu(courseid=""):
    if courseid=="":
        courseid = (int)(course_selector(coursesdict))
    if courseid != "back":
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
                returncourse(courseid).setClassName(input("Please enter new name: "))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "2":
                instructorid = dict_selector(Instructordict)
                changer_instructor_for_class(returncourse(courseid),Instructordict[instructorid])
                
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "3":
                returncourse(courseid).setLocation(input("Please enter new loccation: "))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "4":
                returncourse(courseid).setSemesterID(input("Please enter new semester Id"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "5":
                returncourse(courseid).setSemesterName(input("Please enter new semester name"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
                
            if temp == "6":
                returncourse(courseid).setDate(input("Please enter new dates in mtwrf format"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(courseid)
            if temp == "7":
                returncourse(courseid).setTime(input("Please enter new starttime"))
                updateallstudentcourse(returncourse(courseid))
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
add_instructor("Jane doe","Jane@john.com","123-498-1087","Physics",[],True)
add_instructor("John doe","John@john.com","123-498-1087","English",[],True)
add_instructor("Walter White","walterwhite@gmail.com","322-343-3422","Chemistry",[],True)
add_student("Janie bill","Janie@janie.com","123-456-7890","Computer Science","12/19/1")
add_student("Jesse Pinkman","jessepinkman@gmail.com","555-555-5555","Chemistry","09/24/84")
add_student("Student McStudentface","student@student.com","1","Student Studies","02/02/02")
add_course("Physics 211",Instructordict["1"],"Here","123","Summer","MWF","12pm")
add_course("English 15",Instructordict["2"],"Also here","232","Winter","MWF","10am")
add_course("Chemistry 101",Instructordict["3"],"Not here","555","Fall","MTWF","2pm")

AddChild(college,"College of Enginering")
AddChild(college,"College of Medicine")
print(f"{returnchild(college,int(treechildselector(college))).value} was selected")

AddChild(college,"General Education")
printallchildvalues(college)

#runtime loop
while not Finished:
    Finished = mainmenu()


