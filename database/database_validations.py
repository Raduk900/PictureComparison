import mysql.connector
import database_connector


def check_user_code(code):

  mydb = database_connector.open_db_connection()

  if mydb.is_connected():
      print("Connected to MySQL database")
          
  sql = "SELECT USER_ID, BOX_ID FROM user_take_item WHERE CODE = %s"

  mycursor = mydb.cursor()
  mycursor.execute(sql, (code,))
  results = mycursor.fetchall()

  if len(results) == 0:
    print("No user found with CODE {}".format(code))
    mydb.close()
    exit()
    
  for result in results:
    print("USER_ID: {}, BOX_ID: {}".format(result[0], result[1]))

  database_connector.close_db_connection(mydb)
  
def get_user_email(item_id):
  
  mydb = database_connector.open_db_connection()
  
  sql = "SELECT PICTURE_URL FROM user_give_item WHERE ITEM_ID = %s"

  mycursor = mydb.cursor()
  mycursor.execute(sql, (item_id,))
  result = mycursor.fetchone()

  if not result:
    print("No picture URL found for ITEM_ID {}".format(item_id))
    
    exit()

  print("PICTURE_URL: {}".format(result[0]))
  
  database_connector.close_db_connection(mydb)
    
  
check_user_code(123456)
get_user_email(1)