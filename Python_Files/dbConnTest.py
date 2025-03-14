import mysql.connector

conn = mysql.connector.connect (
    host="localhost",
    user="cst8277",
    password="8277",
    database="pythondb"
    )

# Check if connection was successful
if conn.is_connected():
    print("Successfully connected to MySQL!")

# Don't forget to close the connection when done
conn.close()