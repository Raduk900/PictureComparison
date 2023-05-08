import mysql.connector
import database.database_connector as database_connector


  
def get_user_picture(item_id):
  
  mydb = database_connector.open_db_connection()
  
  sql = "SELECT PICTURE_URL FROM user_give_item WHERE ITEM_ID = %s"

  mycursor = mydb.cursor()
  mycursor.execute(sql, (item_id,))
  result = mycursor.fetchone()

  if not result:
    print("No picture URL found for ITEM_ID {}".format(item_id))
    
  print("PICTURE_URL: {}".format(result[0]))
  
  database_connector.close_db_connection(mydb)
  
  return result[0]
    
  
# check_user_code(123456)
# get_user_picture(1)