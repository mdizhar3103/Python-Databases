import sqlalchemy as db

engine = db.create_engine("sqlite:///sqlalchemy_sqlite.db")
connection = engine.connect()

query = "select * from post where Id=1;"
print(engine.execute(query).fetchall())

query = "select ViewCount from post where Id=1;"
print(engine.execute(query).fetchall())

# updating the data
query = "update post set ViewCount=0 where Id=1;"
engine.execute(query)

query = "select ViewCount from post where Id=1;"
print(engine.execute(query).fetchall())

query = "select * from post where Id=1;"
print(engine.execute(query).fetchall())

# #########################
#                         #
#  Using Decalarative API #
#                         #
# #########################

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

session = sessionmaker()
session.configure(bind=engine)
my_session = session()
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


query = db.update(Post).where(Post.Id == 1).values(ViewCount = 1)
result = connection.execute(query)

post_query = my_session.query(Post).filter(
    Post.Id == 1)

print(post_query.one().Id)
print(post_query.one().ViewCount)
print(post_query.one().Title)

# Updating Multiple Records
query = db.update(Post).\
    values(ViewCount = Post.ViewCount + 50)
result = connection.execute(query)
# Note: this is dangerous be careful before running

# See the result on sqlite database
# sqlite> select ViewCount from post;

# Using session object
my_post = my_session.query(Post).filter(Post.Id == 1).one()
print(my_post.Title)
# modifying using python way
my_post.Title = "Modified Question"
print(my_session.dirty)
my_session.commit()

# select Title from post where Id=1;

# #################################

# Correlated Updates
# select avg(ViewCount) from post;

avg_views = db.select([db.func.avg(Post.ViewCount).label('AverageViews')])
query = db.update(Post).values(ViewCount = avg_views)
results = connection.execute(query)
print(results.rowcount)

# Deleting the record
print(my_session.query(Post.Id).all())
first_post = my_session.query(Post).first()
print(first_post)

my_session.delete(first_post)
print(my_session.query(Post.Id).all())
my_session.commit()

# deleting multiple records
print(my_session.query(Post.Id).all())
my_session.query(Post).filter(Post.Id > 2).delete()
my_session.commit()

# deleting the table
metadata = db.MetaData()
metadata.reflect(bind=engine)    # to load database information
print(metadata.tables.keys())
print(metadata.tables)

post_table = metadata.tables["post"]
print(post_table)
# dropping the table
post_table.drop(bind=engine)
