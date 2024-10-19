import mysql.connector as mysql
# Create Database
def crdb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql')
     mycur=mydb.cursor()
     mycur.execute("create database if not exists cycleshop")
     print("database created")
# Show Databases
def showdb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql')
     mycur=mydb.cursor()
     mycur.execute("show databases")
     for i in mycur:
          print(i)
# Create Table In Database
def crtb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("create table shop_management(brand_name varchar(20),billno int,customer_name varchar(19),customer_contactno int,price int)")
     print("table created")
# To Show Tables In Database
def showtb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("show tables")
     data=mycur.fetchall()
     for i in data:
          print(i)
# To Show The Structure Of Table
def desc():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("desc shop_management")
     for i in mycur:
          print(i)
# To Insert Values Into Tables
def insert():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     c=int(input("Enter No. Of Customers ::"))
     for i in range(c):
          bname=input("enter name of brand")
          billno=int(input("enter bill no.::"))
          cname=input("enter the name of customer")
          cont=int(input("enter your contact number"))
          price=int(input("enter the price of cycle"))
          data=("insert into shop_management values('{}',{},'{}',{},{})").format(bname,billno,cname,cont,price)
          mycur.execute(data)
     print("\n\nData is Successfully Added!!!\n")
     mydb.commit()
# To Display All Records
def displaytb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("select * from shop_management")
     data=mycur.fetchall()
     for i in data:
          print(i)
# To Search Any Record     
def search():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     bn=int(input("enter the bill no to be searched"))
     s=("select * from shop_management where billno={}").format(bn)
     mycur.execute(s)
     data=mycur.fetchone()
     print(data)
# To Update Any Data
def update():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     bill=int(input("enter bill number you want to update::"))
     n=input("enter new name of person::")
     bname=input("enter the type of brand::")
     p=int(input("enter the price"))
     con=int(input("enter contact number::"))
     mycur.execute("update shop_management set customer_name='{}',brand_name='{}',price={},customer_contactno='{}' where billno={}".format(n,bname,p,con,bill))
     mydb.commit()
     print("\n\n data is successfully updated!!!\n")
     
# To Delete Record From The Table
def delete():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     billno=int(input("enter bill number to delete a record::"))
     mycur.execute("delete from shop_management where billno={}".format(billno))
     mydb.commit()
     print("\n\ndata is successfully deleted!!!\n")
# To Add Column
def alteradd():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("alter table shop_management add column address varchar(29)")
     print("\n\ncolumn added successfully")
# To Modify The Table
def primary():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("alter table shop_management add primary key(billno)")
     print("\n\ncolumn BILL NO. is now a primary key")
# To Drop A Column
def dropcolumn():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     d=input("enter coloumn name you want to delete::")
     mycur.execute("alter table shop_management drop {}".format(d))
     print("\n\ncolumn",d,"dropped successfully")
# To Arrange In Order Of Bill Number
def orderby():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("select * from shop_management order by billno")
     for i in mycur:
          print(i)
# To  Group by Brand Type
def groupby():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("select brand_name,count(*) from shop_management group by brand_name")
     data=mycur.fetchall()
     for i in data:
          print(i)
# To Count Number of Customer
def count():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("select count(*) from shop_management")
     data=mycur.fetchall()
     for i in data:
          print(i)
# To Delete The System
def dropdb():
     mydb=mysql.connect(host='localhost',user='root',password='mysql',database='cycleshop')
     mycur=mydb.cursor()
     mycur.execute("drop database cycleshop")
     print("\n\ndatabase dropped successfully")
# Main Menu
while True:
     print('<>'*30)
     print('\t\t\tWELCOME TO CYCLE SHOP MANAGEMENT PROGRAM')
     print('<>'*30)
     print('~'*50)
     print('Press 1 to Create Database')
     print('Press 2 to Display Database')
     print('Press 3 to Create Table')
     print('Press 4 to Show Tables in Database')
     print('Press 5 to Display the Structure of Table')
     print('Press 6 to Insert Data')
     print('Press 7 to Display Data')
     print('Press 8 to Search a Record Stored')
     print('Press 9 to Update a Record')
     print('Press 10 to Delete a Record')
     print('Press 11 to Add a Column(Address)')
     print('Press 12 to Add Primary Key')
     print('Press 13 to Drop a Column')
     print('Press 14 to Order by Bill Number')
     print('Press 15 to Group by Brand Type')
     print('Press 16 to Cout All Entries')
     print('Press 17 to Drop Database')
     print('Press 18 FOR EXIT!')
     print('~'*50)
     ch=int(input("ENTER YOUR CHOICE"))
     if ch==1:
          crdb()
     elif ch==2:
          showdb()
     elif ch==3:
          crtb()
     elif ch==4:
          showtb()
     elif ch==5:
          desc()
     elif ch==6:
          insert()
     elif ch==7:
          displaytb()
     elif ch==8:
          search()
     elif ch==9:
          update()
     elif ch==10:
          delete()
     elif ch==11:
          alteradd()
     elif ch==12:
          primary()
     elif ch==13:
          dropcolumn()
     elif ch==14:
          orderby()
     elif ch==15:
          groupby()
     elif ch==16:
          count()
     elif ch==17:
          dropdb()
     elif ch==18:
          break
     else:
          print("THANK YOU, HAVE A NICE DAY")
