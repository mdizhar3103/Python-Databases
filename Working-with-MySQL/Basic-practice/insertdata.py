from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd",
    database="testdb",
)

cursor = myconn.cursor()

query = """
INSERT INTO users(first_name, last_name, email, age) 
VALUES (%s, %s, %s, %s) 
"""

data = ('Mohd', 'Izhar', 'izhar@gmail.com', '22')

print("inserting single row")
cursor.execute(query, data)

# Inserting mulitple records
print("Inserting many records")

records = [
    ('Tridib', 'Mondol', 'mondol@gmail.com', '21'),
    ('Arpit', 'Singh', 'arpit@gmail.com', '22'),
    ('Waqar', 'Ahmad', 'waqar@gmail.com', '21'),
]

# execute many
cursor.executemany(query, records)

myconn.commit()
cursor.close()
myconn.close()