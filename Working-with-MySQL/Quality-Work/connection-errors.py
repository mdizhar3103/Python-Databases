from mysql import connector as conn
from mysql.connector import errorcode


config = {
    'host': "localhost",
    'user': "pythonuser",
    'password': "Password",
    'database': "skills",
    'raise_on_warnings': True
}

# better approach: using try-except block
print("Connection using Try-except block".center(50))
try:
    myconnection = conn.connect(**config)
    print("Connection Succeeded...")
except conn.Error as err:
    print("Connection Failed!")
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection Closed!")
    myconnection.close()
input("Press Enter to Continue...\n")


# Using Combination of Try-except and Context Manger
print("Connection using Combination of Try-except and Context Manger".center(50))

try:
    with conn.connect(**config) as myconnection:
        print("Connection established successfully!")
        print("Connection Closed!")
except conn.Error as err:
    print("Connection Failed!")
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
input("Press Enter to Continue...\n")


# Using Context Manager
print("Using Context Manager".center(50))
with conn.connect(**config) as myconnection:
    print("Connection established successfully!")
    print("Connection Closed!")

print("Script Completed!")