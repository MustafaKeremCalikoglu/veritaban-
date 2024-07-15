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

#peace of cake = çocok oyuncağı

def getproducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()



    # cursor.execute("Select * From Products where id=1 ")
    # result=cursor.fetchall() # fetchall tüm kaydı getitir fetchone ilk kaydı getirir

    # cursor.execute("Select * From Products where id>1 ")
    # result=cursor.fetchall() 

    # cursor.execute("Select * From Products where name='samsungc7' and price=2700")
    # result=cursor.fetchall() 

    # cursor.execute("Select * From Products where name='samsungc7' or price=2700")
    # result=cursor.fetchall() 

    # cursor.execute("Select * From Products where name LIKE '%samsung%'")
    # result=cursor.fetchall() 

    # cursor.execute("Select * From Products where name LIKE 'samsun%'")
    # result=cursor.fetchall() 

    cursor.execute("Select * From Products where name LIKE '%kia'")
    result=cursor.fetchall() 

    for i in result:
        print(f"id : {i[0]} , name : {i[1]} , price : {i[2]} , description : {i[4]}")

def getproductsId(Id):
    connection=mysql.connector.connect(host="localhost",user="root",password="41abd271",database="node_app")
    cursor=connection.cursor()
    sql=f"Select * from Products where id={Id} "
    

    cursor.execute(sql)
    i=cursor.fetchall()

    
    print(i) 




getproductsId(1)
