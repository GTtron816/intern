import psycopg2
data=[]
conn=psycopg2.connect(database="gt",host="localhost",user="postgres",password="root",port="5432")
cursor=conn.cursor()

id=109
name='joy'
phno='234141578'
cursor.execute("insert into customer values({},'{}','{}')".format(id,name,phno))
conn.commit()
cursor.execute("select * from customer")
data=cursor.fetchall()
for i in data:
        print(i)
conn.close()