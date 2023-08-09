# Installed MySQL on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
print("JAI SHREE GANESH")
import mysql.connector

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wArther17",
}

dataBase = mysql.connector.connect(**config)

# prepare cursor object
cursorObject = dataBase.cursor()

# Create a DataBase 
cursorObject.execute("CREATE DATABASE SHIV_CRM_DB")

print("ALL DONE!!!")