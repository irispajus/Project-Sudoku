from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
from sudoku_genereerimine import *

class SudokuGUI(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x540")
        self.title("Sudoku")
        # Create a main frame to hold all the other widgets
        self.main_frame = CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both")
        # Create a label widget for the title
        self.title_label = CTkLabel(self.main_frame, text="Sudoku", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        self.levelSelection()

    def createGameBoard(self, level):
        # Destroy level selection buttons & frame
        self.level_selection.destroy()
        # Create a frame to hold the game board
        self.board_frame = CTkFrame(self.main_frame)
        self.board_frame.pack(pady=10)
        # Generate a new game board
        self.board = main()
        self.deepCopy()
        self.board = tyhjenda(self.board, level)
        # Create buttons
        self.buttons_frame = CTkFrame(self.main_frame)
        self.buttons_frame.pack(pady=10)
        self.exit_button = CTkButton(self.buttons_frame, text="Check", command=self.checkFields)
        self.exit_button.pack(pady=5)
        self.exit_button = CTkButton(self.buttons_frame, text="Reset board", command=self.resetBoard)
        self.exit_button.pack(pady=5)
        self.exit_button = CTkButton(self.buttons_frame, text="Show solution", command=self.solve)
        self.exit_button.pack(pady=5)
        # Create entry widgets for each cell in the game board
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = CTkEntry(self.board_frame, width=3, font=("Helvetica", 16), justify="center", validate="key", validatecommand=(self.register(self.validateInput), "%P"))
                cell.insert(0, str(self.board[i][j]))
                if str(self.board[i][j]) == '':
                    cell.configure(state="normal")
                else:
                    cell.configure(state="readonly")
                row.append(cell)
                cell.grid(row=i, column=j, padx=1, pady=1)
            self.cells.append(row)
        #print(self.cells)

    # Allow only 1 digit for cell input        
    def validateInput(self, value):
        if len(value) > 1:
            return False
        return value.isdigit()
    
    # Overwrite with the initial board
    def solve(self):
        solved_board = self.full_board
        # Solve the game board
        for i in range(9):
            for j in range(9):
                self.cells[i][j].configure(state="normal")
                self.cells[i][j].delete(0, "end")
                self.cells[i][j].insert(0, str(solved_board[i][j]))
                self.cells[i][j].configure(state="disabled")

    # Create a frame & buttons for level selection
    def levelSelection(self):
        # Create a frame for level selection buttons
        self.level_selection = CTkFrame(self.main_frame)
        self.level_selection.pack(expand=True, fill="both")
        # Create buttons
        self.easy = CTkButton(self.level_selection, text="Easy", command=lambda: self.createGameBoard(1))
        self.easy.pack(pady=10)
        self.medium = CTkButton(self.level_selection, text="Medium", command=lambda: self.createGameBoard(2))
        self.medium.pack(pady=10)
        self.hard = CTkButton(self.level_selection, text="Hard", command=lambda: self.createGameBoard(3))
        self.hard.pack(pady=10)
        self.random = CTkButton(self.level_selection, text="Random", command=lambda: self.createGameBoard(0))
        self.random.pack(pady=10)
    
    # ToDo:
    def checkFields(self):
        win = True
        self.boolean = False
        for i in range(9):
            for j in range(9):
                if (self.cells[i][j].cget("state") != "readonly"):
                    self.checkEntry(i, j)
                    if self.boolean and self.cells[i][j].get != '':
                        self.cells[i][j].configure(fg_color="green")
                    else:
                        win = False
                        self.cells[i][j].configure(fg_color="red")
                #self.cells[i][j].configure(state="readonly")
        if (win):
            self.buttons_frame.destroy()
            self.win_frame = CTkFrame(self.main_frame)
            self.win_frame.pack()
            self.you_win = CTkLabel(self.win_frame, text="YOU WIN!", font=("Helvetica", 30))
            self.you_win.pack()
    
    # Reset board
    def resetBoard(self):
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = CTkEntry(self.board_frame, width=3, font=("Helvetica", 16), justify="center")
                cell.insert(0, str(self.board[i][j]))
                if (str(self.board[i][j] == '')):
                    cell.configure(state="normal")
                else:
                    cell.configure(state="readonly")
                row.append(cell)
                cell.grid(row=i, column=j, padx=1, pady=1)
            self.cells.append(row)

    # Create a copy of the solved board
    def deepCopy(self):
        self.full_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.full_board[i][j] = self.board[i][j]
    
    #sudoku reeglid: ühes reas ja veerus ei tohi sama number korduda
    def checkEntry (self, rida, veerg):
        self.boolean = True
        vaartus = self.cells[rida][veerg].get()
        for i in range(9):
            if vaartus == self.cells[i][veerg] or vaartus == self.cells[rida][i] or vaartus == self.board[i][veerg] or vaartus == self.board[rida][i]:
                self.boolean = False
        #väiksemas väljas (3x3) ei tohi samuti numbrid korduda
        read = (rida // 3) * 3
        veerud = (veerg // 3) * 3
        for i in range(read, read + 3):
            for j in range(veerud, veerud + 3):
                if rida == i and veerg == j:
                    break
                if self.cells[i][j].get() == vaartus or self.board[i][j] == vaartus:
                    self.boolean = False
                    break
            if not self.boolean:
                break


# Create an instance of the SudokuGUI class and run the main loop
#gui = SudokuGUI()
#gui.mainloop()
