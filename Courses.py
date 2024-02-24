class Courses:
    def __init__(self,id,name,instructor,location,semesterID,semesterName,studentList):
        self.id=id
        self.name=name
        self.instructor=instructor
        self.location=location
        self.semesterID=semesterID
        self.semesterName=semesterName
        self.studentList=studentList
    def getClassID(self):
        return self.id
    def getClassName(self):
        return self.name
    def getInstructor(self):
        return self.instructor
    def getLocation(self):
        return self.location
    def getSemesterID(self):
        return self.semesterID
    def getSemesterName(self):
        return self.semesterName
    def setClassID(self,newid):
        self.id=newid
    def setClassName(self,newname):
        self.name=newname
    def setInstructor(self,newInstructor):
        self.instructor=newInstructor
    def setLocation(self,newLocation):
        self.location=newLocation
    def setSemesterID(self,newsid):
        self.semesterID=newsid
    def setSemesterName(self,newsname):
        self.semesterName=newsname
    def getStudentList(self):
        return self.studentList
    def setStudentList(self,newlist):
        self.studentList=newlist
