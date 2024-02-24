class human:
    _id = -1 
    _name = ""
    _email = ""
    _contact = ""
    
    def __init__(self,id,name,email,contact):
        self._id = id 
        self._name = name
        self._email=email
        self._contact = contact 
    
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_email(self):
        return self._email
    def get_contact(self):
        return self._contact 
    def set_id(self,newid):
        self._id = newid 
    def set_name(self,newname):
        self.name = newname 
    def set_email(self,newemail):
        self._email = newemail
    def set_contact(self,newcontact):
        self._contact = newcontact
    def displayinfo(self):
        return f"Id number: {self._id} \nName: {self._name} \nEmail: {self._email}\nContactNumber: {self._contact}"



dave = human(1,"David","Dave@hotsinglesinyourarea.com","123")

print(dave.displayinfo())        
    
    