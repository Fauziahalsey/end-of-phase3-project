import sqlite3
import webbrowser

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

# Create the Doctors table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctors (
        Doctor_id INTEGER PRIMARY KEY,
        Name TEXT,
        Phone_no INTEGER
    )
''')

# Create the Appointments table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Appointments (
        Appointment_id INTEGER PRIMARY KEY,
        Doctor_id INTEGER,
        Patient_id INTEGER,
        Date DATE,
        Time TIME,
        FOREIGN KEY (Doctor_id) REFERENCES Doctors (Doctor_id),
        FOREIGN KEY (Patient_id) REFERENCES Patients (Patients_id)
    )
''')

# PatientsDoctors table for the many-to-many relationship
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PatientsDoctors (
        Patient_id INTEGER,
        Doctor_id INTEGER,
        PRIMARY KEY (Patient_id, Doctor_id),
        FOREIGN KEY (Patient_id) REFERENCES Patients (Patients_id),
        FOREIGN KEY (Doctor_id) REFERENCES Doctors (Doctor_id)
    )
''')

conn.commit()

def add_patient():
    name = input("Enter the patient's name: ")
    phone_no = input("Enter the patient's phone number: ")

    # Inserting patient information into the database
    cursor.execute('INSERT INTO Patients (Name, Phone_no) VALUES (?, ?)', (name, phone_no))
    conn.commit()
    print(f"Patient '{name}' with phone number '{phone_no}' added successfully.")


def add_doctor():
    name = input("Enter the doctor's name: ")
    phone_no = input("Enter the doctor's phone number: ")

    # Inserting doctor information into the database
    cursor.execute('INSERT INTO Doctors (Name, Phone_no) VALUES (?, ?)', (name, phone_no))
    conn.commit()
    print(f"Doctor '{name}' with phone number '{phone_no}' added successfully.")

def schedule_appointment():
    doctor_id = input("Enter the doctor's ID: ")
    patient_id = input("Enter the patient's ID: ")
    date = input("Enter the appointment date (YYYY-MM-DD): ")
    time = input("Enter the appointment time (HH:MM AM/PM): ")

    # Inserting appointment information into the database
    cursor.execute('''
        INSERT INTO Appointments (Doctor_id, Patient_id, Date, Time)
        VALUES (?, ?, ?, ?)
    ''', (doctor_id, patient_id, date, time))
    
    # Inserting association into PatientsDoctors table
    cursor.execute('INSERT INTO PatientsDoctors (Patient_id, Doctor_id) VALUES (?, ?)', (patient_id, doctor_id))
    
    conn.commit()
    print("Appointment scheduled successfully.")

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
            print("Thank you for contacting mama care!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def read_educational_content():
    # Open the educational content link in a web browser
    educational_link = "https://www.goodhousekeeping.com/health/fitness/a37050658/pregnancy-exercises/"
    webbrowser.open(educational_link)

def show_appointment_scheduling_menu():
    while True:
        print("=======================")
        print("Appointment Scheduling")
        print("=======================")
        print("1. Schedule Appointment")
        print("2. Back to Main Menu")

        choice = input("Please select an option (1-2): ")

        if choice == '1':
            schedule_appointment()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def show_offline_capability_info():
    # Displaying information about offline capability
    print("Welcome to Offline  mama care Capability section.")
    print("In this section, you can access offline resources.")
    print("You can read books, articles, and watch videos even when you're not connected to the internet.")
    input("Press Enter to go back to the main menu...")

def manage_patients_menu():
    while True:
        print("=======================")
        print("Patient Management")
        print("=======================")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Back to Main Menu")

        choice = input("Please select an option (1-3): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            add_doctor()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

# Close the database connection when done
conn.close()
