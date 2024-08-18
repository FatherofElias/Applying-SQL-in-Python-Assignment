import mysql.connector
from mysql.connector import Error

def add_member(id, name, age):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            database='fitness_db',
            user='root',
            password='Elias928'
        )
        if conn.is_connected():
            cursor = conn.cursor()

            # SQL query to add a new member
            cursor.execute("""
                INSERT INTO Members (id, name, age)
                VALUES (%s, %s, %s)
            """, (id, name, age))

            # Commit the transaction
            conn.commit()
            print("Member added successfully!")

    except Error as e:
        # Handle duplicate IDs or other constraint violations
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            # Close the connection
            cursor.close()
            conn.close()



def input_new_member():
    id = input("Enter member ID: ")
    name = input("Enter member name: ")
    age = input("Enter member age: ")

    # Add the new member to the database
    add_member(id, name, age)


input_new_member()