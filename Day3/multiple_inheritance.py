from abc import ABC

class RBIBank():
    def interest():#this is abstract method
        pass
    def loan():
        print('provides home loan')

class HDFC(RBIBank):
    def  interest():
        print('11% interest') 

class  SBI(RBIBank):
    def interest():
        print('5% interest')

class AXIS(RBIBank):
    def interest():
        print('7% interest')

aobj=AXIS
aobj.interest()
aobj.loan()    