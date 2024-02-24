import Human
class Student(Human):
    def __init__(self,id,name,email,contact,major,dob,courses):
        super().__init__(id,name,email,contact)
        self.major=major
        self.dob=dob
        self.courses=courses
    def getMajor(self):
        return self.major
    def getDOB(self):
        return self.dob
    def getCourses(self):
        return self.courses
    def setMajor(self,newmajor):
        self.major=newmajor
    def setDOB(self,newdob):
        self.dob=newdob
    def AddCourse(self,course):
        self.courses.append(course)
    def DropCourse(self,course):
        for i in self.courses():
            if i==course:
                self.courses.pop(i)