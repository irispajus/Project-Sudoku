#############################################
#   Credit: Sirli Põder & Erki Laanemäe     #
#############################################
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
from menyy_ja_salvestamine import loe_salvestatud_tulemus
from sudoku_genereerimine import *
from ajavott import *

class SudokuGUI(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x540")
        self.title("Sudoku")
        # Create a main frame to hold all the other widgets
        self.main_frame = CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both")
        # Create a label widget for the title
        self.title_label = CTkLabel(self.main_frame, text="Sudoku", font=("Verdana", 40))
        self.title_label.pack(pady=15)

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
        self.check_fields_button = CTkButton(self.buttons_frame, text="Check solution", command=self.checkFields)
        self.check_fields_button.pack(pady=5)
        self.reset_board_button = CTkButton(self.buttons_frame, text="Reset board", command=self.resetBoard)
        self.reset_board_button.pack(pady=5)
        self.show_solution_button = CTkButton(self.buttons_frame, text="Show solution", command=self.solve)
        self.show_solution_button.pack(pady=5)
        # Create entry widgets for each cell in the game board
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = CTkEntry(self.board_frame, width=3, font=("Verdana", 16), justify="center", validate="key", validatecommand=(self.register(self.validateInput), "%S"))
                cell.insert(0, str(self.board[i][j]))
                if str(self.board[i][j]) == '':
                    cell.configure(state="normal")
                else:
                    cell.configure(state="readonly")
                row.append(cell)
                cell.grid(row=i, column=j, padx=1, pady=1)
            self.cells.append(row)
        # Get starting time
        global time
        time = getStartingTime()

    # Allow only 1 digit for cell input        
    def validateInput(self, value):
        if value.isdigit() and int(value) in range(1, 10):
            return True
        return False
    
    # Overwrite with the initial board
    def solve(self):
        # Remove the ability to check a solved board
        #self.check_fields_button.destroy()
        #self.show_solution_button.destroy()
        #totalTime = getSpentTime(time)
        #self.time_spent = CTkLabel(self.buttons_frame, text="Mission failed...\nTime spent: " + str(totalTime), font=("Verdana", 12))
        #self.time_spent.pack(pady=10)
        #self.menu_button = CTkButton(self.buttons_frame, text="Back to menu", command=self.backToMenu)
        #self.menu_button.pack(pady=5)
        solved_board = self.full_board
        self.disable_check_button = True
        # Solve the game board
        for i in range(9):
            for j in range(9):
                self.cells[i][j].configure(state="normal")
                self.cells[i][j].delete(0, "end")
                self.cells[i][j].insert(0, str(solved_board[i][j]))
                self.cells[i][j].configure(state="disabled")

    # Delete elements and call out levelSelection()
    def backToMenu(self):
        self.board_frame.destroy()
        self.buttons_frame.destroy()
        self.levelSelection()

    # Create a frame & buttons for level selection
    def levelSelection(self):
        # Create a frame for level selection buttons
        self.level_selection = CTkFrame(self.main_frame)
        self.level_selection.pack(expand=True, fill="both", pady=50, padx=150)
        self.select_level_label = CTkLabel(self.level_selection, text="Choose difficulty:", font=("Verdana", 18))
        self.select_level_label.pack(pady=5)
        # Create buttons
        self.easy = CTkButton(self.level_selection, text="Easy", command=lambda: self.createGameBoard(1))
        self.easy.pack(pady=10)
        self.medium = CTkButton(self.level_selection, text="Medium", command=lambda: self.createGameBoard(2))
        self.medium.pack(pady=10)
        self.hard = CTkButton(self.level_selection, text="Hard", command=lambda: self.createGameBoard(3))
        self.hard.pack(pady=10)
        self.random = CTkButton(self.level_selection, text="Random", command=lambda: self.createGameBoard(0))
        self.random.pack(pady=10)
        self.scoreboard= CTkButton(self.level_selection, text="Scoreboard", command=lambda: self.showScoreboard())
        self.scoreboard.pack(pady=50)
    
    # Display top 5 results
    def showScoreboard(self):
        self.level_selection.destroy()
        self.buttons_frame = CTkFrame(self.main_frame)
        self.buttons_frame.pack()
        self.results_label = CTkLabel(self.buttons_frame, text="Top 5 results", font=("Verdana", 18))
        self.results_label.pack(pady=10)
        self.results_label = CTkLabel(self.buttons_frame, text="Place\t Username\t Result \t\t Date")
        self.results_label.pack(pady=10, padx=10)
        results = loe_salvestatud_tulemus("lahendamise_ajad.txt")[:5]
        for i, (username, result, date) in enumerate(results, 1):
            result_label = CTkLabel(self.buttons_frame, text=f"{i}. \t {username} \t {result} \t {date}")
            result_label.pack()
        self.menu_button = CTkButton(self.buttons_frame, text="Back to menu", command=self.backToMenu)
        self.menu_button.pack(pady=10)

    # Call out checkEntry on every cell & edit cell colors
    def checkFields(self):
        self.boolean = True
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
        if (win):
            self.winWin()
    
    # Reset board
    def resetBoard(self):
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = CTkEntry(self.board_frame, width=3, font=("Verdana", 18), justify="center")
                cell.insert(0, str(self.board[i][j]))
                if (str(self.board[i][j] == '')):
                    cell.configure(state="normal")
                else:
                    cell.configure(state="readonly")
                row.append(cell)
                cell.grid(row=i, column=j, padx=1, pady=1)
            self.cells.append(row)
        time = getStartingTime()

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
            if rida != i and vaartus == self.cells[i][veerg].get() or vaartus == self.board[i][veerg]:
                self.boolean = False
                break
            if veerg != i and vaartus == self.cells[rida][i].get() or vaartus == self.board[rida][i]:
                self.boolean = False
                break
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
    
    # Afer winning..
    def winWin(self):
        totalTime = getSpentTime(time)
        self.buttons_frame.destroy()
        self.win_frame = CTkFrame(self.main_frame)
        self.win_frame.pack()
        self.you_win = CTkLabel(self.win_frame, text="YOU WIN!", font=("Verdana", 30))
        self.you_win.pack()
        self.time_spent = CTkLabel(self.win_frame, text="Time spent: " + str(totalTime), font=("Verdana", 20))
        self.time_spent.pack(pady=10)
        self.save_result_button = CTkButton(self.win_frame, text="Save result", command=lambda: self.askUsername(totalTime))
        self.save_result_button.pack(pady=5)
        self.menu_button = CTkButton(self.win_frame, text="Back to menu", command=self.backToMenu)
        self.menu_button.pack(pady=5)

    # Ask for username
    def askUsername(self, totalTime):
        self.win_frame.destroy()
        self.final_frame = CTkFrame(self.main_frame)
        self.final_frame.pack()
        self.username_entry = CTkEntry(self.final_frame, width=250, placeholder_text = "Username:", font=("Verdana", 16))
        self.username_entry.pack()
        self.save_result_button = CTkButton(self.final_frame, text="Save result", command=lambda: self.saveAndReturn(totalTime))
        self.save_result_button.pack(pady=10)
    
    # Save results to file & return to main menu
    def saveAndReturn(self, totalTime):
        writeToFile(self.username_entry.get(), totalTime)
        self.final_frame.destroy()
        self.backToMenu()

