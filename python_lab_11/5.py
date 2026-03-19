import tkinter as tk
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
)

def signup():
    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (entry_user.get(), entry_pass.get())
    )
    conn.commit()
    label.config(text="Signup Success")

def login():
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (entry_user.get(), entry_pass.get())
    )
    if cursor.fetchone():
        label.config(text="Login Success")
    else:
        label.config(text="Invalid")

root = tk.Tk()

entry_user = tk.Entry(root)
entry_user.pack()

entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Signup", command=signup).pack()
tk.Button(root, text="Login", command=login).pack()

label = tk.Label(root)
label.pack()

root.mainloop()