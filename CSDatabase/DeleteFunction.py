import sqlite3

def delete_product(data):
    input(data)
    with sqlite3.connect("McDonalds.db") as db:
        cursor = db.cursor()
        sql ='delete from Customers where CustomerID = ? '
        cursor.execute(sql,data)
        db.commit() 
