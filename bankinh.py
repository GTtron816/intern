import random 
class account:
    acc_id=None
    acc_name=None
    balance=None
    def __init__(self,name):
        self.acc_name=name
        self.acc_id=random.randint(100, 500) 
        self.balance=0.0
        print("Your Account ID: {}".format(self.acc_id))
        
    def deposit(self):
             dep=float(input("Enter amount: "))
             self.balance=dep+self.balance
             print("Available Balance: {}".format(self.balance))
    
    def withdraw(self):
             wit=float(input("Enter amount: "))
             if wit>self.balance:
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
    
class savings(account):
    def __init__(self):
         self.name=str(input("Enter Your Name"))
         self.actype="Savings"
         self.min=1000
         super().__init__(self.name)
    def withdraw(self):
         wit=float(input("Enter amount: "))
         if self.balance < self.min:
             print("Low Minimum Balance")
         elif wit>self.balance:
             print("Insufficient Balance")
         elif self.balance-wit < self.min:
             print("Low Balance To Withdraw")
         else:
              self.balance=self.balance-wit
             
class current(account):
    def __init__(self):
         self.name=str(input("Enter Your Name"))
         self.actype="Current"
         self.od=-2000
         super().__init__(self.name)
    def withdraw(self):
        if self.actype=="Current":
            print("You are eligible for withdrawing {}".format(self.balance-(self.od)))
        wit=float(input("Enter amount: "))
        if self.balance < self.od:
            print("Low Balance Than Over Draft")
        elif wit>self.balance and self.balance == self.od:
            print("Insufficient Balance")
        elif self.balance-wit < self.od:
             print("Low Balance To Withdraw")
        else:
            self.balance=self.balance-wit
             
    
    
    
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
            c=0
            state=0
            while state == 0 :
                 print("Choose Your Account type")
                 print("**********************")
                 print("Choose an option")
                 print("1.Current")
                 print("2.Saving")
                 print("**********************")
                 c=int(input("Enter a choice from menu"))
                 match c:
                  case 1:
                    state=1
                    self.acc.append(current())
                    
                  case 2:
                    state=1
                    self.acc.append(savings())  
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
b=bank()
b.banckcall()
                