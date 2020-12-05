

import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

conn.execute('''CREATE TABLE GRADUATIONDATA
               (DETAIL CHAR(10000));''')
         
print ("Table created successfully");

conn.close()
