import mysql.connector
import database.database_connector as database_connector
# import database_connector

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
    return 0

  print("test: ", results[0][1])

  return results[0][1]

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

def get_item_unique_code_give_item(item_id):

  mydb = database_connector.open_db_connection()

  sql = "SELECT UNIQUE_CODE FROM user_give_item WHERE ITEM_ID = %s"

  mycursor = mydb.cursor()
  mycursor.execute(sql, (item_id,))
  result = mycursor.fetchone()

  if not result:
    print("No unique code found for ITEM_ID {}".format(item_id))

  print("Unique code: {}".format(result[0]))

  database_connector.close_db_connection(mydb)

  return result[0]

def get_item_unique_code_take_item(code):

  mydb = database_connector.open_db_connection()

  sql = "SELECT UNIQUE_CODE FROM user_take_item WHERE CODE = %s"

  mycursor = mydb.cursor()
  mycursor.execute(sql, (code,))
  result = mycursor.fetchone()

  if not result:
    print("No unique code found for CODE {}".format(code))

  print("Unique code: {}".format(result[0]))

  database_connector.close_db_connection(mydb)

  return result[0]

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

def add_to_user_take_item():
    mydb = database_connector.open_db_connection()

    user_id = get_next_highest_id(mydb, "USER_ID", "user_take_item")

    box_id = get_next_highest_id(mydb, "BOX_ID", "user_take_item")

    sql = "INSERT INTO user_take_item (USER_ID, BOX_ID) VALUES (%s, %s)"
    values = (user_id, box_id)

    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    mydb.commit()

    print("Added new row to user_take_item: USER_ID = {}, BOX_ID = {}".format(user_id, box_id))

    database_connector.close_db_connection(mydb)

def get_next_highest_id(mydb, column, table):
    sql = "SELECT MAX({}) FROM {}".format(column, table)

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchone()

    if result[0] is not None:
        next_highest_id = result[0] + 1
    else:
        next_highest_id = 1

    return next_highest_id

def delete_user_by_code(code):
    mydb = database_connector.open_db_connection()

    sql = "DELETE FROM user_take_item WHERE CODE = %s"
    values = (code,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    mydb.commit()

    deleted_rows = mycursor.rowcount
    print("Deleted {} row(s) from user_take_item".format(deleted_rows))

    database_connector.close_db_connection(mydb)

def add_item_to_user(member_id, unique_code, photo_url, uniqueCode):
    mydb = database_connector.open_db_connection()

    sql = "INSERT INTO user_give_item (USER_ID, UNIQUE_CODE, PICTURE_URL, ITEM_ID) VALUES (%s, %s, %s, %s)"
    values = (member_id, unique_code, photo_url, uniqueCode)

    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    mydb.commit()

    print("Row added to user_add_item")

    database_connector.close_db_connection(mydb)

def take_item_to_user(member_id, unique_code, photo_url, uniqueCode):
    mydb = database_connector.open_db_connection()

    sql = "INSERT INTO user_take_item (USER_ID, BOX_ID, CODE, UNIQUE_CODE) VALUES (%s, %s, %s, %s)"
    values = (member_id, unique_code, uniqueCode, photo_url)

    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    mydb.commit()

    print("Row added to user_add_item")

    database_connector.close_db_connection(mydb)

