from datetime import date
inv=[]
dailysale=[]
class ItemExist_Error(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return(repr(self.value))
  
def createitem():
    item={}
    id=int(input("Enter Item ID"))
    item_details={}
    name=input("Enter product name")
    cat=input("Enter product category")
    qty=int(input("Enter Product Quantity"))
    item_details.update({"Product Name": name})
    item_details.update({"Product Category":cat})
    item_details.update({"Product Quantity":qty})
    item.update({id:item_details})
    inv.append(item)
    
def upqty():
     id=int(input("Enter Item ID"))
     for i in inv:
         if id in i.keys():
             add=int(input("Enter items to add"))
             item=i.get(id)
             qty=item.get("Product Quantity")
             qty=qty+add
             item.update({"Product Quantity":qty})
            
      


def sell():
     id=int(input("Enter Item ID"))
     for i in inv:
         if id in i.keys():
             sold=int(input("Enter items sold"))
             item=i.get(id)
             qty=item.get("Product Quantity")
             if(qty!=0):
              balqt=qty-sold
              item.update({"Product Quantity":balqt})
              dailysold={}
              today=date.today()
              dailysold.update({"Date":today})
              dailysold.update({"Daily Sale":sold})
              dailysale.append(dailysold)
           
         else:
             print("item not found")
         
        

def searchpr():
    search_para=input("Enter the Product name or category to search")
    for i in inv:
        values=i.values()
        items=i.items()
        for j in values:
            if j.get("Product Name") == search_para or j.get("Product Category")==search_para:
                 for key,n in items:
                     print("*****Search********")
                     print("Product ID:",key,end=' ')
                     print("Product Name:",j.get("Product Name"),end=' ')
                     print("Product Category:",j.get("Product Category"),end=' ')
                     print("Product Quantity",j.get("Product Quantity"))
def genrep():
  id=int(input("Enter Item ID"))
  for i in inv:
         if id in i.keys():
             item=i.get(id)
             print("Product ID: {}".format(id))
             
             print("Product Name: {}".format(item.get("Product Name")))
             print("Product Category: {}".format(item.get("Product Category")))
             print("Product Quantity: {}".format(item.get("Product Quantity")))
             for j in dailysale:
               print("*****DAILY SALE******")
               print("Date: {}".format(j.get("Date")))
               print("Sold items: {}".format(j.get("Daily Sale")))
            
    
def inv_menu():
    ch=0
    while ch<8:
        print("Choose an option from the menu")
        print("******************************")
        print("1. Add an item")
        print("2. Update item quantity")
        print("3. Sell item")
        print("4. Search Product")
        print("5. Generate todays Report")
        print("6.Exit")
        ch=int(input("Enter Your Choice: "))
        match ch:
         case 1:
            createitem()
         case 2:
            upqty()
         case 3:
            sell()
         case 4:
            searchpr()
         case 5:
             genrep()
         case 6:
            print("Thank You")
            exit()
inv_menu()