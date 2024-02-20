import csv
import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'testdb',
    'user': 'consultants',
    'password': 'WelcomeItc@2022',
    'host': 'ec2-3-9-191-104.eu-west-2.compute.amazonaws.com',  # or your database server's IP
    'port': '5432',  # default PostgreSQL port
}

# SQL statement for creating the table
create_table_sql = """
CREATE TABLE IF NOT EXISTS people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    occupation VARCHAR(255)
)
"""

# Connect to the PostgreSQL database
def connect_to_db(params):
    try:
        return psycopg2.connect(**params)
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Create a new table
def create_table(connection, create_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_sql)
        connection.commit()
        print("Table created successfully")
    finally:
        cursor.close()

# Load data from a CSV file into the database
def load_data_from_csv(connection, filename):
    try:
        cursor = connection.cursor()
        with open(filename, 'r') as file:
            next(file)  # Skip the header row
            reader = csv.reader(file)
            for row in reader:
                cursor.execute(
                    "INSERT INTO people (name, age, occupation) VALUES (%s, %s, %s)",
                    (row[0], int(row[1]), row[2])
                )
        connection.commit()
        print("Data loaded successfully")
    finally:
        cursor.close()

def main():
    connection = connect_to_db(db_params)
    if connection:
        create_table(connection, create_table_sql)
        # Assuming the CSV file is named 'people.csv' and located in the same directory as this script
        load_data_from_csv(connection, 'people.csv')
        connection.close()

if __name__ == "__main__":
    main()
