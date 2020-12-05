import json
import sqlite3

conn = sqlite3.connect('test.db')
x ={"name":"dravid", "age":18, "city":"chennai" , "gender":"male" , "height":5.8,"weight":49.5,"address":{"city":"chennai","pin code":600092},"graduation in following schools":["PSM","chimya vidyalaya","velammal"],"graduation in following years":(2017,2019),"pass in 1st attempt":True,"black marks in graaduation":False,"arrears":None}

# convert into JSON:
y = json.dumps(x)

print(y)
sql = "insert into GRADUATIONDATA (DETAIL) values ('" "+y+" "') "
conn.execute(sql);

cursor = conn.execute("SELECT DETAIL from BIODATA")
for row in cursor:
   print ("json = ", row[0])


conn.close()


