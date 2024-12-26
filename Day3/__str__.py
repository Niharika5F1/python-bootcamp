class Student:
    branch='cse'#it is static to all 
    def __init__(self,name,roll,address,email):#self is self referencing var
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {Student.branch} {self.address} {self.email}'
    
s1=Student('niha',234,'hyd','niha@gamil.com')
s2=Student('joy',40,'sspet','john@gmail.com')
print(s1)
print(s2)