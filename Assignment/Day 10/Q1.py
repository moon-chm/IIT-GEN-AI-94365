import mysql.connector
host ='Localhost'
user='root'
password='root'
user='root'
database='emp'
try:
    conn=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connection To MYSQL")

    cursor=conn.cursor()
    cursor.execute("show tables")
    tables=cursor.fetchall()
    print('Table in database : ',tables)

    cursor.execute("SELECT *FROM employees  LIMIT 5")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
    print("Connection closed")     
except mysql.connector.Error as err:
    print("Error : ",err)
