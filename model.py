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
conn.close()
