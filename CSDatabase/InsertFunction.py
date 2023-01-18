import sqlite3
db = sqlite3.connect('McDonalds.db')



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
      db.close()


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
      db.close()

if tblForInsert == "Items":
      ItemID = input("ItemID: ")
      ItemName = input("Name: ")


      sql = """INSERT or REPLACE INTO Items
         (ItemID, ItemName)
          VALUES ('{}','{}');""".format(
          ItemID, ItemName)

      cursor = db.cursor()
      cursor.execute(sql)
      db.commit()
      cursor.close()
      db.close()