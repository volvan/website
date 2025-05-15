import os
import psycopg2

conn = psycopg2.connect(
    host="130.208.246.143",
    database="scandb",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])
