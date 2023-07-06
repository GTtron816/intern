class bank:
    acc_id=None
    acc_name=None
    balance=None
    def createac(self):
        self.acc_id=int(input("Enteraccount ID"))
        self.acc_name=str(input("Enter account Name"))
        self.balance=0.0
    def deposit(self):
        id=int(input("Enter account id: "))
        if id == self.acc_id:
             dep=float(input("Enter amount: "))
             self.balance=dep+self.balance
             print("Available Balance: {}".format(self.balance))
        else:
            print("Invalid account")
    def withdraw(self):
        id=int(input("Enter account id: "))
        if id == self.acc_id:
             wit=float(input("Enter amount: "))
             if wit>self.balance:
                 print("Insufficient Balance")
             else:
                 self.balance=self.balance-wit
             print("Available Balance: {}".format(self.balance))
        else:
            print("Invalid account")
    def disp(self):
        print("**Account Details**")
        print("Account id : {}".format(self.acc_id))
        print("Account Name : {}".format(self.acc_name))
        print("Balance : {}".format(self.balance))
def banckcall():
    ch=0
    b=bank()
    while ch<=5:
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
            b.createac()
        case 2:
            b.withdraw()
        case 3:
            b.deposit()
        case 4:
            b.disp()
        case 5:
            print("Thank You Visit Again")
            exit()
banckcall()
    
        

            