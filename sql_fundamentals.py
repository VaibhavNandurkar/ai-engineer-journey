import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
print("Connected to school.db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY, course_name TEXT, instructor TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY, name TEXT, age INTEGER, course_id INTEGER     
)""")

conn.commit()
print("Tables Created")

courses_data = [
    (1, 'Machine Learning', 'Dr. Sharma'),
    (2, 'Web Development',  'Prof. Mehta'),
    (3, 'Data Science',     'Dr. Joshi')
]

students_data = [
    (1, 'Vaibhav', 21, 1),
    (2, 'Rohit',   22, 2),
    (3, 'Priya',   21, 1),
    (4, 'Sneha',   23, 3),
    (5, 'Amit',    20, 2)
]

cursor.executemany("INSERT OR IGNORE INTO courses VALUES (?,?,?)", courses_data)
cursor.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)", students_data)
conn.commit()
cursor.execute("SELECT COUNT(*) FROM students")
print("Students inserted:", cursor.fetchone()[0])

print("All students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall(): print(row)

print("\nAge > 21:")
cursor.execute("SELECT * FROM students WHERE age > 21")
for row in cursor.fetchall(): print(row)

print("\nOrdered A→Z:")
cursor.execute("SELECT * FROM students ORDER BY name ASC")
for row in cursor.fetchall(): print(row)

print("All students + courses")
cursor.execute("""
    SELECT students.name, students.age, courses.course_name
    FROM students INNER JOIN courses ON students.course_id = courses.id
""")
for row in cursor.fetchall(): print(row)

print("\nML students only:")
cursor.execute("""
    SELECT students.name, courses.course_name
    FROM students INNER JOIN courses ON students.course_id = courses.id
    WHERE courses.course_name = 'Machine Learning'
""")
for row in cursor.fetchall(): print(row)

cursor.execute("UPDATE students SET age = ? WHERE name = ?", (23, 'Rohit'))
cursor.execute("DELETE FROM students WHERE id=?", (5,))
conn.commit()

print("Update table:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall(): print(all)

conn.close()
print("Connection closed:")
