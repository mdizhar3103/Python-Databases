from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd",
    database="testdb",
)

cursor = myconn.cursor()

query = "SELECT * FROM users"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)


# fetching one row (run by commeting above query statements)
print("Fetching single row")
query = "SELECT first_name, last_name FROM users"
cursor.execute(query)

result = cursor.fetchone()

for row in result:
    print(row)

cursor.close()
myconn.close()