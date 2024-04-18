from Courses import Courses
from Instructor import instructor 
from student import student
from queue import LifoQueue
from collections import deque
from Tree import TreeNode
from queue import Queue
#Global declerations
#TODO WHEN YOUR DONE, MAKE THIS FALSE. IT PRINTS DEBUG INFO
debug = False
Fallinstructor = Queue()
Springinstructor = Queue()
coursesdict = deque()
fallcourses=deque()
springcourses=deque()
Finished = False
Studentstack = LifoQueue()
college = TreeNode("College")



def optionselector(tempdict):
    index = 0
    for i in tempdict.keys():
        print(f"{index}:{i}")
        index += 1
    temp = input("please select one of the options: ")
    if int(temp) < len(tempdict.keys()):
        return tempdict[list(tempdict.keys())[int(temp)]]
    else:
        return optionselector(tempdict)

def AddChild(node,name):
    allreadythere = False
    for i in node.children:
        if i.value == name:
            allreadythere = True
    if not (allreadythere):
        returnnode = TreeNode(name)
        node.add_child(returnnode)
        return returnnode
        
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
    while not tempstack.empty():
        tempobj = tempstack.get()
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
        tempstack.put(i)
    if temp in idlist or temp in customopt or (temp.lower() == "back" and allowback):
        return temp
    else:
        return stack_selector(tempstack,customopt,allowback)

def queue_selector(tempstack,customopt = None,allowback=False):
    if customopt == None:
        customopt = []
    templist = []
    idlist = []
    while not tempstack.empty():
        tempobj = tempstack.get()
        print(f"{tempobj.get_id()}:{tempobj.get_name()}")
        templist.append(tempobj)
        idlist.append(str(tempobj.get_id()))
    for i in customopt:
        print(f"Other options: {i}")
    if allowback:
        print("Enter \"Back\" to return to the previous menu")
    temp = input("please select one of the options: ")
    for i in templist:
        tempstack.put(i)
    if temp in idlist or temp in customopt or (temp.lower() == "back" and allowback):
        return temp
    else:
        return queue_selector(tempstack,customopt,allowback)

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
def add_instructor(stack,name,email,contact,degree,courses=None,debug=False): 
    if courses == None:
        courses = list()
    if stack.qsize() >= 1:
        templist = []
        while not stack.empty():
            templist.append(stack.get())
        key = str(int(templist[-1].get_id()) +1)
        for i in templist:
            stack.put(i)
    else:
        key = "1"
    stack.put(instructor(key,name,email,contact,degree,courses,debug))
    return instructor(key,name,email,contact,degree,courses,debug)

def add_student(stack,name,email,contact,major,dob,courses = None):
    if courses == None:
        courses = {}
    if stack.qsize() >= 1:
        temp = stack.get()
        key = str(int(temp.get_id()) + 1)
        stack.put(temp)
    else:
        key = "1"
    stack.put(student(key,name,email,contact,major,dob,courses))
    return key
def returncourse(id):
    returnobj = None
    for i in coursesdict:
        if str(i.getClassID()) == str(id):
            returnobj = i

    return returnobj
def returnstudent(stack,id):
    print(f"id is {id}")
    templist = []
    found = False
    while stack.qsize() > 0 and not found:
        returnobj = stack.get()
        if debug:
            print(returnobj.get_id())
        if str(returnobj.get_id()) == str(id):
            found = True
        templist.append(returnobj)
    templist.reverse()
    for i in templist:
        stack.put(i)
    if found:
        return returnobj
    else:
        return None
        
def returninstrucotr(queue,id):
    templist = []
    found = False 
    foundobj = None
    while queue.qsize() > 0:
        returnobj = queue.get()
        if debug:
            print(returnobj.get_id())
        if str(returnobj.get_id()) == str(id):
            foundobj = returnobj
            found = True
        templist.append(returnobj)
    for i in templist:
        queue.put(i)
    if found:
        return foundobj
    else:
        return None

