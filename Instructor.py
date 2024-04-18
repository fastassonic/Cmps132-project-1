from Human import human

class instructor(human):
    __Degree = ""
    __Courses = []
    def __init__(self,id,name,email,contact,degree,courses,debug=False):
        super().__init__(id,name,email,contact)
        self.__Degree = degree 
        self.__Courses = courses
        if debug: 
            print(courses)
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
    def displayinstructorinfo(self,copyofcourselist):
        coursestring = ""
        for key in self.__Courses:
            coursestring += f"  {key.get_name()}\n   id: {key.getClassID()} \n   instructor: {key.getInstructor()} \n   location: {key.getLocation()} \n   semesterid: {key.getSemesterID()}\n   semestername: {key.getSemesterName()} \n"
        if coursestring == "":
            coursestring = "  [Teaching no classes]"
        return "Instructor\n"+ super().displayinfo() + f"\nMajor: {self.__Degree}\n Courses\n" + coursestring