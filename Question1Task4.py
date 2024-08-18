import mysql.connector
from mysql.connector import Error

def delete_workout_session(session_id):
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

            # Check if the session exists
            cursor.execute("SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            if cursor.fetchone()[0] == 0:
                print("Workout session does not exist.")
                return

            # SQL query to delete the session
            cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))

            # Commit the transaction
            conn.commit()
            print("Workout session deleted successfully!")

    except Error as e:
        # Handle errors
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            # Close the connection
            cursor.close()
            conn.close()

# Function to get user input and delete a workout session
def input_delete_workout_session():
    session_id = input("Enter session ID: ")

    # Delete the workout session from the database
    delete_workout_session(session_id)


input_delete_workout_session()