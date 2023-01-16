import sqlite3
import os

if not os.path.exists("McDonalds.db"):
   with open("CreateDbMcDonalds.py", 'r') as CreateDB:
    exec(CreateDB.read())
   

db = sqlite3.connect('McDonalds.db')
c = db.cursor()

tblForInsert = input("Which table would you like to insert data into?  Customers or Orders?")

if tblForInsert == "Customers":
   CustomerID = input("CustomerID: ")
   Forename = input("Customer Forename: ")
   Surname = input("Customer Surname: ")
   EmailAddress = input("Customer Email: ")


   sql = """INSERT or REPLACE INTO Customers
         (CustomerID, Forename, Surname, EmailAddress)
          VALUES ('{}','{}','{}','{}');""".format(
          CustomerID, Forename, Surname, EmailAddress)

   cursor = db.cursor()
   cursor.execute(sql)
   db.commit()
   cursor.close()


if tblForInsert == "Orders":
   OrderID = input("OrderID: ")
   Meal = input("Meal?: ")
   TimeUntillReady = input("Time Untill Cooked?: ")


   sql = """INSERT or REPLACE INTO Orders
         (OrderID, Meal, TimeUntillReady)
          VALUES ('{}','{}','{}');""".format(
          OrderID, Meal, TimeUntillReady)

   cursor = db.cursor()
   cursor.execute(sql)
   db.commit()
   cursor.close()