def remove_student(stack,id):
    foundstudent = returnstudent(id)
    if foundstudent !=None:
        for i in foundstudent.returncourselist():
            coursesdict[i].removefromstudentlist(id)
        templist = []
        while not stack.empty():
            tempobj = stack.get()
            if tempobj.get_id() != id:
                templist.append(tempobj)
        templist.reverse()
        for i in templist:
            stack.put(i)
        if debug:
            printallcoursesdetails()
def remove_instructor(queue,id):
    templist = []
    while queue.qsize() > 0:
        returnobj = queue.get()
        if debug:
            print(returnobj.get_id())
        if not( str(returnobj.get_id()) == str(id)):
            templist.append(returnobj)
    for i in templist:
        queue.put(i)


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
        key=str(int(coursesdict[-1].getClassID())+1)
    else:
        key=str(1)
    coursesdict.append(Courses(key,name,instructorid,location,semesterID,semesterName,studentList,date,time))
    if(semesterName.lower()=="fall"):
        fallcourses.append(Courses(key,name,instructorid,location,semesterID,semesterName,studentList,date,time))
    elif(semesterName.lower()=="spring"):
        springcourses.append(Courses(key,name,instructorid,location,semesterID,semesterName,studentList,date,time))
    else:
        print("Invalid Semester Name")

def changer_instructor_for_class(course,instructor):
    #pass in the objects. theres logic to manage the rest
    #TODO talk to max about how to implement this
    course.getInstructor().DropCourse(course)
    instructor.AddCourse(course)
    course.setInstructor(instructor)
    updateallstudentcourse(course)
    
def del_course(courseid):
    for i in returncourse(str(courseid)).getStudentList():
        i.DropCourse(returncourse(str(courseid)))
    coursesdict.remove(returncourse(str(courseid)))
    if(returncourse(str(courseid)).getSemesterName.lower()=="spring"):
        springcourses.remove(returncourse(str(courseid)))
    elif(returncourse(str(courseid)).getSemesterName.lower()=="fall"):
        fallcourses.remove(returncourse(str(courseid)))


    
def add_student_to_course(course,student):
    print(course)
    student.AddCourse(course)
    course.AddTooStudentList(student)
def del_student_from_course(course,student):
    student.DropCourse(course)
    course.removefromstudentlist(student.get_id())

def updateallstudentcourse(course):
    for i in course.getStudentList():
        i.updatecourse(course)
        
    
    
def printallinstructorsdetails(queue):
    templist = []
    while not queue.empty():
        tempobj = queue.get()
        tempobj.displayinstructorinfo()
        templist.append(tempobj)

    for i in templist:
       queue.put(i)
#menu functions 

def printallcoursesdetails():
    print("\nFall Courses: \n")
    for i in range(len(fallcourses)):
        print(fallcourses[i].displayinfo())
    print("\nSpring Courses: \n")
    for i in range(len(springcourses)):
        print(springcourses[i].displayinfo())

def printallstudentdetails(stack):
    templist = []
    while not stack.empty():
        tempobj = stack.get()
        print(tempobj.displayinfo())
        templist.append(tempobj)
    templist.reverse()
    for i in templist:
        stack.put(i)
#menu functions 

def mainmenu():
    menudict = {"1":collegemenu,"2":instructorsmenu,"3":classesmenu}
    print("""
          Welcome to the penn state beaver student lead Student management system
          (Note Students are not responsible for any \"Accidental Penn testing that occurs in this system\")
          1. Students 
          2. Instructors
          3. Classes
          """)
    temp = input("Please select out of the possible options")
    if temp in ["1","2","3","4","5"]: 
        print("Good boy!")
        if temp == "5":
            print("Bye bye")
            return True
        else:
            menudict[temp]()
            return False
    else: 
        print("Wow, a contrarian!")
        return False

