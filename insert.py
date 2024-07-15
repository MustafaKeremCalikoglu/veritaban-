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



liste=[]
while True:

    name=int(input("öğrenci numaranızı giriniz"))
    price=float(input("isim : "))
    image=input("soyisim : ")
    description=input("doğum tarihi  : ")


    liste.append((name,price,image,description))
    exit=input("çıkmak istiyomusunuz :e/h")
    if exit =="e":
        print("kayıtlarınız tamamlanıyor...")
        insertproducts(liste)       
        break
    