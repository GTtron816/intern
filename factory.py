import random
class spares:
    spare_id=None
    spare_name=None
    qty=None
    def __init__(self,name,qt):
        self.spare_id=random.randint(100, 500)
        self.spare_name=name
        self.qty=qt
class Machine:
    machine_name=None
    loction=None
    qty=None
    def __init__(self,name,location,qt):
        self.machine_name=name
        self.loction=location
        self.qty=qt
    
class factory(Machine):
    factory_id=None
    factory_name=None
    factory_place=None
    def __init__(self,name,place):
        self.factory_name=name
        self.factory_id=random.randint(100, 500)
        self.factory_place=place

        