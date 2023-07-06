import random    
class bank:
    acc=[]
    def banckcall(self):
     ch=0
     while ch<=5:
      print("**********************")
      print("Choose an option")
      print("1.Create an Account")
      print("2.Wihdraw")
      print("3.Deposit")
      print("4.Display")
      print("5.Exit")
      print("*********************")
      ch=int(input("Enter a choice from menu"))
      match ch:
        case 1:
            self.acc.append(account())
        case 2:
            id=int(input("Enter account id: "))
            for i in self.acc:
                if i.acc_id == id:
                    i.withdraw()
        case 3:
            id=int(input("Enter account id: "))
            for i in self.acc:
                if i.acc_id == id:
                    i.deposit()
        case 4:
            id=int(input("Enter account id: "))
            for i in self.acc:
                if i.acc_id == id:
                 i.disp()
        case 5:
            print("Thank You Visit Again")
            exit()
            
class account:
    acc_id=None
    acc_name=None
    balance=None
    actype=None
    _min=None
    def __init__(self):
        self.acc_id=random.randint(100, 500) 
        self.acc_name=str(input("Enter account Name"))
        self.balance=0.0
        ch=0
        while self.actype == None:
            print("Choose Your Account type")
            print("**********************")
            print("Choose an option")
            print("1.Current")
            print("2.Saving")
            print("**********************")
            ch=int(input("Enter a choice from menu"))
            match ch:
                case 1:
                    self.actype="Current"
                    self.min=0
           
                case 2:
                    self.actype="Savings"
                    self.min=1000
        print("Your Account ID: {}".format(self.acc_id))
        
    def deposit(self):
             dep=float(input("Enter amount: "))
             self.balance=dep+self.balance
             print("Available Balance: {}".format(self.balance))
    
    def withdraw(self):
             wit=float(input("Enter amount: "))
             if self.actype=="Savings" and self.balance < self.min:
                 print("Low Minimum Balance")
             elif wit>self.balance:
                 print("Insufficient Balance")
             else:
                 self.balance=self.balance-wit
             print("Available Balance: {}".format(self.balance))
        
    def disp(self):
        print("**Account Details**")
        print("Account id : {}".format(self.acc_id))
        print("Account Name : {}".format(self.acc_name))
        print("Account Type : {}".format(self.actype))
        print("Balance : {}".format(self.balance))
b=bank()
b.banckcall()