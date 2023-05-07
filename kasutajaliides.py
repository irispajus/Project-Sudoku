import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkEntry, set_default_color_theme, CTkLabel

set_default_color_theme("green") #värvide lisamine miskipärast ei tööta 
#app = CTk()
#app.configure (bg = 'green', fg = 'white')

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sudoku")
        self.main_frame = CTkFrame(self)
        self.main_frame.pack (expand = True, fill = "both")

        self.nameLabel = CTkLabel (self.main_frame, text = "Sudokude lahendamine")
        self.nameLabel.pack (padx = 100, pady = 20, fill = "x")

        self.nameEntry = CTkEntry(self.main_frame,
                            placeholder_text = "Kasutajanimi")
        self.nameEntry.pack (padx = 100,pady = 50, fill = "x")
        

        self.nameEntry = CTkEntry(self.main_frame,
                            placeholder_text = "Parool")
        self.nameEntry.pack (padx = 100,pady = 5, fill = "x")
        

app = App()
app.geometry("600x540")
app.mainloop()