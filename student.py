from studentcourse import StudentCourse
from Human import human
class student(human):
    __major = ""
    __dob = ""
    __courses = {}
    def __init__(self,id,name,email,contact,major,dob,courses):
        super().__init__(id,name,email,contact)
        self.__major=major
        self.__dob=dob
        self.__courses=courses
    def getMajor(self):
        return self.__major
    def getDOB(self):
        return self.__dob
    def getCourses(self):
        return self.__courses
    def setMajor(self,newmajor):
        self.__major=newmajor
    def setDOB(self,newdob):
        self.__dob=newdob
    def AddCourse(self,course):
        self.__courses[str(course.getClassID())] = StudentCourse(course.get_name(),str(course.getClassID()),course.getInstructor(),course.getLocation(),course.getSemesterID(),course.getSemesterName(),course.getStudentList(),[100,100,100,100],course.getDate(),course.getTime())
    def DropCourse(self,course):
        print(self.__courses.keys())
        if str(course.getClassID()) in str(self.__courses.keys()):
            del self.__courses[course.getClassID()]
        else:
            print("No class found for {course.getcourseid()}")
    def updatecourse(self,updatedcourse):
        if updatedcourse.getcourseid() in self.__courses.keys():
            self.__courses[updatedcourse.getcourseid()] = StudentCourse(updatedcourse.get_name(),str(updatedcourse.getClassID()),updatedcourse.getInstructor(),updatedcourse.getLocation(),updatedcourse.getSemesterID(),updatedcourse.getSemesterName(),updatedcourse.getStudentList(),self.__courses[updatedcourse.getcourseid()].getGrade(),updatedcourse.getDate(),updatedcourse.getTime()) 
        else:
            print(f"the student appears to be missing {updatedcourse.getcoursename()}")
    def returncourselist(self):
        return self.__courses
    def returncourse(self,id):
        print(id)
        if id in self.__courses.keys():
            return self.__courses[id]
        else:
            print("Id not found")
    def gradechange(self,id,newgrade):
        if id in self.__courses.keys():
            self.__courses[id].setGrade(newgrade)
    def displayinfo(self):
        coursestring = ""
        for key in self.__courses.keys():
            coursestring += self.__courses[key].displayinfo()
        return super().displayinfo()[:] + f"\nMajor: {self.__major}\nDate of birth: {self.__dob} \nCourses \n " + coursestring
    
    
    
    
    