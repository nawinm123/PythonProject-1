import mysql.connector
from mysql.connector import Error

def fetch_records_from_db():
    """
    Connects to a MySQL database, executes a query, and fetches records.
    :return: List of fetched records or None if an error occurs
    """
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'root'
    db_name = 'python_poc'
    db_query = 'select * from data'

    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Execute the query
            cursor = connection.cursor()
            cursor.execute(db_query)
            table_records = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            print("MySQL connection is closed")
            return table_records

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    try:
        records = fetch_records_from_db()
        if records:
            print("Fetched Records:")
            for record in records:
                print(record)
        else:
            print("No records fetched or an error occurred.")

    except Exception as e:
        print(f"Error: {e}")
