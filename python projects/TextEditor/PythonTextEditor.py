import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("Text Editor") # creates the title for the text editor window

text=tk.Text(root)

text.grid()

def saveas(): # saves the text entered as a variable 

    t = text.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if save_location: # saves the text as a txt file
        with open(save_location, "w", encoding="utf-8") as file:
            file.write(t)

    
button=tk.Button(root, text="Save", command=saveas) 
button.grid()

def open_file(): # opens text file to edit 
    file_location = filedialog.askopenfilename(
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if file_location: # finds the file location entered and opens the file
        with open(file_location, "r", encoding="utf-8") as file:
            t = file.read()

        text.delete("1.0", "end")
        text.insert("1.0", t)

button=tk.Button(root, text="open", command=open_file) 
button.grid()

def font_courier():
    text.config(font=("Courier New", 12))

def font_helvetica():
    text.config(font=("Helvetica"))

font_button = tk.Menubutton(root, text="Font")
font_button.grid()

font_menu = tk.Menu(font_button)
font_button["menu"] = font_menu

font_choice = tk.StringVar(value="courier")

font_menu.add_radiobutton(
    label="courier",
    variable=font_choice,
    value="courier",
    command=font_courier
)

font_menu.add_radiobutton(
    label="Helvetica",
    variable=font_choice,
    value="Helvetica",
    command=font_helvetica    
)


root.mainloop()