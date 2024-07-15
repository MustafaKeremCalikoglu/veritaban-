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
    # cursor.execute("Select * From Products")
    
   
    
    # result=cursor.fetchall()
    # print(result)
    # for i in result:
    #     print(i)

    # for i in result:
    #     print(f"name : {i[1]} price: {i[2]}")


    cursor.execute("Select name,price From Products")
    result=cursor.fetchall() # fetchall tüm kaydı getitir fetchone ilk kaydı getirir
    
    for i in result:
        print(f"name : {i[0]} price: {i[1]}")

getproducts()
