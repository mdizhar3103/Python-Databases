import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:izhar@localhost:3306/sakila')

results = engine.execute("SHOW TABLES")

first_result = results.fetchone()

print(first_result)

other_result = results.fetchall()
print(len(other_result))

# reading data using pandas

import pandas as pd 

query = "SELECT * FROM city"

city_df = pd.read_sql_query(query, engine)

print(type(city_df))

print(city_df)

print(city_df.columns)

print(city_df[['city', 'country_id']].head())