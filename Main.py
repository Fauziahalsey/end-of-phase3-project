import sqlite3
import webbrowser  # Import the webbrowser module

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

# Define doctor information
doctor_name = "Dr. Smith"
doctor_phone = "0759871476"
doctor_id = "12345"

def main_menu():
    while True:
        print("=======================")
        print("Prenatal Care CLI App")
        print("=======================")
        print("1. Educational Resources (Read Educational Content)")
        print("2. Appointment Scheduling")
        print("3. Offline Capability")
        print("4. Manage Patients")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            read_educational_content()  # Directly read educational content
        elif choice == '2':
            show_appointment_scheduling_menu()
        elif choice == '3':
            show_offline_capability_info()
        elif choice == '4':
            manage_patients_menu()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def read_educational_content():
    # Open the educational content link in a web browser
    educational_link = "https://www.goodhousekeeping.com/health/fitness/a37050658/pregnancy-exercises/"
    webbrowser.open(educational_link)

def show_appointment_scheduling_menu():
    # Display doctor's information
    print("Appointment Scheduling")
    print("Doctor's Name:", doctor_name)
    print("Doctor's Phone Number:", doctor_phone)
    print("Doctor's ID:", doctor_id)

    # Implement the Appointment Scheduling menu here
    pass

def show_offline_capability_info():
    # Display information about offline capability
    print("Welcome to the Offline Capability section.")
    print("In this section, you can access offline resources.")
    print("You can read books, articles, and watch videos even when you're not connected to the internet.")
    input("Press Enter to go back to the main menu...")

def manage_patients_menu():
    while True:
        print("=======================")
        print("Patient Management")
        print("=======================")
        print("1. Add Patient")
        print("2. Back to Main Menu")

        choice = input("Please select an option (1-2): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

# Close the database connection when done
conn.close()
