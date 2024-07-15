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
    @staticmethod
    def tumkayit():
        Student.mycursor.execute("Select * From student")
        result=Student.mycursor.fetchall()
        for i in result:
            print(f"name:{i[2]},surname:{i[3]},birthday:{i[4]},gender:{i[5]} ")
    
    @staticmethod
    def ortakayit():
        Student.mycursor.execute("Select StudentNumber,Name,Surname From student")
        result=Student.mycursor.fetchall()
        for i in result:
            print(i)
    @staticmethod
    def kizkayit():
        Student.mycursor.execute("Select * From student where Name LIKE '%ah%' or Surname LIKE'%ah%' ")
        result=Student.mycursor.fetchall()
        for i in result:
            print(i)
    @staticmethod
    def dogumkayit():
        Student.mycursor.execute("Select * From student where YEAR(Birthdate)=2005 ")
        result=Student.mycursor.fetchall()
        for i in result:
            print(i)
    @staticmethod
    def erkeksayi():
        Student.mycursor.execute("Select COUNT(Name) From student where Gender='E'  ")
        result=Student.mycursor.fetchone()
        print(result[0])
    @staticmethod
    def siralama():
        Student.mycursor.execute("Select * From student where Gender='k' Order By Name ")
        result=Student.mycursor.fetchall()
        print(result)

Student.siralama()





