# Installed MySQL on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
print("JAI SHREE GANESH")
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'wArther17'
)

# prepare cursor object
cursorObject = dataBase.cursor()

# Create a DataBase 
cursorObject.execute("CREATE DATABASE SHIV_CRM_DB")

print("ALL DONE!!!")