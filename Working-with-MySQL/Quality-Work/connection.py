from mysql import connector as conn


config = {
    'host': "localhost",
    'user': "pythonuser",
    'password': "Passw0rd",
    'database': "sakila",
    'raise_on_warnings': True
}

# Normal approach:
print("Connection using Normal approach")
myconnection = conn.connect(**config)
print(myconnection)
myconnection.close()
input("Press Enter to Continue...\n")


# better approach: using try-except block
print("Connection using Try-except block")
try:
    myconnection = conn.connect(**config)
    print("Connection Succeeded...")
except conn.Error as e:
    print("Connection Failed with error: ", e)
else:
    print("Connection Closed!")
    myconnection.close()
input("Press Enter to Continue...\n")


# Using Context Manger
print("Using Context Manger")
with conn.connect(**config) as myconnection:
    print("Connection established successfully!")
    print("Connection Closed!")


print("Script Completed!")