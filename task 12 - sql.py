import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

conn.execute('''CREATE TABLE BIODATA
               (DETAIL CHAR(100));''')
         
print ("Table created successfully");

conn.close()
