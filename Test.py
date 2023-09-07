###IMPORTS###
import customtkinter as ctk
from tkinter import messagebox
import random
import pickle

###VARIABELEN###
with open("account_database.pkl","rb") as fp: #Opent de account database
    global database
    database = pickle.load(fp) #Haalt de database op en update die
global standaardlijst
standaardlijst = {
    'Een':'One',
    'Twee':'Two',
    'Drie':'Three',
    'Vier':'Four',
    'Vijf':'Five',
    'Zes':'Six',
    'Zeven':'Seven',
    'Acht':'Eight',
    'Negen':'Nine',
    'Tien':'Ten',
    'Elf':'Eleven',
    'Twaalf':'Twelve',
    'Dertien':'Thirteen',
    'Veertien':'Fourteen',
    'Vijftien':'Fifteen',
    'Zestien':'Sixteen',
    'Zeventien':'Seventeen',
    'Achttien':'Eighteen',
    'Negentien':'Nineteen',
    'Twintig':'Twenty',
}

###COMMANDO'S###

def login(): #Bij login
    print("Test")
    gebruikersnaam = str(entry1.get()) #Haal gebruikersnaam op
    wachtwoord = str(entry2.get()) #Haal wachtwoord op
    if gebruikersnaam in database: #Als de gebruikersnaam in de database staat...
        if wachtwoord == database[gebruikersnaam]: #Als het wachtwoord klopt...
            change_to_next() #Login
        else:
            messagebox.showerror('Python Error', 'Error: Wrong password')
    else: #Als de gebruikersnaam niet bestaat...
        messagebox.showerror('Python Error', 'Error: Account not found, wrong username')

def registreer(): #Wordt geactiveerd bij registratie
    gebruikersnaam = str(entry1.get()) #Haal gebruikersnaam op
    wachtwoord = str(entry2.get()) #Haal wachtwoord op
    if gebruikersnaam not in database: #Als de gebruikersnaam nog niet in gebruik is
        database.update({gebruikersnaam:wachtwoord}) #Voeg naam en wachtwoordcombi toe aan database
        print(database)
        save_database()
    else: #Als de gebruikersnaam al in de database staat
        messagebox.showerror('Python Error', 'Error: Username already in use.') #Stuur error

def change_to_next():
    inlogscreen.destroy()
    next =  ctk.CTkFrame(root)
    next.pack(fill='both',expand=True)
    prompt = random.choice(list(termenlijst.keys()))
    hallo = ctk.CTkLabel(master=next, text=f"Wat is de vertaling van: {prompt}")
    hallo.pack(pady=12, padx=10)
    global antwoord
    antwoord = ctk.CTkEntry(master=next, placeholder_text="Gebruikersnaam")
    antwoord.pack(pady=12, padx=10)
    root.mainloop()

def verwijder_account():
    gebruikersnaam = str(entry1.get()) #Haal gebruikersnaam op
    if gebruikersnaam in database:
        wachtwoord = str(entry2.get()) #Haal wachtwoord op
        if wachtwoord == database[gebruikersnaam]:
            del database[gebruikersnaam]
            print(f'Account {gebruikersnaam} is verwijderd!')
            save_database()
        else:
            messagebox.showerror('Python Error', 'Error: Wrong password.') #Stuur error
    else:
        messagebox.showerror('Python Error', 'Error: Username not in database.') #Stuur error

def colorswitch(choice): #Als het thema veranderd moet worden
    print("combobox dropdown clicked:", choice)
    ctk.set_appearance_mode(choice) #Verander thema naar doorgegeven keuze

def save_database(): #Slaat de database op
    with open('account_database.pkl', 'wb') as fp: #Sla de nieuwe database op in account_database.pkl
        pickle.dump(database, fp)
        print('dictionary saved successfully to file')


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

    verwijderknop = ctk.CTkButton(master=frame, text="Verwijder Account", command=verwijder_account)
    verwijderknop.pack(pady=12, padx=10)


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
    global termenlijst
    termenlijst = standaardlijst
    inlogscherm()
    root.mainloop()
 
main()

###FUNCTIES###

# Deze functie draagt de gebruiker het prompt voor, en controleert of het inguvelde antwoord overeenkomt
# met de betekenis die als value is ingevuld bij de bijbehorende key in de achtieve termenlijst.
def promptvoordracht_en_controle():
    # Deze line geeft een prompt door een random key te kiezen uit een lijst met keys van de termenlijst
    prompt = random.choice(list(termenlijst.keys()))
    print("Wat is de vertaling van:",prompt)
    antwoord = input()
    # Deze line checkt of het opgegeven antwoord overeenkomt met het antwoord (value) 
    # die gekoppeld staat aan het prompt in de termenlijst 
    if antwoord.title() == termenlijst[prompt]:
        print('Correct')
    else:
        print('Incorrect')

def mainf():

    for key in termenlijst:
        promptvoordracht_en_controle()