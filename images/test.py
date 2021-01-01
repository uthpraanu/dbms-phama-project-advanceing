import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
curser = mydb.cursor()
        
query3 = "select name_id from log order by log_id desc limit 1"
curser.execute(query3)
rows1=curser.fetchall()
print(rows1)
print(rows1[0][0])