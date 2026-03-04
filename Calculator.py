import tkinter as tk

window = tk.Tk()
window.title("Calculator.py")
window.geometry("350x500")
window.minsize(300, 400)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(5):
    window.grid_rowconfigure(i, weight=1)


def open_about():
    about = tk.Toplevel(window)
    about.title("About")
    about.geometry("300x200")

    tk.Label(about, text="About Calculator.py",
             font=("Arial", 14)).pack(pady=20)
    tk.Label(about, text="official Github Repository",
             font=("Arial", 14)).pack(pady=20)


menu_bar = tk.Menu(window)

menu_bar.add_command(label="About", command=open_about)

window.config(menu=menu_bar)


display = tk.Entry(
    window,
    font=("Arial", 30),
    justify="right",
    bd=5
)
display.grid(row=0, column=0, columnspan=4,
             sticky="nsew", padx=10, pady=10)


def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


buttons = [
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0

for button in buttons:

    if button == "C":
        action = clear
    elif button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(
        window,
        text=button,
        font=("Arial", 20),
        bd=3,
        command=action
    ).grid(row=row, column=col,
           sticky="nsew", padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1


window.mainloop()