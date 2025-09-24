import sqlite3
connection=sqlite3.connect('Student.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Student(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Name TEXT NOT NULL,
                   Age INTEGER NOT NULL,
                   marks INTEGER NOT NULL,
                   section TEXT NOT NULL
               )''')
##insert data
cursor.execute("INSERT INTO Student (ID,Name, Age, marks, section) VALUES (1, 'Alice', 20, 85, 'A')")
cursor.execute("INSERT INTO Student (ID,Name, Age, marks, section) VALUES (2, 'Bob', 21, 90, 'B')")
cursor.execute("INSERT INTO Student (ID,Name, Age, marks, section) VALUES (3, 'Charlie', 22, 78, 'A')")
cursor.execute("INSERT INTO Student (ID,Name, Age, marks, section) VALUES (4, 'David', 23, 88, 'C')")
cursor.execute("INSERT INTO Student (ID,Name, Age, marks, section) VALUES (5, 'Eve', 20, 92, 'B')")
print("Data inserted successfully")
data=cursor.execute("SELECT * FROM Student")
for row in data:
    print(row)
connection.commit()
connection.close()