def studentmenu(stack):
    print(stack)
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
            tempid = add_student(stack,input("Student name?: "),input("Student Email?: "),input("Student contact?: "),input("Student's major?: "),input("Student's DOB?:"))
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu(stack)
        if temp == "2":
            if stack.qsize() > 1:
                #TODO Dict_selector implementation
                tempid = stack_selector(stack,allowback=True)
                if tempid.lower() != "back":
                    remove_student(stack,tempid)
            else:
                print("Number of students would be reduced to 0 during this operation. Please create a new student before destroying the last one ")
            print(""" 
                  Would you like to resume?
                  1. Yes
                  2. No
                  """)
            if input("") == "1":
                studentmenu(stack)
        if temp == "3":
            studenteditmenu(stack)
        if temp == "4":
            #TODO Dict_selector implementation
            tempid = stack_selector(stack,["all"],allowback=True)
            if tempid.lower() == "all":
                printallstudentdetails(stack)
            elif tempid.lower() == "back":
                return()
            else:
                print(returnstudent(stack,tempid).displayinfo())
        if temp == "5":
            studentclassmenu(stack)
        if temp=="6":
            mainmenu()
    else:
        print("not a valid option ")
        studentmenu()
        

def studentclassmenu(stack,editingid=""):
    if editingid == "":
        #TODO Dict_selector implementation
        editingid = stack_selector(stack,allowback=True)
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
                tempcourse = returncourse(course_selector(coursesdict))
                print(f"Tempcourse is {tempcourse}")
                add_student_to_course(tempcourse,returnstudent(stack,editingid))
            if temp == "2":
                tempcourse = coursesdict[dict_selector(returnstudent(stack,editingid).returncourselist())]
                del_student_from_course(tempcourse,returnstudent(stack,editingid))
            if temp == "3":
                for i in returnstudent(stack,editingid).returncourselist():
                    i.displayinfo()
            if temp == "4":
                coursesid = dict_selector(returnstudent(stack,editingid).returncourselist(),allowback=True)
                if coursesid.lower() != "back":
                    tempgrade = ""
                    while not tempgrade.isnumeric():
                        try:
                            tempgrade = [input("Enter in the new quiz 1 grade"),input("Enter in the new quiz 2 grade"),input("Enter in the new quiz 3 grade")]
                        except:
                            tempgrade = ""
                    returnstudent(stack,editingid).gradechange(coursesid,int(tempgrade))
            if temp == "5":
                studentmenu(stack)
    else:
        studentmenu(stack)    
            
    
