import mysql.connector

def open_db_connection():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="KamilameląĄĄ",
    database="dekui"
    )

    if mydb.is_connected():
        print("Connected to MySQL database")
        
    return mydb


def close_db_connection(mydb):
    mydb.close()
    

mydb = open_db_connection()
    
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_give_item")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
close_db_connection(mydb)
