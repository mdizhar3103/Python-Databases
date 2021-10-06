from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd"
)

cursor = myconn.cursor()

# create databases
query = "CREATE DATABASE testdb"
cursor.execute(query)

# list databases
query = "SHOW DATABASES"
cursor.execute(query)

for db in cursor:
    print(db)
