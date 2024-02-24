from Human import human

class instructor(human):
    __Degree = ""
    __Courses = []
    def __init__(self,id,name,email,contact,degree,courses):
        super().__init__(id,name,email,contact)
        self.__Degree = degree 
        self.__Courses = courses
    def get_degree(self):
        return self.__Degree 
    def set_degree(self,newdegree):
        self.__Degree = newdegree
    def get_courses(self):
        return self.__Courses
    def AddCourse(self,course):
        if not str(course.getClassID()) in self.__Courses:
            self.__Courses.append(str(course.getClassID()))
    def DropCourse(self,course):
        if str(course.getClassID()) in self.__Courses:
            self.__Courses.remove(str(course.getClassID()))
        else:
            print(self.__Courses)
            print(f"No class found for {course.getClassID()}") 
    def displayinfo(self,copyofcourselist):
        coursestring = ""
        for key in self.__Courses:
            coursestring += f"  {copyofcourselist[key].getClassName()}\n  id: {copyofcourselist[key].getClassID()} \n  instructor: {copyofcourselist[key].getInstructor()} \n  location: {copyofcourselist[key].getLocation()} \n  semesterid: {copyofcourselist[key].getSemesterID()}\n  semestername: {copyofcourselist[key].getSemesterName()} \n"
        return "Instructor\n"+ super().displayinfo() + f"\nMajor: {self.__Degree}\n Courses\n" + coursestring