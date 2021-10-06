from mysql import connector as conn

myconn = conn.connect(
    host="localhost",
    user="pythonuser",
    password="Passw0rd",
    database="testdb",
)

cursor = myconn.cursor()

# creating table
query = """
CREATE TABLE `users`(
    `first_name` VARCHAR(255), 
    `last_name` VARCHAR(255),
    `email` VARCHAR(255),
    `age` INTEGER,
    `user_id` INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL)
"""
cursor.execute(query)

cursor.execute("SHOW TABLES")
for tables in cursor:
    print(tables)

cursor.close()
myconn.close()