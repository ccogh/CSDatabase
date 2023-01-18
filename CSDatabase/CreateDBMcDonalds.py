import sqlite3

db = sqlite3.connect('McDonalds.db')
c = db.cursor()

db.execute('''
          CREATE TABLE IF NOT EXISTS Customers
          ([CustomerID] INTEGER PRIMARY KEY, 
           [Forename] TEXT, 
           [Surname] TEXT,
           [EmailAddress] CHAR(30),
           [OrderID] Integer)
          ''')
db.execute('''
          CREATE TABLE IF NOT EXISTS Orders
          ([OrderID] INTEGER PRIMARY KEY, 
           [Meal] INTEGER, 
           [TimeUntillReady] INTEGER)
          ''')
db.execute('''
          CREATE TABLE IF NOT EXISTS Items
          ([ItemID] INTEGER PRIMARY KEY,
           [ItemName] INTEGER)
          ''')

db.commit()

