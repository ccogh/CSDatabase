import sqlite3
import os

if not os.path.exists("McDonalds.db"):
   with open("CreateDbMcDonalds.py", 'r') as CreateDB:
    exec(CreateDB.read())
   

db = sqlite3.connect('McDonalds.db')
c = db.cursor()

manipulationFunction = input("Insert, Delete, or Edit?")

if manipulationFunction == "Insert":
   with open("InsertFunction.py", "r") as file:
      exec(file.read())
