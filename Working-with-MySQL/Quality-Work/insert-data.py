from __future__ import print_function
from datetime import date, datetime, timedelta
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
            insert_data(cursor)
            # Make sure data is committed to the database
            myconnection.commit()
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


def insert_data(cursor):
    print("Inserting Data in tables...")
    tomorrow = datetime.now().date() + timedelta(days=1)

    add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")
    add_salary = ("INSERT INTO salaries "
                "(emp_no, salary, from_date, to_date) "
                "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    # Insert new employee
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid

    # Insert salary information
    data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
    }
    cursor.execute(add_salary, data_salary)
    print("Insertion Completed!\n")


if __name__ == '__main__':
    establish_connection()
    
