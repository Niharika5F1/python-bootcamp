class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'

class Stud(Person):
    def __init__(self,name,age,roll,branch):
            super().__init__(name,age)#
            self.roll=roll
            self.branch=branch
            
    def __str__(self):#converts obj to string
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'

obj=Stud('niha',20,101,'cse')
print(obj)


class annualday(Stud):
     def __init__(self,name,age,roll,branch,program):
          super().__init__(name,age,roll,branch)
          self.program=program
     def __str__(self):
          studetails=super().__str__()
          return f'{studetails},{self.program}'
     
aobj=annualday('niha',20,'f1','cse','solo')
print(aobj)
    


