class EMP:
    def __init__(self,name,role,salary):#without parameters in constructor
        self.name=name
        self.role=role
        self.__salary=salary#"__"are given bcoz it is private data

    def get_salary(self):    #public method and data is private
        print(self.__salary)
    
    def Empdisplay(self):  #public method
        print(self.name,self.role)

    
class Company(EMP):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc

    def Comdisplay(self):
        print(self.cname,self.loc)

    def _hiring(self):     #protected method
        print('hiring the freshers')

cobj=Company('accenture','hyd')
eobj=EMP('niha','dev',85000)
eobj.Empdisplay()
cobj.Comdisplay()
cobj._hiring()
eobj.get_salary()

