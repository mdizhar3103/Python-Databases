from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd",
    database="testdb",
)

cursor = myconn.cursor()

query = """
DELETE FROM users WHERE age >= 99
"""
print("deleting records")
cursor.execute(query)

myconn.commit()
cursor.close()
myconn.close()