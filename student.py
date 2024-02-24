import Human
class Student(Human):
    __major = ""
    __dob = ""
    __courses = {}
    def __init__(self,id,name,email,contact,major,dob,courses = {}):
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
        self.__courses[str(course.getcourseid())] = course
    def DropCourse(self,course):
        if str(course.getcourseid()) in self.__courses.keys():
            del self.__courses[course.getcourseid()]
        else:
            print("No class found for {course.getcourseid()}")
    def returncourse(self,updatedcourse):
        if updatedcourse.getcourseid() in self.__courses.keys():
            self.__courses[updatedcourse.getcourseid()] = updatedcourse 
        else:
            print(f"the student appears to be missing {updatedcourse.getcoursename()}")
    def returncourse(self,id):
        if id in self.__courses.keys():
            return self.__courses[id]
        else:
            print("Id not found")
    def displayinfo(self):
        coursestring = ""
        for key in self.__courses.keys():
            coursestring += f"  {self.__courses[key].getclassname()}\n  id: {self.__courses[key].getid()} \n  instructor: {self.__courses[key].getinstructor()} \n  location: {self.__courses[key].getlocation()} \n  semesterid: {self.__courses[key].getsemesterid()}\n  semestername: {self.__courses[key].getsemestername()} \n"
        return super().displayinfo() + f"\nMajor: {self.__major}\nDate of birth: {self.__dob} \n Courses" + coursestring