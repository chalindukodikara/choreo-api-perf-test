import psycopg2
import json
from faker import Faker
from psycopg2 import sql
import threading
from kind import generate_component_kind, generate_build_kind, generate_deployment_kind, generate_project_kind

connection_configs = {
    "dbname": "choreo_declarative_api_db",
    "user": "chalindu",
    "password": "Admin@1234",
    "host": "localhost",
    "port": "5432"
}
table_name = "desired_store"

def clear_kind_table():
    try:
        conn = psycopg2.connect(**connection_configs)
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE " + table_name)
        conn.commit()
        conn.close()
        print(table_name + " table cleared successfully.")
    except Exception as e:
        print("Error clearing " + table_name + " table:", e)

def insert_data_with_threads(num_times, num_threads):
    def insert_thread():
        conn = psycopg2.connect(**connection_configs)
        for _ in range(num_times // num_threads):
            if conn.closed:
                conn = psycopg2.connect(**connection_configs)
            data = generate_component_kind()
            insert_kind_at_once(data, conn)
        conn.close()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=insert_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def insert_multiple_kind_data_with_threads(num_times, num_threads):
    def insert_thread():
        conn = psycopg2.connect(**connection_configs)
        for i in range(num_times // num_threads):
            if conn.closed:
                conn = psycopg2.connect(**connection_configs)
            if i % 4 == 0:
                data = generate_project_kind(table_name)
            elif i % 4 == 1:
                data = generate_component_kind(table_name)
            elif i % 4 == 2:
                data = generate_build_kind(table_name)
            else:
                data = generate_deployment_kind(table_name)
            insert_kind_at_once(data, conn)
        conn.close()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=insert_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def insert_kind(data):
    try:
        conn = psycopg2.connect(**connection_configs)
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("INSERT INTO " + table_name + " (payload) VALUES (%s)"), (json.dumps(data),)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error inserting kind data:", e)

def insert_kind_at_once(data, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("INSERT INTO " + table_name + " (payload) VALUES (%s)"), (json.dumps(data),)
        )
        conn.commit()
    except Exception as e:
        print("Error inserting kind data:", e)

