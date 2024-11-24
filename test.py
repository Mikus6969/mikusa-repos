from DB_creation import Database
from Add_data import Adder
from Delete_data import Deleter
from View_data import Viewer

def test_methods():
    
    test_name = "NAME"
    test_surname = "SURNAME"
    test_personal_id = 999

    
    print("\n--- Adding Employee ---")
    Adder.add_employee(test_name, test_surname, test_personal_id)

    
    print("\n--- Viewing Added Employee ---")
    try:
        added_data = Viewer.view_by_id(test_personal_id)
        if added_data:
            print("Data retrieved:", added_data)
            assert added_data[1] == test_name, "Name mismatch!"
            assert added_data[2] == test_surname, "Surname mismatch!"
            assert added_data[3] == test_personal_id, "Personal ID mismatch!"
            print("Retrieved data matches the input.")
    except AssertionError as e:
        print("Test Failed:", e)
        return

    print("\n--- Deleting Employee ---")
    Deleter.delete(test_personal_id)

    print("\n--- Verifying Deletion ---")
    post_delete_data = Viewer.view_by_id(test_personal_id)
    if not post_delete_data:
        print(" ")
    else:
        print("Test Failed: Data still exists")

if __name__ == "__main__":
    test_methods()
