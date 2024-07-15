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

    # cursor.execute("Select * From Products Order By name")
    # result=cursor.fetchall()

    # cursor.execute("Select * From Products Order By price") 
    # result=cursor.fetchall()
    
    
    # cursor.execute("Select * From Products Order By  price DESC")  #decreasing azalan demek
    # result=cursor.fetchall()

    cursor.execute("Select * From Products Order By price DESC,name")  

    try:
        result=cursor.fetchall()
    except :
        print("hata var")
    for i in result:
        print(f"id : {i[0]} , name : {i[1]} , price : {i[2]} , description : {i[4]}")

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


getproductsInfo()
