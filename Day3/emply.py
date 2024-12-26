class Employee:
    company_name='infosys'
    location='hyd'
    #it is static to all 
    def __init__(self,name,id,dept,email):#self is self referencing var
        self.name=name
        self.id=id
        self.dept=dept
        self.email=email
    def display(self):
        print('name is:',self.name)#8 bytes
        print('id is:',self.id)#4
        print('dept is:',self.dept)#8
        #if static print('branch is:',Student)
        print('location is:',Employee.location)#8
        print('email is:',self.email)#8
        print('com_name is:',Employee.company_name)
#creating obj outside funtion
s1=Employee('niharika',165,'designer','niha@gmail.com')#36 bytes if static 28
s1.display()