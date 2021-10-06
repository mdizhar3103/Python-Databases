# Object Relation Mapping 
"""
It is a programmable technique for converting data between 
in compatible type systems in object-oriented programming languages.

Table: Represents a table in the database
Mapper: Maps a python class to a table
Class: Object that defines how a record maps to an object
"""

# Original Classical Mapping
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper
import sqlalchemy as db

# creating connection
engine = db.create_engine('mysql+mysqlconnector://root:izhar@localhost:3306/sakila')

# creating metadata info about database
metadata = MetaData()

# defining table object
customers = Table(
    'customer', 
    metadata,
    Column('customer_id', Integer, primary_key=True),
    Column('store_id', Integer),
    Column('first_name', String),
    Column('last_name', String),
    Column('email', String),
    Column('address_id', Integer),
    Column('active', String),
    Column('create_date', DateTime),
    Column('last_update', DateTime),
)

# defining customer class
class Customers(object):

    def __init__(self, customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update):
        self.customer_id = customer_id
        self.store_id = store_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address_id = address_id
        self.active = active
        self.create_date = create_date
        self.last_update = last_update

# associating via mapper function
customers_mapper = mapper(Customers, customers)

# creating query
larger_address_id = customers.select(Customers.address_id > 15)
print(larger_address_id)

# fetching results
results = engine.execute(larger_address_id).fetchall()
print(results)