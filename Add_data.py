from DB_creation import Database

class Adder:
    
    @staticmethod
    def add_employee(name, surname, personal_id):

        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Employees (name, surname, personal_id)
            VALUES (?, ?, ?)
        ''', (name, surname, personal_id))

        conn.commit()
        conn.close()
        print("Employee added.")

if __name__ == "__main__":
    Adder.add_employee("Mikus", "Ozols", 123)