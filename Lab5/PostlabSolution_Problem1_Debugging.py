import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE PARTICIPANT (
    Participant_ID TEXT PRIMARY KEY,
    Last_Name TEXT,
    First_Name TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Telephone TEXT,
    Date_Of_Birth TEXT
);
""")
cursor.execute("""
CREATE TABLE ADVENTURE_CLASS (
    Class_ID TEXT PRIMARY KEY,
    Description TEXT,
    Max_Size INTEGER,
    Fee REAL
);
""")
cursor.execute("""
CREATE TABLE GUIDE (
    Guide_ID TEXT PRIMARY KEY,
    Last_Name TEXT,
    First_Name TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Phone TEXT,
    Hire_Date TEXT
);
""")
cursor.execute("""
CREATE TABLE CLASS_INSTANCE (
    Class_ID TEXT,
    Class_Date TEXT,
    Guide_ID TEXT,
    PRIMARY KEY (Class_ID, Class_Date),
    FOREIGN KEY (Class_ID) REFERENCES ADVENTURE_CLASS(Class_ID),
    FOREIGN KEY (Guide_ID) REFERENCES GUIDE(Guide_ID)
);
""")
cursor.execute("""
CREATE TABLE ENROLLMENT (
    Participant_ID TEXT,
    Class_ID TEXT,
    Class_Date TEXT,
    PRIMARY KEY (Participant_ID, Class_ID, Class_Date),
    FOREIGN KEY (Participant_ID) REFERENCES PARTICIPANT(Participant_ID),
    FOREIGN KEY (Class_ID, Class_Date) REFERENCES CLASS_INSTANCE(Class_ID, Class_Date)
);
""")

cursor.execute("INSERT INTO PARTICIPANT VALUES ('P001','Doe','John','123 Elm St','Townsville','TS','12345','555-1234','1990-01-01')")
cursor.execute("INSERT INTO ADVENTURE_CLASS VALUES ('C001','Intro to Hiking',10,50.0)")
cursor.execute("INSERT INTO GUIDE VALUES ('G001','Smith','Jane','456 Oak St','Villageton','VT','67890','555-5678','2020-05-15')")
cursor.execute("INSERT INTO CLASS_INSTANCE VALUES ('C001','2025-07-01','G001')")
cursor.execute("INSERT INTO ENROLLMENT VALUES ('P001','C001','2025-07-01')")
conn.commit()

print("Participants and Their Classes:")
for row in cursor.execute("""
    SELECT p.Participant_ID,
           p.First_Name || ' ' || p.Last_Name AS Participant,
           ac.Description,
           ci.Class_Date,
           g.First_Name || ' ' || g.Last_Name AS Guide
    FROM ENROLLMENT e
    JOIN PARTICIPANT p ON e.Participant_ID = p.Participant_ID
    JOIN CLASS_INSTANCE ci ON e.Class_ID = ci.Class_ID AND e.Class_Date = ci.Class_Date
    JOIN ADVENTURE_CLASS ac ON ci.Class_ID = ac.Class_ID
    JOIN GUIDE g ON ci.Guide_ID = g.Guide_ID;
"""):
    print(row)

conn.close()
