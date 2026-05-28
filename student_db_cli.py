import sqlite3

class StudentDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, age INTEGER, course TEXT, marks REAL
            )""")    
        self.conn.commit()
        print("DB ready.")

    def add_student(self, name, age, course, marks): 
        self.cursor.commit(
            "INSERT INTO students (name, age, course, marks) VALUES (?,?,?,?)",
            (name, age, course, marks)
        )
        self.conn.commit()
        print(f"Student added: {name}")

    def view_all(self):
        self.cursor.execute("SELECT * FROM students") 
        rows = self.cursor.fetchall()
        if not rows:
            print("No students found.")
            return 
        for r in rows:
            print(f"ID:{r[0]} | {r[1]} | Age:{r[2]} | {r[3]} | Marks:{r[4]}")

    def search_student(self, name):
        self.cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f'%{name}%',))
        rows = self.cursor.fetchall()
        if rows:
            for r in rows:
                print(f"ID:{r[0]} | {r[1]} | Age:{r[2]} | {r[3]} | Marks:{r[4]}") 
        else:
            print("No match found.")

    def update_marks(self, student_id, new_marks):
        self.cursor.execute(
                    "UPDATE students SET marks = ? WHERE id = ?",
                    (new_marks, student_id)
                    )        
        self.conn.commit()
        if self.cursor.rowcount == 0:
            print("Student ID not found")
        else:
            ("Marks updated.") 

    def delete_student(self, student_id):
        self.cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id)
        )           
        self.conn.commit()
        if self.cursor.rowcount == 0:
            print("ID not found.")
        else:
            print("Student deleted.")

    def show_stats(self):
        self.cursor.execute(
               "SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students"
        )     
        count, avg, high, low =  self.cursor.fetchone()  
        print(f"Total Students : {count}")
        print(f"Average Marks  : {avg:.2f}")
        print(f"Highest Marks  : {high:.2f}")
        print(f"Lowest Marks   : {low:.2f}")  

def main():
    db = StudentDB('student.db')
    while True:
        print("\n1.Add  2.View All  3.Search  4.Update Marks  5.Delete  6.Stats 7.Exit")
        try:
            choice = int(input("Choice: "))
        except ValueError:    
            print("Enter a number.")
            continue
        if choice == 1:
            name   = input("Name: ")
            age    = int(input("Age: "))
            course = input("Course: ")
            marks  = float(input("Marks: "))
            db.add_student(name, age, course, marks)
        elif choice == 2:
            db.view_all()
        elif choice == 3:
            db.search_student(input("Student name: "))
        elif choice == 4:
            db.update_marks(int(input("Student ID: ")), float(input("New Marks: "))) 
        elif choice == 5:
            db.delete_student(int(input("Student ID to delete: "))) 
        elif choice == 6:
            db.show_stats()
        elif choice == 7:
            print("Goodbye!") 
            db.conn.close()
            break                

if __name__ == '__main__':
    main() 

