import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    email TEXT
)
""")

def register():
    cursor.execute(
        "INSERT INTO students (name, course, email) VALUES (?, ?, ?)",
        (entry_name.get(), entry_course.get(), entry_email.get())
    )
    conn.commit()
    label.config(text="Registered!")

root = tk.Tk()

entry_name = tk.Entry(root)
entry_name.pack()

entry_course = tk.Entry(root)
entry_course.pack()

entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Register", command=register).pack()

label = tk.Label(root)
label.pack()

root.mainloop()