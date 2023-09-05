import sqlite3

# Create a database connection
conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

# Create the Patients table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patients (
        Patients_id INTEGER PRIMARY KEY,
        Name TEXT,
        Phone_no INTEGER
    )
''')
conn.commit()

def add_patient():
    name = input("Enter the patient's name: ")
    phone_no = input("Enter the patient's phone number: ")

    # Insert patient information into the database
    cursor.execute('INSERT INTO Patients (Name, Phone_no) VALUES (?, ?)', (name, phone_no))
    conn.commit()
    print(f"Patient '{name}' with phone number '{phone_no}' added successfully.")

def main_menu():
    while True:
        print("=======================")
        print("Patient Management CLI")
        print("=======================")
        print("1. fauzia omala")
        print("2. 0793687179")

        print("2. Exit")

        choice = input("Please select an option (1-2): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

# Close the database connection when done
conn.close()
