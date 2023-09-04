###IMPORTS###
import customtkinter as ctk


###VARIABELEN###
global database
database = {}


###COMMANDO'S###

def login():
    print("Test")
    gebruikersnaam = str(entry1.get())
    wachtwoord = str(entry2.get())
    print(gebruikersnaam)
    print(wachtwoord)
    change_to_next()

def registreer():
    gebruikersnaam = str(entry1.get())
    wachtwoord = str(entry2.get())
    if gebruikersnaam not in database:
        database.update({gebruikersnaam:wachtwoord})
        print(database)
    else:
        print("Gebruikersnaam al in gebruik")

def change_to_next():
    next =  ctk.CTkFrame(root)
    next.pack(fill='both',expand=True)
    inlogscreen.destroy()
    root.mainloop()

def colorswitch(choice):
    print("combobox dropdown clicked:", choice)
    ctk.set_appearance_mode(choice)

###SCHERMEN###

def inlogscherm():
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    global inlogscreen
    inlogscreen =  frame

    label = ctk.CTkLabel(master=frame, text="Login System")
    label.pack(pady=12, padx=10)
    global entry1
    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Gebruikersnaam")
    entry1.pack(pady=12, padx=10)
    global entry2
    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Wachtwoord", show="•")
    entry2.pack(pady=12, padx=10)

    registreerknop = ctk.CTkButton(master=frame, text="Registreren", command=registreer)
    registreerknop.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Inloggen", command=login)
    button.pack(pady=12, padx=10)

    combobox = ctk.CTkComboBox(master=frame, values=["Dark", "Light", "System"],command=colorswitch)
    combobox.pack(padx=12, pady=10)
    combobox.set("Dark")

    checkbox = ctk.CTkCheckBox(master=frame, text="Houd mij ingelogd")
    checkbox.pack(pady=12, padx=10)



def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    global root
    root = ctk.CTk()
    root.geometry("1366x768")
    inlogscherm()
    root.mainloop()
    
main()