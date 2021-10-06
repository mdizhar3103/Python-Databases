import datetime
import mysql.connector
from mysql.connector import errorcode


config = {
    'host': "localhost",
    'user': "pythonuser",
    'password': "Passw0rd",
    'database': "employees",
    'raise_on_warnings': True
}


def establish_connection():
    try:
        with mysql.connector.connect(**config) as myconnection:
            print("Connection established successfully!")
            cursor = myconnection.cursor()
            select_query(cursor)
            basic_select(cursor)
            cursor.close()
            print("Connection Closed!")

    except mysql.connector.Error as err:
        print("Connection Failed!")
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def select_query(cursor):
    query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE hire_date BETWEEN %s AND %s")

    hire_start = datetime.date(1999, 1, 1)
    hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query, (hire_start, hire_end))

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))


def basic_select(cursor):
    print("Running basic_select statement...\n")
    query = ("SELECT * FROM employees")
    cursor.execute(query)
    print(cursor.fetchall())


if __name__ == '__main__':
    establish_connection()
    