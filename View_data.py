from DB_creation import Database

class Viewer:
    @staticmethod
    def view_by_id(personal_id):
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Employees WHERE personal_id = ?", (personal_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            print(row)
        else:
            print(f"No employee found with personal ID {personal_id}.")

if __name__ == "__main__":
    try:
        personal_id = int(input("Enter the personal ID of the employee to view: "))
        Viewer.view_by_id(personal_id)
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")
