# Declarative (Better approach than querying_sqlalchemy.py)

"""
ORM
- Typically used system
- Define classes
- Mapped to relational database tables
- Series of extensions
    - on top of the mapper construct

Session: Core concepts of SQLAlchemy
    - Establishes and maintains conversations
    - Between our program and the database
    - Entry point for queries
"""

# we need session first

from querying_sqlalchemy import Customers, customers, customers_mapper
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

# creating connection
engine = db.create_engine('mysql+mysqlconnector://root:izhar@localhost:3306/sakila')

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

# get list of Customers
my_session.query(Customers).all()

# total count
print("================ Total Count ===================")
print(len(my_session.query(Customers).all()))

# get the first row
print("=============== First Row ===================")
print(my_session.query(Customers).first())

# accession specific columns
print("================ Accession Specific Columns =================")
print(my_session.query(Customers.customer_id, Customers.first_name).first())

# #########################################################################
# 
# This is little bit hard to understand lets do it using Declarative API
# Declarative Base: (Base class for declarative class definations)
#   - Define Models
#   - Connect them to the database
# #########################################################################

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# defining Model
class Actor(Base):
    __tablename__ = 'actor'
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return """
        <{0} actor_id: {1} - first_name: {2}>
        """.format(self.__class__.__name__, self.actor_id, self.first_name)


print("====== Declarative API Output ========")
print(my_session.query(Actor).first())

# accession field using Declarative API
print(my_session.query(Actor).first().last_name)

# iterating over the results
for each_actor in my_session.query(Actor):
    print(each_actor)

# print the actual query
the_query = my_session.query(Actor)
print(the_query)
print("type of query is :", type(the_query))

# Use echo = True in create_engine to get each created query output syntax

# filtering results
print("===== Using filter by function ======")
print(my_session.query(Actor).filter_by(last_name="NOLTE").all())

# using filter function explicit is better than implicit
print("===== Using filter function ======")
print(my_session.query(Actor).filter(Actor.last_name=="NOLTE").all())

# using like function
print("===== Using Like function ======")
print(my_session.query(Actor).filter(Actor.last_name.like("J%")).all())

# using contains function
print("===== Using Contain function ======")
print(my_session.query(Actor).filter(Actor.last_name.contains("J")).all())


# Many fuctions available in func

from sqlalchemy import func

# func is function generator
print("======== (func) dir ====")
print(dir(func))

# using count function
print("======== Using func.count ====")
print(my_session.query(func.count(Actor.actor_id)).scalar())

# print(my_session.query(func.count(Actor.actor_id)).all()) # return in list form counts with tuples 

# Using operators and Labels
print("\n==== Using label function ====\n")
print(my_session.query(Actor.actor_id,
db.cast((Actor.first_name + " " + Actor.last_name), 
db.String(30)).label("full_name"), 
 Actor.first_name, Actor.last_name).all())

#  limiting the results
print("\n==== Using limit function ====")
print(my_session.query(Actor.actor_id,
db.cast((Actor.first_name + " " + Actor.last_name), 
db.String(30)).label("full_name"), 
 Actor.first_name, Actor.last_name).limit(5).all())

# ####################################################
# 
#           Using Joins
# 
# ####################################################

class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = db.Column(db.Integer(), primary_key=True)
    film_id = db.Column(db.Integer(), primary_key=True)
    last_update = db.Column(db.DateTime)


# implicit join
print("===============Implicit Join ============")
print(my_session.query(Actor, FilmActor).filter(Actor.actor_id == FilmActor.actor_id).first())

# explicit join
print("===============Explicit Join ============")
print(my_session.query(Actor, FilmActor).join(FilmActor ,Actor.actor_id == FilmActor.actor_id).first())

# Refer to doc for Heirarichal Table
