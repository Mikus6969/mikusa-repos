import os
import sqlite3
import datetime
from DB_creation import Database


class DatabaseMigrator:

    @staticmethod
    def migrate(column_name, column_type):
        conn = Database.create_connection()
        cursor = conn.cursor()

        migration_folder = "./migrations"
        os.makedirs(migration_folder, exist_ok=True)  

        # Define the file name for the migration script
        migration_file_name = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_add_column_{column_name}.sql"
        migration_path = os.path.join(migration_folder, migration_file_name)

        try:
            # Generate the SQL query to add the new column
            query = f"ALTER TABLE Employees ADD COLUMN {column_name} {column_type};"
            cursor.execute(query)

            # Write the migration query to a file
            with open(migration_path, "w") as migration_file:
                migration_file.write(query)
            print(f"Migration file created at {migration_path}")

            conn.commit()
            print(f"New column '{column_name}' added to table Employees.")

        except sqlite3.OperationalError:
            print(f"error occurred while adding column '{column_name}'")

        finally:
            conn.close()

if __name__ == "__main__":
    # Example: Add a new column
    DatabaseMigrator.migrate("position", "TEXT")