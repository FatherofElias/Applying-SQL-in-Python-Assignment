import mysql.connector
from mysql.connector import Error

def update_member_age(member_id, new_age):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            database='fitness_db',
            user='root',
            password='placeholder'
        )
        if conn.is_connected():
            cursor = conn.cursor()

            # Check if the member exists
            cursor.execute("SELECT COUNT(*) FROM Members WHERE id = %s", (member_id,))
            if cursor.fetchone()[0] == 0:
                print("Member does not exist.")
                return

            # SQL query to update age
            cursor.execute("""
                UPDATE Members
                SET age = %s
                WHERE id = %s
            """, (new_age, member_id))

            # Commit the transaction
            conn.commit()
            print("Member age updated successfully!")

    except Error as e:
        # Handle errors
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            # Close the connection
            cursor.close()
            conn.close()

# Function to get user input and update member age
def input_update_member_age():
    member_id = input("Enter member ID: ")
    new_age = input("Enter new age: ")

    # Update the member's age in the database
    update_member_age(member_id, new_age)

input_update_member_age()