import json
import sqlite3

conn = sqlite3.connect('test.db')
x ='{ "name":"dravid", "age":18, "city":"chennai" , "gender":"male" , "height":"5.8"}'

# parse x:
y = json.loads(x)

# convert into JSON:
y = json.dumps(x)

print(y)
sql = "insert into BIODATA (DETAIL) values ('" + y + "') "
conn.execute(sql);

cursor = conn.execute("SELECT DETAIL from BIODATA")
for row in cursor:
   print ("json = ", row[0])


conn.close()
