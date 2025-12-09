import tkinter as tk
import os

if tk._default_root is not None:
    tk._default_root.destroy()

window = tk.Tk()
window.title("Habit + Mood Tracker")

habits = []
habit_vars = []

# // Adding Custom Habits //

def add_habit():
    name = habit_entry.get().strip()
    if name == "":
        return
    
    if window.winfo_exists():
        var = tk.IntVar(window)
        tk.Checkbutton(window, text=name, variabl=var).pack(anchor="w")
        habits.append(name)
        habit_vars.append(var)
        habit_entry.delete(0, tk.END)
    
# // Saving Data //

def save_habits():
    with open("habits.txt", "w") as f:
        for name, var in zip(habits, habit_vars):
            f.write(f"{name}| {var.get()}\n")
            
# // Load saved habits //

def load_habits():
    if not os.path.exists("habits.txt"):
        return
    
    with open("habits.txt", "r") as f:
        lines = f.readlines()
        
    for line in lines:
        if "| " in line or "|" in line:
            name, val = line.strip().split("|")
            var = tk.IntVar(window, value=int(val))
            tk.Checkbutton(window, text=name, variable=var).pack(anchor="w")
            
            habits.append(name)
            habit_vars.append(var)

# // //
            
habit_entry = tk.Entry(window)
habit_entry.pack()

tk.Button(window, text="Add Habit", command=add_habit).pack()

tk.Button(window, text="Save", command=save_habits).pack(pady=10)

# // Loading saved after closing //

window.mainloop()

load_habits()

# // Running app //
if __name__ == "__main__":
    main()
