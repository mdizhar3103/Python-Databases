from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd",
    database="testdb",
)

cursor = myconn.cursor()

query = """
UPDATE users SET age = 23 WHERE first_name = 'Mohd' AND last_name = 'Izhar'
"""
print("updating records")
cursor.execute(query)
# Note: performing update with non unique columns will update 
# multiple rrcords of same match
# Always perform update with primary key column

myconn.commit()
cursor.close()
myconn.close()