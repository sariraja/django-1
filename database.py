import pymysql

connection = pymysql.connect(
    host='localhost',
    user='my_username',
    password='my_password',
    port= 0000,
    database='my_db')
columns = ['firstname VARCHAR(255)', 'lastname VARCHAR(255)','order_id', '']
sql = 'CREATE TABLE my_table (' + ', '.join(columns) + ');'
cursor = connection.cursor()
cursor.execute(sql)
