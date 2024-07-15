import mysql.connector
from datetime import datetime
from connection import connection



class Student:
    connection=connection
    mycursor=connection.cursor()
    
    def __init__(self,studentNumber,name,surname,birtdate,gender):
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birtdate=birtdate
        self.gender=gender
    
    def saveStudent(self):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values=(self.studentNumber,self.name,self.surname,self.birtdate,self.gender)
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt başarıyla eklenmiştir")
            print(f"son eklenen kaydın id : {Student.mycursor.lastrowid}")
        except mysql.connector.error as err:
            print("hata: ",err)
        finally:
            Student.connection.close() 
   




ahmet=Student(106,"ali","yılmaz",datetime(2005,6,17),"E")
ahmet.saveStudent()



# def insertproducts(list):
#     cursor=connection.cursor()
#     sql="INSERT INTO student(StudentNumber,Name,Surname,Birtdate,Gender) VALUES(%s,%s,%s,%s,%s)"
#     values=list
#     cursor.executemany(sql,values)

#     try:
#         connection.commit()
#         print(f"{cursor.rowcount} tane kayıt başarıyla eklenmiştir")
#         print(f"son eklenen kaydın id : {cursor.lastrowid}")
#     except mysql.connector.error as err:
#         print("hata: ",err)
#     finally:
#         connection.close() 


