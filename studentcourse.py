from Courses import Courses
class StudentCourse(Courses):
    def __init__(self,name,id,instructor,location,semesterID,semestername,studentList,grade):
        super().__init__(name,id,instructor,location,semesterID,semestername,studentList)
        self._grade=grade
    def getGrade(self):
        return self._grade
    def setGrade(self,newgrade):
        self._grade=newgrade
    def displayinfo(self):
        #id,name,instructor,location,semesterID,semesterName,studentList
        return f"Course\nId number: {self._id}\nname: {self._name}\nInstructor Id: {self._instructor}\nLocation: {self._location}\nSemester id: {self._semesterID}\nSemester Name: {self._semesterName}\nStudent Grade List: {self._grade}"
