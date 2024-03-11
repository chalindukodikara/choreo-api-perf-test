import psycopg2
import json
from faker import Faker
from psycopg2 import sql

connection_configs = {
    "dbname": "postgres",
    "user": "chalindu",
    "password": "Admin@1234",
    "host": "localhost",
    "port": "5432"
}

def clear_kind_table():
    try:
        conn = psycopg2.connect(**connection_configs)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM kind")
        conn.commit()
        conn.close()
        print("Kind table cleared successfully.")
    except Exception as e:
        print("Error clearing kind table:", e)
    

def insert_component_kind(data):
    try:
        conn = psycopg2.connect(**connection_configs)
        cursor = conn.cursor()
        db_key = "choreo/api/example_org/" + data["metadata"]["projectName"] + "/" + data["metadata"]["name"]
        cursor.execute(
            sql.SQL("INSERT INTO kind (key, value) VALUES (%s, %s)"), (db_key, json.dumps(data))
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error inserting component data:", e)
