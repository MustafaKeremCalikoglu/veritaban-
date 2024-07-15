import mysql.connector

mydb=mysql.connector.connect( 
    host="localhost" ,
    user="root" ,
    password="41abd271",
    database="mydatabase"
    )

mycursor=mydb.cursor()



#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")

#for i in mycursor:
#    print(i)    

mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")