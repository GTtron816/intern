from datetime import date
import random 
import psycopg2
class NotFoud(Exception):
    pass
conn=psycopg2.connect(database="gt",host="localhost",user="postgres",password="root",port="5432")
cursor=conn.cursor()


  
def createitem():
    id=random.randint(100, 500)
    name=input("Enter product name: ")
    cat=input("Enter product category: ")
    qty=int(input("Enter Product Quantity: "))
    cursor.execute("insert into item values({},'{}',{},{})".format(id,name,cat,qty))
    conn.commit()
    
def upqty():
     id=int(input("Enter Item ID: "))
     qty=int(input("Enter Quantity: "))
     try:
         cursor.execute("update item set qty={} where item_id={}".format(qty,id))
         conn.commit()
         if(cursor.rowcount==0):
             raise NotFoud('Item to Update Not Found')
     except NotFoud as e:
         print(e)

def sell():
     id=int(input("Enter Item ID: "))
     sid=random.randint(100, 500)
     sold=int(input("Enter items sold: "))
     today=date.today()
     cid=int(input("Enter CustomerID: "))
     try:
         cursor.execute("insert into sale values({},{},{},'{}',{})".format(sid,id,sold,today,cid))
         conn.commit()
         cursor.execute("update item set qty=qty-(select dailysale from sale where sale_id={}) where item_id={}".format(sid,id))
         conn.commit()
         if(cursor.rowcount==0):
             raise NotFoud('Item Not Found')
     except NotFoud as e:
         print(e)

def searchpr():
    try:
     search_para=input("Enter the Product name or category to search: ")
     data=[]
     cursor.execute("select item_id,name,cat_name,qty from item inner join cate c on cat=cat_id where name ='{}' or cat_name='{}'".format(search_para,search_para))
     data=cursor.fetchall()
     if(cursor.rowcount==0):
             raise NotFoud('Item Not Found')
     for i in data:
         print(" ")
         print("*****Search********")
         print("Product ID:",i[0],end='   ')
         print("Product Name:",i[1],end='   ')
         print("Product Category:",i[2],end='   ')
         print("Product Quantity",i[3])
    except NotFoud as e:
         print(e)
 
def create_cust():
    id=random.randint(100, 500)
    name=str(input("Enter Customer name: "))
    phno=str(input("Enter Customer Phone: "))
    cursor.execute("insert into customer values({},'{}','{}')".format(id,name,phno))
    conn.commit()
         
def genrep():
  dataitem=[]
  datasale=[]
  try:
   id=int(input("Enter Item ID"))
   cursor.execute("select item_id,name,cat_name,qty from item inner join cate on cat_id=cat where item_id={}".format(id))
   dataitem=cursor.fetchall()
   if(cursor.rowcount==0):
             raise NotFoud('Item Not Found')
   
   for i in dataitem:
     print(" ")
     print("******ITEM DATA********")
     print("Product ID: {}".format(i[0]))
     print("Product Name: {}".format(i[1]))
     print("Product Category: {}".format(i[2]))
     print("Product Quantity: {}".format(i[3]))
   cursor.execute("select day,dailysale,cname,cphone from sale s inner join customer c on s.cid=c.cid where pr_id={}".format(id))
   datasale=cursor.fetchall()
   if(cursor.rowcount==0):
             raise NotFoud('Sales Data Not Found')
   for j in datasale:
        print(" ")
        print("*****DAILY SALE******")
        print("Date: {}".format(j[0]))
        print("Sold items: {}".format(j[1]))
        print("Customer Name: {}".format(j[2]))
        print("Customer Phone: {}".format(j[3]))
  except NotFoud as e:
         print(e)
      
def searchcust():
    try:
     data=[]
     name=str(input("Enter Customer Name: "))
     cursor.execute("select * from customer where cname='{}'".format(name))
     data=cursor.fetchall()
     if(cursor.rowcount==0):
             raise NotFoud('Customer Not Found')
     for i in data:
        print(" ")
        print("Customer ID: {}  Customer Name: {}  Customer Phone: {}".format(i[0],i[1],i[2]))
    except NotFoud as e:
         print(e)
def createcat():
    id=random.randint(100, 500)
    name=str(input("Enter Category name: "))
    cursor.execute("insert into cate values({},'{}')".format(id,name))
    conn.commit()
    
def searchcat():
    try:
     data=[]
     name=str(input("Enter Category Name: "))
     cursor.execute("select * from cate where cat_name='{}'".format(name))
     data=cursor.fetchall()
     if(cursor.rowcount==0):
             raise NotFoud('Category Not Found')
     for i in data:
        print(" ")
        print("Category ID: {}  Category Name: {}".format(i[0],i[1]))
    except NotFoud as e:
         print(e)

def custrep():
    try:
        data=[]
        daydata=[]
        id=int(input("Enter Customer ID: "))
        cursor.execute("select c.cid,cname,cphone,sum(dailysale) from customer c inner join sale s on c.cid=s.cid where c.cid={} and day='{}' group by c.cid,cname,cphone".format(id,date.today()))
        data=cursor.fetchall()
        if(cursor.rowcount==0):
             raise NotFoud('Customer Sales Data Not Found')
        for i in data:
           print(" ")
           print("Customer ID: {}  Customer Name: {}  Customer Phone: {}  Today's Sale: {}".format(i[0],i[1],i[2],i[3]))
        cursor.execute("select day,dailysale from sale s inner join customer c on c.cid = s.cid where c.cid={}".format(id))
        daydata=cursor.fetchall()
        for i in daydata:
            print("Date: {}  Sale: {}".format(i[0],i[1]))
    except NotFoud as e:
      print(e)
   
def inv_menu():
    ch=0
    while ch<11:
        print(" ")
        print("Choose an option from the menu")
        print("******************************")
        print("1. Add an item")
        print("2. Update item quantity")
        print("3. Sell item")
        print("4. Search Product")
        print("5. Generate todays Report")
        print("6. Create Customer")
        print("7. Search Customer")
        print("8. Create Category")
        print("9. Search Category")
        print("10. Customer Report")
        print("11. Exit")
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
             create_cust()
         case 7:
             searchcust()
         case 8:
             createcat()
         case 9:
             searchcat()
         case 10:
             custrep()
         case 11:
            print("Thank You")
            exit()
inv_menu()