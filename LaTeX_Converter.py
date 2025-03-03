import customtkinter as ctk
import sympy as sp


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()

app.geometry("500x500")
app.resizable(False, False)
app.title("LaTeX-Converter")

output = ""

def convert():
    global output
    string = input1.get()
    string = sp.sympify(string)
    output = sp.latex(string)
    outputLabel.configure(text=output)

def copy_to_clipboard():
    text = outputLabel.cget("text")  # Text aus dem Label holen
    app.clipboard_clear()      # Zwischenablage leeren
    app.clipboard_append(text) # Text zur Zwischenablage hinzufügen
    app.update() 

Headline = ctk.CTkLabel(app, width=200, height=50,text="LaTeX-Converter", fg_color="#242424", font=("Arial", 24))
Headline.pack(side="top", pady=20, padx=20)

input1 = ctk.CTkEntry(app, width=400, height=100,placeholder_text="Gib etwas ein...", placeholder_text_color="grey", fg_color="lightgrey", font=("Arial",18), text_color="black")
input1.pack(side="top", pady=10, padx=20)

Convert_button = ctk.CTkButton(app, width=150, height=50, text="Convert", font=("Arial", 18), command=convert)
Convert_button.pack(side="top", pady=0, padx=20)

outputLabel = ctk.CTkLabel(app, width=400, height=100, text="", fg_color="lightgrey", font=("Arial", 18), text_color="black", corner_radius=5, bg_color="grey")
outputLabel.pack(side="top", pady=10, padx=20)

copyButton = ctk.CTkButton(app, width=50, height=50, text="Copy", font=("Arial", 18), command=copy_to_clipboard)
copyButton.pack(side="right", pady=0, padx=20)

app.mainloop()