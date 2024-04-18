from Courses import Courses
class StudentCourse(Courses):
    def __init__(self,name,id,instructor,location,semesterID,semestername,studentList,grade,dates,time):
        super().__init__(id,name,instructor,location,semesterID,semestername,studentList,dates,time)
        self._grade=grade
    def getGrade(self):
        total=0
        for i in self._grade:
            total+=i
        total/=len(self._grade)
        return "Quiz Grades: "+str(self._grade)+"\nTotal Grade: "+(str)(total) + "%"
    def setGrade(self,newgrade):
        self._grade=newgrade
    def displayinfo(self):
        #id,name,instructor,location,semesterID,semesterName,studentList
        return f"Course Id number: {self._id}\n name: {self._name}\n Instructor Id: {self._instructor}\n Location: {self._location}\n Semester id: {self._semesterID}\n Semester Name: {self._semesterName}\nClass dates: {self._dates}\nClass Time: {self._time} \nStudent Grade List: {self.getGrade()}"
