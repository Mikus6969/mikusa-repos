from DB_creation import Database

class Deleter:
    @staticmethod
    def delete(personal_id):
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Employees WHERE personal_id = ?", (personal_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Employee with personal ID {personal_id} has been deleted.")
        else:
            print(f"No employee found with personal ID {personal_id}.")

if __name__ == "__main__":
    try:
        personal_id = int(input("Enter the personal ID of the employee to delete: "))
        Deleter.delete(personal_id)
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")