def studenteditmenu(stack,editingid=""):
    if editingid == "":
        editingid = stack_selector(stack,allowback=True)
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
                returnstudent(stack,editingid).set_name(input("Please enter new name: "))
                print(returnstudent(stack,editingid).get_name())
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(stack,editingid)
            if temp == "2":
                returnstudent(stack,editingid).set_email(input("Please enter new email: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(stack,editingid)
            if temp == "3":
                returnstudent(stack,editingid).set_contact(input("Please enter new contact details: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(stack,editingid)
            if temp == "4":
                returnstudent(stack,editingid).setMajor(input("Please enter new major: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(stack,editingid)
            if temp == "5":
                returnstudent(stack,editingid).setDOB(input("Please enter new DOB: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    studenteditmenu(stack,editingid)
                
            if temp == "6":
                studentmenu()
        else:
            studenteditmenu(stack,editingid)
def instructorsmenu(queue = None):
    if queue == None:
        queue = optionselector({"Spring":Springinstructor,"Fall":Fallinstructor})
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
            
            tempid = add_instructor(queue,input("Instructor's name?: "), input("Instructor's Email?: "), input("Instructor's contact?: "),input("Instructor's degree?: "))
            print(tempid)
            print(""" 
                Would you like to resume?
                1. Yes
                2. No
                """)
            if input("") == "1":
                instructorsmenu()
        if temp == "2":
            if queue.qsize() > 1:
                tempid = queue_selector(queue,allowback=True)
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
            instructoreditmenu(queue)
        if temp == "4":
            tempid = queue_selector(queue,allowback=True)

            if tempid.lower() == "all":
                printallinstructorsdetails()
            elif tempid.lower() == "back":
                return ()
            else:
                print(returninstrucotr(queue,tempid).displayinstructorinfo(coursesdict))
        if temp == "5":
            mainmenu()
    else:
        print("not a valid option ")
        instructorsmenu()


def instructoreditmenu(queue,editingid=""):
    if editingid == "":
        editingid = queue_selector(queue,allowback=True)
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
                returninstrucotr(queue,editingid).set_name(input("Please enter new name: "))
                print(returninstrucotr(queue,editingid).get_name())
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(queue,editingid)
            if temp == "2":
                returninstrucotr(queue,editingid).set_email(input("Please enter new email: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(queue,editingid)
            if temp == "3":
                returninstrucotr(queue,editingid).set_contact(input("Please enter new contact details: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(queue,editingid)
            if temp == "4":
                returninstrucotr(queue,editingid).set_degree(input("Please enter new degree: "))
                print(""" 
                    Would you like to resume?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    instructoreditmenu(queue,editingid)
            if temp == "5":
                instructorsmenu()
        else:
            instructoreditmenu(queue,editingid)
def classesmenu(queue=None):
    if queue == None:
        queue = optionselector({"Spring":springcourses,"Fall":fallcourses})
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
            tempqueue = optionselector({"Spring Instructor":Springinstructor,"Fall Instructor":Fallinstructor})
            instructorid = queue_selector(tempqueue,["undefined"],True)
            if instructorid.lower() != "back":
                instructor = returninstrucotr(tempqueue,instructorid)
                sem=input("Semester name (either Spring or Fall): ")
                while sem.lower() !="spring" and sem.lower() !="fall":
                    print("Invalid Semester Name")
                    sem = input("Semester name (either Spring or Fall): ")
                add_course(input("Course name: "),instructor,input("Course Location: "),input("Semester id: "),sem,input("Dates (Please use the mtwrf format): "),input("Please include the time this class occurs"))
                printallcoursesdetails()
        if temp == "2":
            courseid = course_selector(queue,allowback=True)
            if courseid.lower() != "back":
                del_course(courseid)

                printallcoursesdetails()
        if temp == "3":
            courseeditmenu(queue)
        if temp == "4":
            tempid = course_selector(queue,["all"],allowback=True)
            if tempid.lower() == "all":
                printallcoursesdetails()
            elif tempid.lower() == "back":
                return()
            else:
                print(coursesdict[(int)(tempid)].displayinfo())
        if temp=="5":
            mainmenu()

def courseeditmenu(queue,courseid=""):
    if courseid=="":
        courseid = (int)(course_selector(queue))
    if courseid != "back":
        print(""" 
            Course editing submenu:
            1. Change name
            2. Change instructor
            3. Change location 
            4. Change semester id
            5. Change semester name
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
                    courseeditmenu(queue,courseid)
            if temp == "2":
                tempqueue = optionselector({"Spring Instructor":Springinstructor,"Fall Instructor":Fallinstructor})
                instructorid = queue_selector(tempqueue)
                changer_instructor_for_class(returncourse(courseid),returninstrucotr(tempqueue,instructorid))
                
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
            if temp == "3":
                returncourse(courseid).setLocation(input("Please enter new loccation: "))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
            if temp == "4":
                returncourse(courseid).setSemesterID(input("Please enter new semester Id"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
            if temp == "5":
                returncourse(courseid).setSemesterName(input("Please enter new semester name (Either Fall or Spring)"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
                
            if temp == "6":
                returncourse(courseid).setDate(input("Please enter new dates in mtwrf format"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
            if temp == "7":
                returncourse(courseid).setTime(input("Please enter new starttime"))
                updateallstudentcourse(returncourse(courseid))
                print(""" 
                    Would you like to resume editing?
                    1. Yes
                    2. No
                    """)
                if input("") == "1":
                    courseeditmenu(queue,courseid)
                
            if temp == "8":
                classesmenu()
    else:
        courseeditmenu(queue,courseid)
    
    

def collegemenu():
    finished = False
    while not finished:
        print(f"""
            Penn state Department directory
            1. Add department 
            2. Remove Department
            3. Print all depertments
            4. Navigate through department
            5. Finished
            """)
        temp = input("Please select out of the possible options")
        if temp in ["1","2","3","4","5"]: 
            if temp == "1":
                AddChild(college,input("Name of Department"))
            if temp == "2":
                delnode = treechildselector(college,allowback=True)
                if delnode != "Back":
                    RemoveChild(college,returnchild(college,delnode))
            if temp == "3":
                printallchildvalues(college)
            if temp == "4":
                departmentmenu(returnchild(college,int(treechildselector(college))))
                
            if temp == "5":
                finished = True
                
            
def departmentmenu(node):
    finished = False
    while not finished:
        print(f"""
            {node.value} directory
            1. Add degree 
            2. Remove degree
            3. Print all degree
            4. Navigate through degree
            5. Back
            """)
        temp = input("Please select out of the possible options")
        if temp in ["1","2","3","4","5"]: 
            if temp == "1":
                tempnode = AddChild(node,input("Name of Department"))
                AddChild(tempnode,LifoQueue())
            if temp == "2":
                delnode = treechildselector(node,allowback=True)
                if delnode != "Back":
                    RemoveChild(node,returnchild(node,delnode))
            if temp == "3":
                printallchildvalues(node)
            if temp == "4":
                studentmenu(returnchild(node,int(treechildselector(node=node))).children[0].value)
                
            if temp == "5":
                print("Should be finished?")
                finished = True
    

            


#Demo students/instructors/courses
add_instructor(Fallinstructor,"Jane doe","Jane@john.com","123-498-1087","Physics",[],True)
add_instructor(Fallinstructor,"John doe","John@john.com","123-498-1087","English",[],True)
add_instructor(Fallinstructor,"Walter White","walterwhite@gmail.com","322-343-3422","Chemistry",[],True)
add_student(Studentstack,"Janie bill","Janie@janie.com","123-456-7890","Cmpsc","12/19/1")
add_student(Studentstack,"Jesse Pinkman","jessepinkman@gmail.com","555-555-5555","Cmpsc","09/24/84")
add_student(Studentstack,"Student McStudentface","student@student.com","1","Cmpsc","02/02/02")
add_student(Studentstack,"Doug Douglasson", "doug@doug.com","333","Cmpsc,","03/03/03")
add_student(Studentstack,"Steve Dingle", "steve@school.com","234","Cmpsc,","03/01/03")
add_student(Studentstack,"Joe Smithon", "joe@gmail.com","8","Cmpsc,","01/03/03")
add_student(Studentstack,"Jimbus Robnan", "jimble@gmail.com","50000000000","Cmpsc,","01/01/03")
add_student(Studentstack,"rob", "robert@doug.com","2234343434","Cmpsc,","03/03/06")
add_student(Studentstack,"Joseph Mother", "joe@joeseph.com","3","Cmpsc,","09/03/03")
add_student(Studentstack,"Doug Douglasson 2", "doug2@doug.com","3332","Cmpsc,","03/08/03")

add_course("Physics 211",returninstrucotr(Fallinstructor,"1"),"Here","123","Fall","MWF","12pm")
add_course("English 15",returninstrucotr(Fallinstructor,"2"),"Also here","232","Spring","MWF","10am")
add_course("Chemistry 101",returninstrucotr(Fallinstructor,"3"),"Not here","555","Fall","MTWF","2pm")

AddChild(college,"College of Enginering")
AddChild(college,"College of Medicine")
AddChild(college,"General Education")

AddChild(college.returnchild("College of Enginering"),"Cmpsc")
AddChild((college.returnchild(("College of Enginering"))).returnchild("Cmpsc"),Studentstack)
printallchildvalues(college)

#runtime loop
while not Finished:
    Finished = mainmenu()


