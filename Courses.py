class Courses:
    #TODO gonna suck but we need to add date and time to this.... augh
    def __init__(self,id,name,instructor,location,semesterID,semesterName,studentList,dates,time,department = None,degree=None):
        self._id=id
        self._name=name
        self._instructor=instructor
        self._location=location
        self._semesterID=semesterID
        self._semesterName=semesterName
        self._studentList=studentList
        self._dates = dates
        self._time = time
        self._department = department
        self._degree = degree
    def getClassID(self):
        return self._id
    #changed for the purpose of dict selector
    def get_name(self):
        return self._name
    def getInstructor(self):
        return self._instructor
    def getLocation(self):
        return self._location
    def getSemesterID(self):
        return self._semesterID
    def getSemesterName(self):
        return self._semesterName
    def getDate(self):
        return self._dates
    def getTime(self):
        return self._time   
    def getDepartment(self):
        return self._department 
    def getDegree(self):
        return self._degree
    def setDepartment(self,ndp):
        self._department = ndp
    def setDegree(self,ndg):
        self._degree = ndg
    def setDate(self,newdate):
        self._dates = newdate
    def setTime(self,newtime):
        self._time = newtime
    def setClassID(self,newid):
        self._id=newid
    def setClassName(self,newname):
        self._name=newname
    def setInstructor(self,newInstructor):
        self._instructor=newInstructor
    def setLocation(self,newLocation):
        self._location=newLocation
    def setSemesterID(self,newsid):
        self._semesterID=newsid
    def setSemesterName(self,newsname):
        self._semesterName=newsname
    def getStudentList(self):
        return self._studentList
    def AddTooStudentList(self,newitem):
        print(f"Adding a new student{newitem} to {self._name}")
        self._studentList.append(newitem)
    def removefromstudentlist(self,delitem):
        if delitem in self._studentList:
            self._studentList.remove(delitem)
        else:
            print("Student id not found? How is this happening")
    def displayinfo(self):
        #id,name,instructor,location,semesterID,semesterName,studentList
        return f"Course\nId number: {self._id}\nname: {self._name}\nInstructor Id: {self._instructor}\nLocation: {self._location}\nDates: {self._dates}\nTime: {self._time}\nSemester id: {self._semesterID}\nSemester Name: {self._semesterName}\nStudent Id List: {self._studentList}"
