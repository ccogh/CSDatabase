import sqlite3

db = sqlite3.connect('McDonalds.db')
c = db.cursor()

db.execute('''
          CREATE TABLE IF NOT EXISTS Customers
          ([CustomerID] INTEGER PRIMARY KEY, 
           [Forename] TEXT, 
           [Surname] TEXT,
           [EmailAddress] CHAR(30))
          ''')
db.execute('''
          CREATE TABLE IF NOT EXISTS Orders
          ([OrderID] INTEGER PRIMARY KEY, 
           [Meal] INTEGER, 
           [TimeUntillReady] INTEGER,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID))
          ''')
db.execute('''
          CREATE TABLE IF NOT EXISTS Items
          ([ItemID] INTEGER PRIMARY KEY,
           [ItemName] TEXT)
          ''')

db.commit()

