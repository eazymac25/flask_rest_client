# Simple Flask Client
A simple Flask Rest Client

The goal is to open the data in store_procedures/Air_Quality.csv, 
create a database and table in PostgresSQL, and rap a REST client around that data.

The first step is to create a simple store procedure which creates the table
from a csv.

With the table created, the package makes use of flask and SQL Alchemy
to query the data and display it via an http get

MORE to COME! :)
