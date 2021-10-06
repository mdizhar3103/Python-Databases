import sqlalchemy as db
from sqlalchemy import MetaData

# creating engine
engine = db.create_engine("mysql+mysqlconnector://root:izhar@localhost:3306", echo=True)
connect = engine.connect()

# creating database
try:
    query = "CREATE DATABASE test_mysql_sa;"
    engine.execute(query)
except Exception as e:
    print("Database Already Exist MySQL")

# creating SQLite Databases
engine = db.create_engine("sqlite:///new_sqlite.db")
connection = engine.connect()

# creating Tables
engine = db.create_engine("mysql+mysqlconnector://root:izhar@localhost:3306/test_mysql_sa", echo=True)
connect = engine.connect()

metadata = MetaData()
posts = db.Table(
    'posts', metadata,
    db.Column('Id', db.Integer()),
    db.Column('Title', db.String(255)),
    db.Column('ViewCount', db.Integer()),
    db.Column('IsQuestion', db.Boolean()),
)
# this will create all tables
metadata.create_all(engine)

print("Accessing Database: ",posts)
print("Accessing Column: ", posts.c)
print(dir(posts))

# specifying primary keys, nullable, unique
posts_two = db.Table(
    'posts_two', metadata,
    db.Column('Id', db.Integer(), primary_key=True, unique=True),
    db.Column('Title', db.String(255), nullable=False),
    db.Column('ViewCount', db.Integer(), default=1000),
    db.Column('IsQuestion', db.Boolean(), default=True),
)

# using different method to create tables 
try:
    posts_two.create(engine)
except Exception as e:
    print("Table already exists")

########################################################
#
# Creating Using Declarative API
#
########################################################
print("Using Declarative API\n")

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = db.create_engine("sqlite:///sqlalchemy_sqlite.db", echo=True)
connection = engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String())


class Post(Base):
    __tablename__ = "post"
    Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer(), default=1000)
    Question = db.Column(db.Boolean(), default=True)

    # defining foreign constraints
    OwnerUserId = db.Column(
        db.Integer(), 
        db.schema.ForeignKey('user.Id'), 
        nullable=False)

    # Defining relationship
    User = relationship('User', backref="post")

# creating table now
Base.metadata.create_all(engine)

# accession the database
# >>> sqlite3 sqlalchemy_sqlite.db
# >>> .tables        // to list tables
# >>> .schema post   // to see table schema

# #############################################################
# 
#                       Inserting Data
# 
# #############################################################

print("========= Inserting data ==========")
engine = db.create_engine(
    "sqlite:///sqlalchemy_sqlite.db"
)
connection = engine.connect()
metadata = db.MetaData()

# creating table object
users = db.Table(
    'user', 
    metadata, 
    autoload=True,
    autoload_with = engine)

# using insert
stmt = db.insert(users).values(Name="Mohd Izhar")
result = connection.execute(stmt)
print(result.rowcount)

###########################
# Inserting Using Session #
###########################

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

# inserting data now
tridib = User(Name="Tridib")
abhinav = User(Name="Abhinav")

my_session.add(tridib)
my_session.add(abhinav)
my_session.new
my_session.commit()

for each_user in my_session.query(User).all():
    print(each_user.Name)

# inserting multple records
print("inserting multiple records")
posts = db.Table(
    'post', 
    metadata, 
    autoload = True,
    autoload_with = engine)

stmt = db.insert(posts)
values_list = [{'Title': 'Data Science Questions', 'OwnerUserId': 1},
{'Title': 'BigData Questions', 'OwnerUserId': 2}]
result = connection.execute(stmt, values_list)

# check the data in database

# performing operations for defaults
one_post = Post(Title="Simple question", OwnerUserId=1)
one_answer = Post(Title="Simple answer", Question = False, OwnerUserId=1)
print(my_session)
my_session.add_all([one_post, one_answer])
my_session.commit()
print(engine.execute("select * from post;").fetchall())
