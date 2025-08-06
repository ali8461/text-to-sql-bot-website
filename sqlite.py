# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('test.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE STUDENT (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(255),
    CLASS VARCHAR(255),
    SECTION VARCHAR(255),
    AGE INTEGER,
    EMAIL VARCHAR(255),
    ENROLL_DATE DATE
);"""
cursor.execute(table)

# Queries to INSERT records.
students = [
    ('Ali', 'Data Science', 'A', 22, 'ali@example.com', '2023-01-15'),
    ('Ahmed', 'Data Science', 'B', 23, 'ahmed@example.com', '2023-01-16'),
    ('Ahtesham', 'DevOps', 'C', 24, 'ahtesham@example.com', '2023-02-01'),
    ('Areeb', 'Data Science', 'C', 21, 'areeb@example.com', '2023-02-10'),
    # More data
    ('Sara', 'Cybersecurity', 'A', 22, 'sara@example.com', '2023-03-05'),
    ('Bilal', 'DevOps', 'B', 25, 'bilal@example.com', '2023-03-12'),
    ('Fatima', 'Data Science', 'B', 23, 'fatima@example.com', '2023-04-01'),
    ('Zain', 'Cybersecurity', 'C', 22, 'zain@example.com', '2023-04-15')
]

cursor.executemany('''
    INSERT INTO STUDENT (NAME, CLASS, SECTION, AGE, EMAIL, ENROLL_DATE)
    VALUES (?, ?, ?, ?, ?, ?)
''', students)

# Display data inserted
print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
