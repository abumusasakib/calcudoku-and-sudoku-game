import tkinter as tk
from tkinter import messagebox
import random


class PuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Puzzle Game: Sudoku or Calcudoku")

        # Menu bar
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # Help menu
        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Game Rules", command=self.show_help)
        self.menu.add_cascade(label="Help", menu=help_menu)

        # Game type selection
        self.game_type = tk.StringVar(value="Sudoku")
        tk.Label(master, text="Select Game:").pack(pady=5)
        tk.Radiobutton(master, text="Sudoku", variable=self.game_type, value="Sudoku", command=self.start_game).pack()
        tk.Radiobutton(master, text="Calcudoku", variable=self.game_type, value="Calcudoku", command=self.start_game).pack()

        # Difficulty selector for Sudoku and Calcudoku
        tk.Label(master, text="Select Difficulty:").pack(pady=5)
        self.difficulty = tk.StringVar(value="Medium")
        tk.Radiobutton(master, text="Easy", variable=self.difficulty, value="Easy", command=self.start_game).pack()
        tk.Radiobutton(master, text="Medium", variable=self.difficulty, value="Medium", command=self.start_game).pack()
        tk.Radiobutton(master, text="Hard", variable=self.difficulty, value="Hard", command=self.start_game).pack()

        # Frame for the grid
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(pady=10)

        # Control buttons
        tk.Button(master, text="Validate Solution", command=self.validate_solution).pack(pady=5)

        self.start_game()

    def start_game(self):
        """
        Start the selected game by setting up the grid.
        """
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        if self.game_type.get() == "Sudoku":
            self.setup_sudoku()
        elif self.game_type.get() == "Calcudoku":
            self.setup_calcudoku()

    def generate_sudoku_board(self):
        """
        Generate a random valid Sudoku board using backtracking.
        """
        def is_valid(board, row, col, num):
            # Check row
            if num in board[row]:
                return False
            # Check column
            if num in [board[i][col] for i in range(9)]:
                return False
            # Check 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def fill_board(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        random_nums = list(range(1, 10))
                        random.shuffle(random_nums)
                        for num in random_nums:
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if fill_board(board):
                                    return True
                                board[row][col] = 0
                        return False
            return True

        # Start with an empty board
        board = [[0] * 9 for _ in range(9)]
        fill_board(board)
        return board

    def remove_cells_sudoku(self, board):
        """
        Remove cells from a completed Sudoku board to create a puzzle.
        Difficulty levels determine the number of cells removed.
        """
        difficulty_levels = {"Easy": 30, "Medium": 40, "Hard": 50}
        cells_to_remove = difficulty_levels.get(self.difficulty.get(), 40)

        puzzle = [row[:] for row in board]
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                cells_to_remove -= 1
        return puzzle

    def setup_sudoku(self):
        """
        Set up the Sudoku grid with a random puzzle.
        """
        self.grid_size = 9
        self.solution = self.generate_sudoku_board()
        self.puzzle = self.remove_cells_sudoku(self.solution)

        self.grid = [[tk.StringVar(value="" if self.puzzle[i][j] == 0 else str(self.puzzle[i][j]))
                      for j in range(self.grid_size)] for i in range(self.grid_size)]

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.puzzle[i][j]
                if value == 0:
                    entry = tk.Entry(self.grid_frame, textvariable=self.grid[i][j], width=2, justify="center")
                    entry.grid(row=i, column=j, padx=2, pady=2)
                else:
                    label = tk.Label(self.grid_frame, text=str(value), width=2, justify="center", relief="ridge", bg="lightgray")
                    label.grid(row=i, column=j, padx=2, pady=2)

    def generate_calcudoku_board(self):
        """
        Generate a random valid Calcudoku board with cages and constraints.
        """
        size = 4
        board = [[0] * size for _ in range(size)]

        def is_valid(board, row, col, num):
            if num in board[row]:
                return False
            if num in [board[i][col] for i in range(size)]:
                return False
            return True

        def fill_board(board):
            for row in range(size):
                for col in range(size):
                    if board[row][col] == 0:
                        nums = list(range(1, size + 1))
                        random.shuffle(nums)
                        for num in nums:
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if fill_board(board):
                                    return True
                                board[row][col] = 0
                        return False
            return True

        fill_board(board)
        return board


    def create_calcudoku_cages(self, board, difficulty):
        """
        Create random cages for the Calcudoku board with arithmetic constraints.
        Adjust the number of cages and their size based on difficulty.
        """
        size = len(board)
        cages = []
        visited = [[False] * size for _ in range(size)]

        # Set the number of cages and maximum cage size based on difficulty
        if difficulty == "Easy":
            num_cages = 4
            max_cage_size = 2
        elif difficulty == "Medium":
            num_cages = 6
            max_cage_size = 3
        elif difficulty == "Hard":
            num_cages = 6
            max_cage_size = 4

        def get_random_operation():
            return random.choice(["+", "-", "*", "/"])

        def find_unvisited_neighbors(row, col):
            """Find unvisited adjacent cells."""
            neighbors = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < size and 0 <= new_col < size and 
                    not visited[new_row][new_col]):
                    neighbors.append((new_row, new_col))
            return neighbors

        attempts = 0
        max_attempts = 100  # Prevent infinite loop

        print(f"Creating cages for {difficulty} difficulty")

        while len(cages) < num_cages and attempts < max_attempts:
            # Find an unvisited cell to start a new cage
            start_row, start_col = None, None
            for i in range(size):
                for j in range(size):
                    if not visited[i][j]:
                        start_row, start_col = i, j
                        break
                if start_row is not None:
                    break

            if start_row is None:
                print("No unvisited cells remaining")
                break

            # Create a new cage
            cage = [(start_row, start_col)]
            visited[start_row][start_col] = True
            current_size = 1

            # Attempt to expand cage
            while current_size < max_cage_size:
                # Find unvisited neighbors of current cage
                possible_neighbors = []
                for cell in cage:
                    possible_neighbors.extend(find_unvisited_neighbors(cell[0], cell[1]))
                
                if not possible_neighbors:
                    break

                # Randomly select a neighbor to add
                new_cell = random.choice(possible_neighbors)
                cage.append(new_cell)
                visited[new_cell[0]][new_cell[1]] = True
                current_size += 1

            # Calculate the cage clue
            cells = [board[x][y] for x, y in cage]
            operation = get_random_operation()
            
            if operation == "+":
                clue = sum(cells)
            elif operation == "-":
                clue = abs(cells[0] - cells[1]) if len(cells) == 2 else sum(cells)
            elif operation == "*":
                clue = 1
                for c in cells:
                    clue *= c
            elif operation == "/":
                clue = max(cells) // min(cells) if len(cells) == 2 else sum(cells)
            
            cages.append((clue, operation, cage))
            
            print(f"Created cage: clue={clue}, operation={operation}, cells={cage}")
            attempts += 1

        print(f"Total cages created: {len(cages)}")
        return cages

    def setup_calcudoku(self):
        """
        Set up the Calcudoku grid with a random puzzle and cages.
        """
        self.grid_size = 4
        self.solution = self.generate_calcudoku_board()
        self.cages = self.create_calcudoku_cages(self.solution, self.difficulty.get())

        self.grid = [[tk.StringVar(value="") for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Create a dictionary to map cell coordinates to cage labels
        cage_labels = {}
        for clue, operation, cells in self.cages:
            label = f"{clue}{operation if operation else ''}"
            for x, y in cells:
                cage_labels[(x, y)] = label

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                entry = tk.Entry(self.grid_frame, textvariable=self.grid[i][j], width=2, justify="center")
                entry.grid(row=i * 2, column=j, padx=2, pady=2)  # Place cells on even rows

                if (i, j) in cage_labels:
                    # Adjust the label row to be on the next row (i * 2 + 1)
                    label = tk.Label(self.grid_frame, text=cage_labels[(i, j)], font=("Arial", 8), bg="white")
                    label.grid(row=i * 2 + 1, column=j)  # Place labels below cells


    def validate_calcudoku_solution(self):
        """
        Validate the Calcudoku solution based on the rules.
        """
        # Check row and column uniqueness
        for i in range(self.grid_size):
            row_values = set()
            col_values = set()
            for j in range(self.grid_size):
                row_val = self.grid[i][j].get()
                col_val = self.grid[j][i].get()
                if row_val.isdigit():
                    row_val = int(row_val)
                    if row_val in row_values or not (1 <= row_val <= self.grid_size):
                        return False, f"Invalid value in row {i + 1}."
                    row_values.add(row_val)
                else:
                    return False, f"Empty cell in row {i + 1}."
                if col_val.isdigit():
                    col_val = int(col_val)
                    if col_val in col_values or not (1 <= col_val <= self.grid_size):
                        return False, f"Invalid value in column {i + 1}."
                    col_values.add(col_val)
                else:
                    return False, f"Empty cell in column {i + 1}."

        # Check cage constraints
        for clue, operation, cells in self.cages:
            values = [int(self.grid[x][y].get()) for x, y in cells]
            if operation == "+" and sum(values) != clue:
                return False, f"Cage {clue}+ is invalid."
            elif operation == "-" and abs(values[0] - values[1]) != clue:
                return False, f"Cage {clue}- is invalid."
            elif operation == "*" and eval("*".join(map(str, values))) != clue:
                return False, f"Cage {clue}* is invalid."
            elif operation == "/" and max(values) // min(values) != clue:
                return False, f"Cage {clue}/ is invalid."

        return True, "Congratulations! Your Calcudoku solution is correct."

    def validate_solution(self):
        """
        Validate the user's solution for Sudoku or Calcudoku.
        """
        if self.game_type.get() == "Sudoku":
            self.validate_sudoku_solution()
        elif self.game_type.get() == "Calcudoku":
            valid, message = self.validate_calcudoku_solution()
            if valid:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Validation Error", message)

    def show_help(self):
        """
        Show the game rules in a messagebox.
        """
        rules = (
            "Sudoku Rules:\n"
            "1. Fill the grid so that every row, column, and 3x3 subgrid contains the numbers 1 through 9.\n\n"
            "Calcudoku Rules:\n"
            "1. Fill the grid so that every row and column contains the numbers 1 through N (grid size).\n"
            "2. Satisfy the arithmetic clues for each cage (sum, product, difference, or division).\n"
            "3. Numbers may not repeat within any row or column."
        )
        messagebox.showinfo("Game Rules", rules)


if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGame(root)
    root.mainloop()
