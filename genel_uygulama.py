import mysql.connector
from datetime import datetime
from connection2 import connection

class Okuldb():
    connection=connection
    mycursor=connection.cursor()

    def __init__(self,isim,soyisim,numara,dogumtarihi,cinsiyet):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.dogumtarihi=dogumtarihi
        self.cinsiyet=cinsiyet

    def ogrenci_kayit(self):
        sql="INSERT INTO ogrenci(isim,soyisim,numara,dogumtarihi,cinsiyet) VALUES (%s,%s,%s,%s,%s)"
        values=(self.isim,self.soyisim,self.numara,self.dogumtarihi,self.cinsiyet)
        Okuldb.mycursor.execute(sql,values)

        try:
            Okuldb.connection.commit()
            print(f"{Okuldb.mycursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kişinin id'si {Okuldb.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata",err)
        
    @staticmethod
    def ogrenciler_kayit(liste):
        sql="INSERT INTO ogrenci(isim,soyisim,numara,dogumtarihi,cinsiyet) VALUES (%s,%s,%s,%s,%s)"
        values=liste
        Okuldb.mycursor.executemany(sql,values)

        try:
            Okuldb.connection.commit()
            print(f"{Okuldb.mycursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kişinin id'si {Okuldb.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata",err)    
    @staticmethod
    def kayıt_goster():
        sql="Select * from ogrenci"
        Okuldb.mycursor.execute(sql)
        result = Okuldb.mycursor.fetchall()
        for i in result:
            print(i)

    @staticmethod
    def getproducts(name):
    



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

        sql="Select * From ogrenci where isim LIKE %s"
        values=('%'+name+'%',)
        Okuldb.mycursor.execute(sql,values)
        result=Okuldb.mycursor.fetchall() 

        for i in result:
            print(i)

x=input("")
Okuldb.getproducts(x)


toplam=[]
while True:
    name=input("isim giriniz: ")
    surname=input("soyisim giriniz: ")
    number=int(input("numaranızı giriniz: "))
    birthdate=input("doğum tarihinizi yıl ay gün olarak aralarında bir boşluk olacak şekilde giriniz:  ")
    liste=birthdate.split()
    gender=input("cinsiyetinizi giriniz K/E :  ")

    toplam.append((name,surname,number,datetime(int(liste[0]),int(liste[1]),int(liste[2])),gender))
    Okuldb.ogrenciler_kayit(toplam)

    devam=input("çıkmak için Ç kalmak içim K basınız ")

    if devam=="Ç" or devam=="ç" :
        Okuldb.kayıt_goster()
        break
    

