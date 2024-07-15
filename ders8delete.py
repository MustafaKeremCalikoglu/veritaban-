import mysql.connector
from numpy import append

def insertproduct(name,price,image,description):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,image,description) VALUES(%s,%s,%s,%s)"
    values=(name,price,image,description)
    cursor.execute(sql,values)
    
    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.error as err:
        print("hata",err)

    finally:
        connection.close()
        print("database bağlantısıs kapandı")


def insertproducts(list):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,image,description) VALUES(%s,%s,%s,%s)"
    values=list
    cursor.executemany(sql,values)
    
    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.error as err:
        print("hata",err)

    finally:
        connection.close()
        print("database bağlantısıs kapandı")


def getproducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()

    sql="Select * From products inner join categories on categories.id=products.categoryid"
    sql="Select products.name,products.price,products.description,categories.name From products inner join categories on categories.id=products.categoryid"
    sql="Select p.name,p.price,p.description,c.name From products as p inner join categories as c on c.id=p.categoryid"



    cursor.execute(sql)  

    try:
        result=cursor.fetchall()
        for i in result:
            print(i)
    except :
        print("hata var")
   

def getproductsId(Id):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()
    sql=f"Select * from Products where id={Id} "
    

    cursor.execute(sql)
    i=cursor.fetchall()

    
    print(i) 

def getproductsInfo():
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()
    # sql="Select COUNT(*) From Products" #satır sayısı
    # sql="Select AVG(price) From Products"  # ortalama
    # sql="Select SUM(price) From Products"  # ortalama
    # sql="Select MAX(price) From Products"  
    sql="Select name From Products where price= (Select MAX(price) From Products)" 
    
    cursor.execute(sql)
    try:
        result=cursor.fetchone()

        print(result[0])
    except:
        print("hata")




def updateProducts(id,name,price):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()

    # sql="Update products Set name='samsungs10' ,price=3000 where id=3  "
    # cursor.execute(sql)
    sql="Update products Set name=%s ,price=%s where id=%s  "
    values=(name,price,id)
    cursor.execute(sql,values)

    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi")
       
    except mysql.connector.error as err:
        print("hata",err)

    finally:
        connection.close()
        print("database bağlantısıs kapandı")


def deleteProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()

    sql="delete from products where id=4  " 
    cursor.execute(sql)

    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
       
    except mysql.connector.error as err:
        print("hata",err)

    finally:
        connection.close()
        print("database bağlantısı kapandı")



getproducts()

