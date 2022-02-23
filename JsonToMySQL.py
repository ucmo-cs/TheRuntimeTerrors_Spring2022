#run this in cmd pip install mysql-connector-python
import mysql.connector
import json

conn = mysql.connector.connect(user='root', password='root',
                               host='localhost', database='risk')

if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")


