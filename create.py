#!/usr/bin/python

import sqlite3



conn = sqlite3.connect('test.db')  #create a table in our database
print "Opened database successfully"

conn.execute('''CREATE TABLE XTREAMING
       (ID INT PRIMARY KEY    AUTOINCREMENT,
       USERNAME          CHAR(25)    NOT NULL,
       PASSWORD          CHAR(25)    NOT NULL,);''')
print "Table created successfully"

conn.close()


conn = sqlite3.connect('test.db')  #insert operation
print "Opened database successfully"

conn.execute("INSERT INTO XTREAMING (ID,USERNAME, PASSWORD) \
      VALUES (1, 'Alvaro', 'Alvaro1)")

conn.execute("INSERT INTO XTREAMING (ID,USERNAME, PASSWORD) \
      VALUES (2,  'Pedro', 'Pedro2')")

conn.execute("INSERT INTO XTREAMING (ID,USERNAME, PASSWORD) \
      VALUES (3, 'Hector', 'Hector3')")

conn.execute("INSERT INTO XTREAMING (ID,USERNAME, PASSWORD) \
      VALUES (4, 'Ivan', 'Ivan4')")

conn.commit()
print "Records created successfully"
conn.close()



conn = sqlite3.connect('test.db')
print "Opened database successfully"

cursor = conn.execute("SELECT ID, USERNAME, PASSWORD FROM XTREAMING")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully"
conn.close()
