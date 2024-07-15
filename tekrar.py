import mysql.connector 
from connection import connection
from  datetime import datetime

class Student():
    connection=connection
    cursor=connection.cursor()

    def __init__(self,number,name,surname,birthdate,gender):
        self.number = number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender=gender

    def save(self):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)" 
        values=(self.number,self.name,self.surname,self.birthdate,self.gender)
        Student.cursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt başarıyla eklenmiştir")
            print(f"son eklenen kaydın id'si{Student.cursor.lastrowid}")        
        except mysql.connector.Error as err:
            print("hata :",err)     
        finally:
            Student.connection.close()



ahmet=Student(637,"mustafa","çalıkoğlu",datetime(2002,2,2),"E")
ahmet.save()
