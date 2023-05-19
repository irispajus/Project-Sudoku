#############################
#   Credit: Erki Laanemäe   #
#############################
from kasutajaliides import SudokuGUI
from customtkinter import CTk

if __name__ == "__main__":
    # Loo GUI ja implementeeri sudoku väli
    app = SudokuGUI()
    app.mainloop()
    # Lõpeta programmi töö peale akna sulgemist 
    app.after_cancel(SystemExit())