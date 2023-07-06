bank=[]
def create():
    account={}
    id=int(input("Account ID"))
    acc=[]
    acc.append(str(input("Enter you name")))
    acc.append(float(0))
    account[id]=acc
    bank.append(account)
    
def withdraw():
    id=int(input("enter your account id"))
    for i in bank:
          if id in i.keys():
             amt=float(input("enter your amount"))
             ac=i[id]
             if amt > ac[1]:
                 print("Insufficient balance")
             else:
                 ac[1]=ac[1]-amt
         
    
    
def dep():
     id=int(input("enter your account id"))
     for i in bank:
         if id in i.keys():
             amt=float(input("enter your amount"))
             ac=i[id]
             ac[1]=ac[1]+amt
             
        
             
        
        
def disp():
    for i in bank:
        print(i)       
        
def disp_menu():
 ch=0
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
            create()
        case 2:
            withdraw()
        case 3:
            dep()
        case 4:
            disp()
        case 5:
            print("Thank You Visit Again")
            exit()
       
disp_menu()
     

     