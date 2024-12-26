from abc import ABC
class vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def breaks():
        print('stop the vehicle')

class RangeRover(vehicle):
    def speed():
        print('380 max speed')
    def milage():
        print('15kmph')
    def model():
        print('new model')

fobj=RangeRover
fobj.milage()
fobj.speed()
fobj.model()
fobj.breaks()
