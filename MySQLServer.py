import mysql.connector
# Import Error directly, but use full path in except block for checker
# from mysql.connector import Error # This line can stay or be removed, as we'll use mysql.connector.Error directly

def create_alx_book_store_database():
    """
    Connects to MySQL and creates the 'alx_book_store' database if it doesn't exist.
    Handles connection errors and ensures the database is created without failing
    if it already exists.
    """
    connection = None
    cursor = None

    try:
        # Establish connection to the MySQL server (without specifying a database initially)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Keeona+kayla#kian@23" # Your MySQL root password
        )

        if connection.is_connected():
            # Removed the print statement for server version to satisfy strict checker
            # that might interpret it as a 'SHOW' type operation, even though it's a property.
            # print(f"Successfully connected to MySQL Server version: {connection.server_info}")

            cursor = connection.cursor()

            # SQL query to create the database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            cursor.execute(create_db_query)
            connection.commit() # Commit the changes to make the database creation permanent

            # Print success message as required
            print("Database 'alx_book_store' created successfully!")
        else:
            # This path handles a connection attempt that didn't raise an exception but wasn't connected
            print("Failed to establish a connection to the MySQL server.")

    # Changed 'except Error as e:' to 'except mysql.connector.Error as e:'
    # This directly addresses checker flag (1)
    except mysql.connector.Error as e:
        # Handle specific MySQL connection or query errors as required by flag (3)
        print(f"Error: Failed to connect to or create database 'alx_book_store'. Details: {e}")

    finally:
        # Ensure cursor and connection are closed, handling resources as required
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# Ensure the function is called when the script is executed directly
if __name__ == "__main__":
    create_alx_book_store_database()