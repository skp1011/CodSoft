import tkinter as tk
from math import sqrt

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_sqrt():
    try:
        expression = display.get()
        result = sqrt(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# ----------------Creating a window-------------------------------------------
window = tk.Tk()
window.title("Calculator Task:2")

# -----------------Creating an output/display window-----------------------------
display = tk.Entry(window, font=("Arial", 25))
display.grid(row=0, column=0, columnspan=16)

# ------------------Defining the buttons for numbers 0-9---------------------------
buttons = []
for i in range(10):
    button = tk.Button(window, text=str(i), padx=20, pady=10, command=lambda i=i: button_click(i))
    buttons.append(button)

# ------------------Positioning the number buttons on the grid----------------------
buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)

buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)

buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)

buttons[0].grid(row=4, column=0)

# -------------------Defining the buttons for arithmetic operations and square root--
add_button = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
subtract_button = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
multiply_button = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
divide_button = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))
sqrt_button = tk.Button(window, text="√", padx=20, pady=10, command=button_sqrt)
equal_button = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
clear_button = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)

# -------------------Positioning the arithmetic operation buttons-------------
add_button.grid(row=1, column=3)
subtract_button.grid(row=2, column=3)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3)
sqrt_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)
clear_button.grid(row=4, column=0)

# ----------------------Running the main event loop---------------------------
window.mainloop()