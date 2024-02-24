import Courses
class StudentCourse(Courses):
    def __init__(self,name,id,instructor,location,semesterID,semestername,studentList,grade):
        super().__init__(name,id,instructor,location,semesterID,semestername,studentList)
        self.grade=grade
    def getGrade(self):
        return self.grade
    def setGrade(self,newgrade):
        self.grade=newgrade