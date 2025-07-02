import mysql.connector
from mysql.connector import Error

def create_alx_book_store_database():
    """
    Connects to MySQL and creates the 'alx_book_store' database if it doesn't exist.
    Handles connection errors and ensures the database is created without failing
    if it already exists.
    """
    connection = None
    cursor = None
    database_name = "alx_book_store"

    try:
        # 1. Establish connection to the MySQL server (without specifying a database initially)
        #    Replace with your actual MySQL credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Keeona+kayla#kian@23" # Your MySQL root password
        )

        if connection.is_connected():
            print(f"Successfully connected to MySQL Server version: {connection.server_info}")
            cursor = connection.cursor()

            # 2. SQL query to create the database if it doesn't exist
            #    Using IF NOT EXISTS prevents the script from failing if the database is already there
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"

            cursor.execute(create_db_query)
            connection.commit() # Commit the changes to make the database creation permanent

            print(f"Database '{database_name}' created successfully!")
        else:
            print("Failed to establish a connection to the MySQL server.")

    except Error as e:
        # Handle specific MySQL connection or query errors
        print(f"Error: Failed to connect to or create database '{database_name}'. Details: {e}")

    finally:
        # 3. Ensure cursor and connection are closed
        if cursor:
            cursor.close()
            # print("Cursor closed.") # Optional: uncomment for more verbose output
        if connection and connection.is_connected():
            connection.close()
            # print("MySQL connection closed.") # Optional: uncomment for more verbose output

if __name__ == "__main__":
    create_alx_book_store_database()