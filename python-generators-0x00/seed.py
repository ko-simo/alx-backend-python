import mysql.connector
import csv
import os

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password"
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
