# pip installl psycopg2

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS

con = psycopg2.connect("user=postgres password='postgres'")

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

 
# Obtain a DB Cursor

cursor  = con.cursor()

# Create a table in PostgreSQL database

cursor.execute('create database customerManagement')
print('well done')