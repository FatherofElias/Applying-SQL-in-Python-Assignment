
import mysql.connector
from mysql.connector import Error

def add_workout_session(member_id, session_id, session_date, session_time, activity):
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

            # SQL query to add a new workout session
            cursor.execute("""
                INSERT INTO WorkoutSessions (member_id, session_id, session_date, session_time, activity)
                VALUES (%s, %s, %s, %s, %s)
            """, (member_id, session_id, session_date, session_time, activity))

            # Commit the transaction
            conn.commit()
            print("Workout session added successfully!")

    except Error as e:
        # Handle invalid member ID or other constraint violations
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            # Close the connection
            cursor.close()
            conn.close()

# Function to get user input and add a new workout session
def input_new_workout_session():
    member_id = input("Enter member ID: ")
    session_id = input("Enter session ID: ")
    session_date = input("Enter session date (YYYY-MM-DD): ")
    session_time = input("Enter session time (HH:MM:SS): ")
    activity = input("Enter activity: ")

    # Add the new workout session to the database
    add_workout_session(member_id, session_id, session_date, session_time, activity)

# Example usage
input_new_workout_session()