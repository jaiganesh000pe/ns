
import sqlite3
conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (pid INTEGER PRIMARY KEY ,name TEXT, addr TEXT, city TEXT, pin TEXT, esaf TEXT,esaf1 TEXT,home TEXT,ebbill TEXT,milk TEXT,petrol TEXT,gramiya TEXT,jaya TEXT,valar TEXT,sur TEXT,sama TEXT,suth TEXT,non TEXT,mob TEXT,fes TEXT,tra TEXT,gym TEXT,food TEXT,frd1 TEXT,elone TEXT,to_lone TEXT,to_home TEXT,all_totel TEXT,to_ TEXT)')
print ("Table created successfully")
conn.close()
