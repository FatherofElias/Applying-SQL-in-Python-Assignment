import mysql.connector
from mysql.connector import Error

def get_members_in_age_range(start_age, end_age):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            database='fitness_db',
            user='root',
            password='placehold'
        )
        if conn.is_connected():
            cursor = conn.cursor()

            # SQL query using BETWEEN
            cursor.execute("""
                SELECT id, name, age
                FROM Members
                WHERE age BETWEEN %s AND %s
            """, (start_age, end_age))

            # Fetch and print the results
            members = cursor.fetchall()
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")

    except Error as e:
        # Handle errors
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            # Close the connection
            cursor.close()
            conn.close()

get_members_in_age_range(25, 30)