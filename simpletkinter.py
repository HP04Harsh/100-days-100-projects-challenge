import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.pack(pady=20)

# Function to update entry
def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Clear function
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons frame
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    
    for btn in row:
        if btn == 'C':
            action = clear
        elif btn == '=':
            action = calculate
        else:
            action = lambda x=btn: click(x)

        tk.Button(row_frame, text=btn, width=5, height=2,
                  font=("Arial", 14), command=action).pack(side=tk.LEFT, padx=5, pady=5)

# Run app
root.mainloop()