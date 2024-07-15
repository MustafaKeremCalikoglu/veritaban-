import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection=connection
    mycursor=connection.cursor()


    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname=surname
        self.birthdate = birthdate
        self.gender = gender


    def saveStudent(self):
        sql="INSERT INTO Student (studentNumber,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        values=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
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
    def students(liste):
        sql="INSERT INTO Student (studentNumber,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        values=(liste)
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt başarıyla eklenmiştir")
            print(f"son eklenen kaydın id : {Student.mycursor.lastrowid}")
        except mysql.connector.error as err:
            print("hata: ",err)
        finally:
            Student.connection.close()




# ahmet=Student(637,"malik","çalık",datetime(2002,5,17),"E")
# ahmet.saveStudent()

öğrenciler=[(16,"yunus","cellek",datetime(2008,5,2),"E"),
            (26,"metin","cellek",datetime(2006,5,2),"k")

]

Student.students(öğrenciler)


