import tkinter as tk
import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")

def add_task():
    task = entry.get()
    cursor.execute("INSERT INTO tasks VALUES (?)", (task,))
    conn.commit()
    listbox.insert(tk.END, task)

def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()
        listbox.delete(selected)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Add", command=add_task).pack()
tk.Button(root, text="Delete", command=delete_task).pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()