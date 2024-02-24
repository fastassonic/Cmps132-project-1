import Human 

class instructor(Human):
    Degree = ""
    __Courses = []
    def __init__(self,id,name,email,contact,degree,courses = []):
        super().__init__(id,name,email,contact)
        self.Degree = degree 
        self.__Courses = courses
    def get_degree(self):
        return self.Degree 
    def set_degree(self,newdegree):
        self.Degree = newdegree
    def get_courses(self):
        return self.__Courses
    def AddCourse(self,course):
        self.__Courses.append(str(course.getcourseid()))
    def DropCourse(self,course):
        if str(course.getcourseid()) in self.__courses:
            self.__Courses.remove(str(course.getcourseid()))
        else:
            print(f"No class found for {course.getcourseid()}") 
    def displayinfo(self,copyofcourselist):
        coursestring = ""
        for key in self.__courses:
            coursestring += f"  {copyofcourselist[key].getclassname()}\n  id: {copyofcourselist[key].getid()} \n  instructor: {copyofcourselist[key].getinstructor()} \n  location: {copyofcourselist[key].getlocation()} \n  semesterid: {copyofcourselist[key].getsemesterid()}\n  semestername: {copyofcourselist[key].getsemestername()} \n"
        return super().displayinfo() + f"\nMajor: {self.__major}\nDate of birth: {self.__dob} \n Courses" + coursestring