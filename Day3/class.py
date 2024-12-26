class Student:
    branch='cse'#it is static to all 
    def __init__(self,name,roll,branch,address,email):#self is self referencing var
        self.name=name
        self.roll=roll
        self.branch=branch#not req when static
        self.address=address
        self.email=email
    def display(self):
        print('name is:',self.name)#8 bytes
        print('roll is:',self.roll)#4
        print('branch is:',self.branch)#8use Student.branch if static
        #if static print('branch is:',Student)
        print('address is:',self.address)#8
        print('email is:',self.email)#8
#creating obj outside funtion
s1=Student('niharika',165,'cse','sspet','niha@gmail.com')#36 bytes if static 28
s1.display()