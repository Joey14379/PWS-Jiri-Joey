''' 
Code voor de app Verba
Code geschreven door:
Jiri Redeker
Joey van den Berg
Voor Profielwerkstuk
© 2024 Jiri Redeker & Joey van den Berg - ALL RIGHTS RESERVED
'''


###IMPORTS###
import customtkinter as ctk
import pickle
import random
import os
from tkinter import messagebox


###ROOT APP###
class App(ctk.CTk):
    def __init__(app): #Als de app opstart...
        super().__init__()
        ctk.set_appearance_mode("Dark")
        if random.randint(1,20) == 20: #5% kans dat de app blauw is ipv groen
            ctk.set_default_color_theme("blue")
        else:
            ctk.set_default_color_theme("green")
        app.geometry("1366x768") #Stel de appgrootte in
        app.minsize(1366, 768) #Maak de app niet verkleinbaar
        app.title("Verba")
        app.attributes('-fullscreen', True) #Zet de app op fullscreen
        global lijsten_list
        try:    #Als lijsten_list er al is:
            with open('lijsten_list.pkl', 'rb') as fp: #Sla de nieuwe database op in {filename}.pkl           
                lijsten_list = pickle.load(fp)
        except: #Anders, maak lijsten_list aan.
            lijsten_list = []
            with open('lijsten_list.pkl', 'wb') as fp:
                pickle.dump(lijsten_list, fp)






    ###SCHERMEN###

    #Homescreen#
    def homescreen(app):
        app.clear()
        app.grid_rowconfigure((0,7), weight=1)
        app.grid_rowconfigure((1,2,3,4,5,6), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1)

        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Welkom bij Verba", 
                                font = ('Arial', 30))
        app.logo.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

        #Button voor flashcards#
        app.button = ctk.CTkButton(master=app,
                                   command=app.flashcards, 
                                   text="Flashcards", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button.grid(row=1, column=1, padx=20, pady=20, sticky="nswe")

        #Button voor woordjes stampen#
        app.button2 = ctk.CTkButton(master=app, 
                                   command=app.woordjes_oefenen, 
                                   text="Woordjes oefenen", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button2.grid(row=2, column=1, padx=20, pady=20, sticky="nswe")

        #Button voor 'Mijn lijsten'#
        app.button3 = ctk.CTkButton(master=app, 
                                   command=lambda:app.mijn_lijsten("Nieuwe lijst maken"), 
                                   text="Mijn lijsten", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button3.grid(row=3, column=1, padx=20, pady=20, sticky="nswe")

        #Button voor settings#
        app.button4 = ctk.CTkButton(master=app, 
                                   command=app.settings, 
                                   text="Settings", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button4.grid(row=4, column=1, padx=20, pady=20, sticky="nswe")

        #Button voor help#
        app.button5 = ctk.CTkButton(master=app,
                                   command=app.help, 
                                   text="Help", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button5.grid(row=5, column=1, padx=20, pady=20, sticky="nswe")

        #Button voor settings#
        app.button6 = ctk.CTkButton(master=app, 
                                   command=app.destroy, 
                                   text="Quit", 
                                   font = ('Arial', 25),
                                   corner_radius= 200)
        app.button6.grid(row=6, column=1, padx=20, pady=20, sticky="nswe")

        #Copyright#
        app.label = ctk.CTkLabel(master=app, 
                                text="© 2024 Jiri Redeker & Joey van den Berg - ALL RIGHTS RESERVED", 
                                font = ('Arial', 10))
        app.label.grid(row=7, column=1, padx=20, pady=(20, 0), sticky="nsew")        

        app.mainloop()

    #Flashcards#
    def flashcards(app):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Flashcards", 
                                font = ('Arial', 25))
        app.logo.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

        #Knop om terug te gaan naar het homescreen#
        app.button = ctk.CTkButton(master=app,
                                   command=app.homescreen, 
                                   text="Terug", 
                                   font = ('Arial', 25),
                                   width=60,
                                   height=50)
        app.button.grid(row=5, column=2, padx=20, pady=20, sticky="es")

        #Start de flashcards#
        app.button1 = ctk.CTkButton(master=app, 
                                   command=lambda:app.flashcards_quiz(app.list.get(),flipped = False,term = "",antwoord = "",current_list={}, answered = True, startup=True,correct=False), 
                                   text="Start", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40,
                                   corner_radius= 300)
        app.button1.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        #Tekstlabel#
        app.label = ctk.CTkLabel(master=app, 
                                text="Welke lijst wil je oefenen?", 
                                font = ('Arial', 25))
        app.label.grid(row=2, column=1, padx=20, pady=(20, 0), sticky="s")

        with open("lijsten_list.pkl","rb") as fp: #Laad lijsten_list in en haal "Nieuwe lijst maken" eruit
            lijsten_list = pickle.load(fp)
        if "Nieuwe lijst maken" in lijsten_list:
            lijsten_list.remove("Nieuwe lijst maken")
        #Selectorpaneel voor al je lijsten
        try:
            app.list = ctk.CTkOptionMenu(master=app, font=('Arial',25), values=lijsten_list,command=None, state="readonly", height=50)
            app.list.set(lijsten_list[0])
            app.list.grid(row=3, column=1, padx=12, pady=10, sticky ="new")
        except: #Laat het de gebruiker zien als er nog geen lijst is om te oefenen.
            messagebox.showerror('Python Error', 'Error: Maak eerst een lijst aan in "mijn lijsten" voordat je kunt oefenen!')
            app.homescreen()

        #Uitleg voor de flashcards
        textbox = ctk.CTkTextbox(master=app,font = ('Arial', 25))
        textbox.grid(row=1,column=0, padx=20, pady=20, sticky="nsew", rowspan="3")
        textbox.insert("0.0", "Flashcards:\n\nIn de modus flashcards kies je één van je lijsten om mee te oefenen. \nVervolgens krijg je één van je \ntermen voorgeschoteld en moet jij \nzelf in je hoofd bedenken wat de \ngoede betekenis is. Heb je deze \ngoed, druk je op goed. Heb je \ndeze fout, druk je op fout. Als je al \nje termen minimaal eenmaal goed beantwoord hebt, heb je \ngewonnen!")
    
        app.mainloop()

    #Flashcards quiz-screen#
    def flashcards_quiz(app,lijst,flipped,term,antwoord,current_list,answered,startup,correct):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        if startup: #Als de quiz voor het eerst wordt opgestart:
            with open(lijst+".pkl","rb") as fp: #Laad de lijst in
                current_list = pickle.load(fp)
                startup = False #Zorg dat er geen startup meer is
        if answered: #Als er geantwoord:
            if correct: #Als het juist was:
                try: #Haal de term uit de lijst
                    current_list.pop(term)
                except:
                    pass
            try: #Probeer een nieuwe term te kiezen
                term = random.choice(list(current_list))
                antwoord = current_list[term]
            except: #Als dat niet lukt omdat er niets meer in de lijst staat...
                app.flashcards_end() #Ben je klaar, ga naar eindscherm

        if flipped: #Als de flashcard omgedraaid is:
            app.text = ctk.CTkLabel(master=app, #Laad de achterkant
                                text=antwoord, 
                                font = ('Arial', 40),
                                fg_color=("white", "green"),
                                corner_radius=8)
            app.text.grid(row=3, column=1, padx=20, pady=(20, 0), sticky="nsew")

            app.vraag = ctk.CTkLabel(master=app, #Laad de achterkant
                                text="Heb je het goed?", 
                                font = ('Arial', 25))
            app.vraag.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="new")

            #Knop voor goede antwoord
            app.goed = ctk.CTkButton(master=app, 
                                   command=lambda:app.flashcards_quiz(lijst,flipped,term,antwoord,current_list,answered=True, startup=False,correct=True), 
                                   text="Goed", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=60,
                                   fg_color=("white", "#197531"),
                                   hover_color="#125724",
                                   corner_radius= 300)
            app.goed.grid(row=3, column=0, padx=20, pady=20, sticky="sew")

            #Knop voor foute antwoord
            app.fout = ctk.CTkButton(master=app, 
                                   command=lambda:app.flashcards_quiz(lijst,flipped,term,antwoord,current_list,answered=True,startup=False,correct=False), 
                                   text="Fout", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=60,
                                   fg_color=("white", "#940740"),
                                   hover_color="#570325",
                                   corner_radius= 300)
            app.fout.grid(row=4, column=0, padx=20, pady=20, sticky="new")

        elif not flipped: #Als de flashcard niet is omgedraaid:
            app.text = ctk.CTkLabel(master=app, #Laad de voorkant
                                text=term, 
                                font = ('Arial', 40),
                                fg_color=("white", "blue"),
                                corner_radius=8)
            app.text.grid(row=3, column=1, padx=20, pady=(20, 0), sticky="nsew")

        #Knop die de card flipt
        app.knop = ctk.CTkButton(master=app, 
                                   command=lambda:app.flashcards_quiz(lijst,flipped,term,antwoord,current_list,answered=False, startup=False, correct=False), 
                                   text="Laat andere kant zien", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40,
                                   corner_radius= 300)
        app.knop.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        #Knop die terug naar start gaat
        app.terug = ctk.CTkButton(master=app,
                                   command=app.homescreen, 
                                   text="Stoppen", 
                                   font = ('Arial', 25),
                                   width=60,
                                   height=50)
        app.terug.grid(row=5, column=2, padx=20, pady=20, sticky="es")

        #Termenteller#
        app.termenteller = ctk.CTkLabel(master=app,
                                text=f"Termen over: {len(current_list)}", 
                                font = ('Arial', 25))
        app.termenteller.grid(row=1, column=2, padx=20, pady=(20, 0), sticky="nsew")

        #Verander de state
        if flipped: 
            flipped = False
        elif not flipped:
            flipped = True

        app.mainloop()


    #Flashcards quiz-screen#
    def flashcards_end(app):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        #Felicitatiebericht#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Gefeliciteerd! Je bent klaar!", 
                                font = ('Arial', 25))
        app.logo.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="nsew")

        #Knop om terug naar hoofdscherm te gaan#
        app.button = ctk.CTkButton(master=app, 
                                   text="Begrepen",
                                   command = lambda: app.homescreen(), 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40,
                                   corner_radius= 300)
        app.button.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        app.mainloop()

    #Woordjes stampen#
    def woordjes_oefenen(app):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1, uniform='column')


        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Woordjes Oefenen", 
                                font = ('Arial', 25))
        app.logo.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")
        
        #Knop voor homescreen#
        app.button = ctk.CTkButton(master=app,
                                   command=app.homescreen, 
                                   text="Terug", 
                                   font = ('Arial', 25),
                                   width=60,
                                   height=50)
        app.button.grid(row=5, column=2, padx=20, pady=20, sticky="es")

        #Knop om te starten met oefenen#
        app.button1 = ctk.CTkButton(master=app, 
                                   command=lambda:app.woordjes_oefenen_quiz(current_list={},lijst=app.list.get(), startup=True,juist=False,antwoord="",term=""), 
                                   text="Start", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40,
                                   corner_radius= 300)
        app.button1.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        #Tekstlabel#
        app.label = ctk.CTkLabel(master=app, 
                                text="Welke lijst wil je oefenen?", 
                                font = ('Arial', 25))
        app.label.grid(row=2, column=1, padx=20, pady=(20, 0), sticky="s")

        #Selectorpannel voor keuze lijst#
        with open("lijsten_list.pkl","rb") as fp: #Laad lijsten_list in en haal "Nieuwe lijst maken" eruit
            lijsten_list = pickle.load(fp)
        if "Nieuwe lijst maken" in lijsten_list:
            lijsten_list.remove("Nieuwe lijst maken")
        try:
            app.list = ctk.CTkOptionMenu(master=app, font=('Arial',25), values=lijsten_list, state="readonly", height=50)
            app.list.set(lijsten_list[0])
            app.list.grid(row=3, column=1, padx=12, pady=10, sticky ="new")
        except: #Laat de gebruiker zien dat er nog geen lijst is, en je dus ook niet kunt oefenen
            messagebox.showerror('Python Error', 'Error: Maak eerst een lijst aan in "mijn lijsten" voordat je kunt oefenen!')
            app.homescreen()
        
        #Uitleg voor oefenen#
        textbox = ctk.CTkTextbox(master=app,font = ('Arial', 25))
        textbox.grid(row=1,column=0, padx=20, pady=20, sticky="nsew", rowspan="3")
        textbox.insert("0.0", "Woordjes oefenen:\n\nIn de modus woordjes oefenen \nkies je één van je lijsten om mee \nte oefenen. Vervolgens krijg je één van je termen voorgeschoteld. Dan moet jij in het invulveld de goede \nbetekenis invullen en op de knop \n'Voer in' drukken. Verba kijkt dan \nvoor je na. Vervolgens laat Verba \nje weten of je het antwoord goed \nof fout hebt. Als je al je termen \nminimaal eenmaal goed \nbeantwoord hebt, heb je \ngewonnen!")
    
        app.mainloop()

    #Quizscherm voor woordjes_oefenen
    def woordjes_oefenen_quiz(app,current_list,lijst,startup,juist,antwoord,term):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        if not startup: #Laat de gebruiker zien of het antwoord goed of fout is, en wat dan wel het juiste antwoord is#
            if juist:
                app.goed = ctk.CTkLabel(master=app, 
                                    text="Dat is goed!", 
                                    font = ('Arial', 25))
                app.goed.grid(row=3, column=1, padx=20, pady=(20, 0), sticky="sew")
                current_list.pop(term)
            else:
                app.fout = ctk.CTkLabel(master=app, 
                                    text=f"Dat is fout, het juiste antwoord is: {antwoord}", 
                                    font = ('Arial', 25))
                app.fout.grid(row=3, column=1, padx=20, pady=(20, 0), sticky="sew")
                
        
        elif startup: #Als de quiz voor het eerst wordt opgestart:
            with open(lijst+".pkl","rb") as fp: #Laad de lijst in
                current_list = pickle.load(fp)
                startup = False #Zorg dat er geen startup meer is

        try:
            term = random.choice(list(current_list))
            antwoord = current_list[term]
        except: #Als dat niet lukt omdat er niets meer in de lijst staat...
            app.flashcards_end() #Ben je klaar, ga naar eindscherm

        #Tekstlabel#
        app.label = ctk.CTkLabel(master=app, 
                                text="Wat betekent:", 
                                font = ('Arial', 25))
        app.label.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="sew")

        #Laat de term zien#
        app.termtext = ctk.CTkLabel(master=app, 
                                text=term,
                                font = ('Arial', 25))
        app.termtext.grid(row=2, column=1, padx=20, pady=(20, 0), sticky="new")

        #Knop die terug naar start gaat#
        app.terug = ctk.CTkButton(master=app,
                                   command=app.homescreen, 
                                   text="Stoppen", 
                                   font = ('Arial', 25),
                                   width=60,
                                   height=50)
        app.terug.grid(row=5, column=2, padx=20, pady=20, sticky="es")

        #Invulveld voor het antwoord#
        app.invul = ctk.CTkEntry(master=app, placeholder_text="Term")
        app.invul.grid(row=4, column=1, padx=20, pady=20, sticky = "nsew")

        #Knop om je antwoord in te voeren#
        app.confirm = ctk.CTkButton(master=app, 
                                   command=lambda:app.check_juist(antwoord,app.invul,current_list,lijst,startup,term),
                                   text="Voer in", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40,
                                   corner_radius= 300)
        app.confirm.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        #Termenteller
        app.termenteller = ctk.CTkLabel(master=app,
                                text=f"Termen over: {len(current_list)}", 
                                font = ('Arial', 25))
        app.termenteller.grid(row=1, column=2, padx=20, pady=(20, 0), sticky="nsew")



    #Mijn lijsten#
    def mijn_lijsten(app,choice):
        app.clear()
        app.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        app.grid_columnconfigure((0,1,2), weight=1, uniform="column")
        current_list = choice

        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Mijn Lijsten", 
                                font = ('Arial', 25))
        app.logo.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

        if current_list == "Nieuwe lijst maken": #Als de lijst 'Nieuwe lijst maken' is, geef dan de mogelijkheid een naam in te vullen
            app.listname = ctk.CTkEntry(master=app, placeholder_text="Naam nieuwe lijst")
            app.listname.grid(row=8, column=1, padx=20, pady=20, sticky="new")
        else: #Zo niet, laat de gebruiker de lijst dan verwijderen
            app.removebtn = ctk.CTkButton(master=app, 
                                   command=lambda:app.remove_list(app.list,lijsten_list), 
                                   text="Verwijder lijst", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40)
            app.removebtn.grid(row=6, column=2, padx=20, pady=20)

        #Tekstlabel#
        app.label = ctk.CTkLabel(master=app, 
                                text="Welke lijst wil je bewerken?", 
                                font = ('Arial', 25))
        app.label.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="sew")

        if current_list not in lijsten_list:
            lijsten_list.append("Nieuwe lijst maken")

        #Selectorpanel voor je lijsten#
        app.list = ctk.CTkComboBox(master=app, font=('Arial',25), values=lijsten_list,command=app.mijn_lijsten, state="readonly")
        app.list.set(current_list)
        app.list.grid(row=2, column=1, padx=12, pady=10, sticky ="new")

        #Tekstlabel term#
        app.text1 = ctk.CTkLabel(master=app, 
                                text="Term", 
                                font = ('Arial', 25))
        app.text1.grid(row=3, column=1, padx=20, pady=0, sticky="sew")
    
        #Invulveld term#
        app.term = ctk.CTkEntry(master=app, placeholder_text="Term")
        app.term.grid(row=4, column=1, padx=20, pady=20, sticky = "new")

        #Tekstlabel betekenis#
        app.text2 = ctk.CTkLabel(master=app, 
                                text="Betekenis", 
                                font = ('Arial', 25))
        app.text2.grid(row=5, column=1, padx=20, pady=0, sticky="sew")
    
        #Invulveld betekenis#
        app.betekenis = ctk.CTkEntry(master=app, placeholder_text="Betekenis")
        app.betekenis.grid(row=6, column=1, padx=20, pady=20, sticky="new")

        #Knop voor opslaan#
        app.button = ctk.CTkButton(master=app, 
                                   command=lambda:app.list_submit(app.term,app.betekenis,app.list,app.listname), 
                                   text="Opslaan", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40)
        app.button.grid(row=7, column=1, padx=20, pady=20, sticky="nsew")
        
        #Knop om terug te gaan naar het hoofdscherm#
        app.button = ctk.CTkButton(master=app, 
                                   command=app.homescreen, 
                                   text="Terug", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40)
        app.button.grid(row=7, column=2, padx=20, pady=20)

        app.mainloop()

    #Settings#
    def settings(app):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1,uniform="column")

        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Settings", 
                                font = ('Arial', 25))
        app.logo.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        #Selectorpanel voor het thema#
        app.theme = ctk.CTkOptionMenu(master=app, font=('Arial',25), values=["Dark", "Light", "System"],command=app.themeswitch, state="readonly")
        app.theme.set("Dark")
        app.theme.grid(row=1, column=1, padx=10, pady=10, sticky ="ew")

        #Knop om terug te gaan naar het hoofdscherm#
        app.button = ctk.CTkButton(master=app, 
                                   command=app.homescreen, 
                                   text="Terug", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40)
        app.button.grid(row=5, column=2, padx=20, pady=20)

        app.mainloop()


    #Help#
    def help(app):
        app.clear()
        app.grid_rowconfigure((0), weight=1)
        app.grid_rowconfigure((1,2,3,4,5), weight=10)
        app.grid_columnconfigure((0,1,2), weight=1,uniform="column")

        #Plaats voor het logo#
        app.logo = ctk.CTkLabel(master=app, 
                                text="Help", 
                                font = ('Arial', 25))
        app.logo.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        #Tekstvak met de handleiding#
        textbox = ctk.CTkTextbox(master=app,font = ('Arial', 25))
        textbox.grid(row=1,column=0, padx=20, pady=20, sticky="nsew", rowspan="4", columnspan="3")
        textbox.insert("0.0", "Handleiding\n\n"
                       "Flashcards:\nIn de modus flashcards kies je één van je lijsten om mee te oefenen. Vervolgens krijg je één van je termen \nvoorgeschoteld en moet jij zelf in je hoofd bedenken wat de goede betekenis is. Heb je deze goed, druk je op goed. \nHeb je deze fout, druk je op fout. Als je al je termen minimaal eenmaal goed beantwoord hebt, heb je gewonnen!\n\n"
                       "Woordjes oefenen:\nIn de modus woordjes oefenen kies je één van je lijsten om mee te oefenen. Vervolgens krijg je één van je termen \nvoorgeschoteld. Dan moet jij in het invulveld de goede betekenis invullen en op de knop 'Voer in' drukken. Verba kijkt dan voor je na. Vervolgens laat Verba je weten of je het antwoord goed of fout hebt. Als je al je termen minimaal \neenmaal goed beantwoord hebt, heb je gewonnen!\n\n"
                       "Mijn lijsten:\nIn het 'mijn lijsten'-scherm kun je zelf een eigen lijst maken. Dit doe je door 'Nieuwe lijst maken' te selecteren en \nvervolgens een term, een betekenis en de naam van de lijst in te vullen. Vervolgens druk je op opslaan. Het scherm verspringt meteen naar de nieuwe lijst en je kunt door meer termen en betekenissen tegelijk in te vullen je lijst \nuitbreiden.\n"
                       "Je past een term aan door de term weer opnieuw in te vullen en een andere betekenis mee te geven. Als je dit \nopslaat is de term aangepast.\nJe kunt een lijst verwijderen door tijdens het bewerken van de lijst op de knop 'verwijderen' te drukken. Let op: Dit is niet omkeerbaar!")

        #Knop om terug te gaan naar het hoofdscherm#
        app.button = ctk.CTkButton(master=app, 
                                   command=app.homescreen, 
                                   text="Terug", 
                                   font = ('Arial', 25),
                                   width=40,
                                   height=40)
        app.button.grid(row=5, column=2, padx=20, pady=20)

        app.mainloop()


    ###COMMANDO'S###

    #Leeg het scherm#
    def clear(app):
        for item in app.winfo_children(): #Voor ieder item...
            item.destroy() #verwijder het item

    #Verandert het thema naar het gekozen thema#
    def themeswitch(app,choice):
        ctk.set_appearance_mode(choice)

    #Upload en update de lijst#
    def list_submit(app,term,betekenis,list,newlistname):
        print(list.get())
        if list.get() == "Nieuwe lijst maken": #Als het een nieuwe lijst is:
            current_list = newlistname.get() + ".pkl" #Neem de ingevulde naam over
            curli = newlistname.get()
        else:   #Als de lijst al bestaat:
            current_list = list.get() + ".pkl" #Neem de aangegeven lijst over
            curli = list.get()
        print(current_list)
        try: #Als de lijst al bestaat:
            with open(current_list,"rb") as fp: #Opent de te bewerken lijst
                tebewerkenlijst = pickle.load(fp)
                if term.get() != "":
                    tebewerkenlijst[term.get()] = betekenis.get()
                else: 
                    app.mijn_lijsten(choice=curli)
            with open(current_list, 'wb') as fp: #Sla de nieuwe lijst op
                pickle.dump(tebewerkenlijst, fp)
                print(f'Dictionary saved successfully to file: {current_list}')
        except: #Als de lijst nog niet bestaat:
            with open(current_list, 'wb') as fp: #Maak een nieuw, leeg .pkl-bestand aan voor de nieuwe lijst
                pickle.dump({}, fp)
                print(f'Succesfully created file: {current_list}')
            with open(current_list,"rb") as fp: #Opent de te bewerken lijst
                tebewerkenlijst = pickle.load(fp)
            if term.get() != "":
                tebewerkenlijst[term.get()] = betekenis.get()
            else:
                messagebox.showerror('Python Error', 'Error: Voeg eerst een term en betekenis toe!')
            with open(current_list, 'wb') as fp: #Sla de nieuwe lijst op
                pickle.dump(tebewerkenlijst, fp)
                print(f'Dictionary saved successfully to file: {current_list}')
            lijsten_list.append(curli)
            with open("lijsten_list.pkl", 'wb') as fp: #Werk de lijst van alle bestaande lijsten bij.
                pickle.dump(lijsten_list, fp)
        app.mijn_lijsten(choice=curli)

    #Verwijdert de gekozen lijst#
    def remove_list(app,lijst, lijsten_list):
        del_list = str(lijst.get())+".pkl" #Kies de aangegeven lijst
        os.remove(del_list) #Verwijder het bestand
        lijsten_list.remove(lijst.get())
        with open("lijsten_list.pkl", 'wb') as fp: #Werk de lijst van alle bestaande lijsten bij.
            pickle.dump(lijsten_list, fp)
        app.mijn_lijsten(choice="Nieuwe lijst maken")

    #Checkt voor goed antwoord#
    def check_juist(app,juiste_antwoord,invul,current_list,lijst,startup,term):
        answer_given = invul.get()
        if answer_given.lower() == juiste_antwoord.lower(): #Als het antwoord gelijk is (niet hoofdlettergevoelig):
            juist = True 
        else: #Anders moet het fout zijn:
            juist = False
        app.woordjes_oefenen_quiz(current_list,lijst,startup,juist,juiste_antwoord,term)

###STARTER###
if __name__ == "__main__":
    app = App()
    app.homescreen() #Start de app op