import random
class spares:
    spare_id=None
    spare_name=None
    spare_qty=None
    def __init__(self,name,qt):
        self.spare_id=random.randint(100, 500)
        self.spare_name=name
        self.qty=qt
    def disp_spare(self):
        id=int(input("Enter a spare id"))
        if id == self.spare_id:
            print("Spare ID: {}".format(self.spare_id))
            print("Spare Name: {}".format(self.spare_name))
            print("Spare Quantity: {}".format(self.spare_qty))
            
class Machine():
    machine_name=None
    loction=None
    m_qty=None
    spare=spares()
    spare=[]
    def __init__(self,name,location,qt):
        self.machine_name=name
        self.loction=location
        self.qty=qt
    def findspare():
        
         c=0
         state=0
         while state == 0 :
                 print("Choose Your Option")
                 print("**********************")
                 print("Choose an option")
                 print("1.Add Spare")
                 print("2.Search Spare")
                 print("**********************")
                 c=int(input("Enter a choice from menu"))
                 match c:
                  case 1:
                    state=1
                    
                    
                  case 2:
                    state=1
                     
    
class factory(Machine):
    factory_id=None
    factory_name=None
    factory_place=None
    def __init__(self,name,place):
        self.factory_name=name
        self.factory_id=random.randint(100, 500)
        self.factory_place=place

        