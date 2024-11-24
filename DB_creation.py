import sqlite3
import os
import datetime

class Database:

    @staticmethod
    def create_connection():
        # Connect to the SQLite database (default path is 'books.db')
        database_path = "employee.db"
        return sqlite3.connect(database_path)

    @staticmethod
    def create_table():
        conn = Database.create_connection()
        cursor = conn.cursor()

        migration_folder = "./migrations"
        os.makedirs(migration_folder, exist_ok=True)  

        # Generate a timestamped name for the initial migration file
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        initial_migration_path = os.path.join(migration_folder, f"{timestamp}_create_employee_table.sql")

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                personal_id INTEGER
            );
        '''

        # Execute the query to create the table
        cursor.execute(create_table_query)

        # Write the initial migration SQL to a file
        if not os.path.exists(initial_migration_path):
            with open(initial_migration_path, "w") as migration_file:
                migration_file.write(create_table_query)
            print(f"Initial migration file created at {initial_migration_path}")

        conn.commit()
        conn.close()


if __name__ == "__main__":
    Database.create_table()

