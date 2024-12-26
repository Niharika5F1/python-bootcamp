class JNTU:
    def schedule_academic():
        print("scheduling Academics")
    def declare_holidays():
        print('national and summer holiday')
    def results():
        print('go to www.jntuhresults.com')

class Sridevi(JNTU):#calling parent from child
    def fees():
        print('3rd year fee is 85k')

sobj=Sridevi
sobj.results()