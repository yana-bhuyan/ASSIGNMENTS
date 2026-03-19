import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")

    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

screen = tk.StringVar()
entry = tk.Entry(root, textvariable=screen)
entry.pack(fill="both", pady=10)

buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, width=5, height=2)
        b.pack(side="left")
        b.bind("<Button-1>", click)

root.mainloop()