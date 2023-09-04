import customtkinter as ctk


### Variables ### 

### Functies ###

def main():
    print("Hello world!")
    window()


def window():
    root = ctk.CTk()
    root.geometry("1920x1080")
    ctk.set_appearance_mode("dark")
    root.mainloop()
    window = ctk.CTkFrame(master=root)
    window.pack(pady=0, padx=0, fill="both", expand=True)





if __name__ == "__main__":
    main()