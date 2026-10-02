import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="Healthcare",
    password="hsvhxx944511",
    database="Healthcare_ai"
)

print("Database connection successful!")

connection.close()




