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
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node-app")
    cursor=connection.cursor()

    sql="Select name,price from products"
    cursor.execute(sql)

    result=cursor.fetchall()
   
    for i in result:
        print(i)

def select():
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node-app")
    cursor=connection.cursor()

    cursor.execute("Select * From products ")


    result=cursor.fetchall()
    for i in result:
        print(i)

def update(name,id):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node-app")
    cursor=connection.cursor()

    sql="update products SET name=%s  where id= %s"
    values=(name,id)

    cursor.execute(sql,values)

    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi")
    except mysql.connector.error as err:
        print("hata",err)

    finally:
        connection.close()
        print("database bağlantısıs kapandı")
    





select()
