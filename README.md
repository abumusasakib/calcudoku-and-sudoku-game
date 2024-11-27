# Puzzle Game Solver

This repository contains a **Puzzle Game Solver** with two main puzzle types: **Sudoku** and **Calcudoku**. The project includes both a **game interface** for interactive play (with difficulty customization) and a **solver** directory with pre-generated puzzle inputs and solutions.

## Project Structure

```text
.
├── game.py
├── README.md
└── solver
    ├── calcudoku
    │   ├── calcudoku_solver.ipynb
    │   ├── input1.txt
    │   ├── input2.txt
    │   ├── input3.txt
    │   ├── output1.txt
    │   ├── output2.txt
    │   └── output3.txt
    └── sudoku
        ├── input1.txt
        ├── input2.txt
        ├── input3.txt
        ├── output1.txt
        ├── output2.txt
        ├── output3.txt
        ├── Sudoku as CSP.md
        └── sudoku_solver.ipynb
```

## Features

### 1. **Interactive Puzzle Game**

- The game allows you to play **Sudoku** or **Calcudoku**.
- You can choose between **Easy**, **Medium**, or **Hard** difficulty levels for **Calcudoku**.
- In **Sudoku**, the traditional 9x9 grid is presented with validation for rows, columns, and subgrids.
- In **Calcudoku**, the user has to solve the puzzle by satisfying the arithmetic clues within cages, with validation for the cages’ sum, product, difference, or division constraints.

### 2. **Puzzle Solver**

- The **solver** directory contains two subfolders: `calcudoku` and `sudoku`.
- Each subfolder includes:
  - Input files with predefined puzzle configurations (e.g., `input1.txt`, `input2.txt`, `input3.txt`).
  - Output files that contain the solutions to the corresponding input puzzles.
  - Jupyter notebooks (`calcudoku_solver.ipynb` and `sudoku_solver.ipynb`) to solve the puzzles programmatically.
  
### 3. **Solver Logic**

- **Calcudoku Solver**:
  - The Calcudoku solver works by using backtracking and validating the constraints for cages (sum, product, difference, or division).
  
- **Sudoku Solver**:
  - The Sudoku solver uses a backtracking approach with row, column, and subgrid constraints to find the solution.

## Installation and Usage

### Prerequisites

- **Python 3.x** or higher
- **Tkinter** for the interactive GUI (included with most Python installations)
- **Jupyter Notebook** to run the solver notebooks (for solving puzzles programmatically)

### Running the Game

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the `game.py` file to start the interactive puzzle game.

```bash
python game.py
```

This will launch a GUI where you can select the puzzle type (Sudoku or Calcudoku) and difficulty level, and start playing.

### Running the Solver

To solve predefined puzzles programmatically, you can use the Jupyter notebooks provided:

1. Navigate to the `solver/calcudoku` or `solver/sudoku` directory.
2. Open the corresponding `.ipynb` notebook in Jupyter:

```bash
jupyter notebook calcudoku_solver.ipynb
```

or

```bash
jupyter notebook sudoku_solver.ipynb
```

The notebook will automatically load the input puzzle from the `inputX.txt` file and compute the solution, saving it to the corresponding `outputX.txt` file.

## Game Rules

### **Sudoku Rules**

1. Fill the grid so that every row, column, and 3x3 subgrid contains the numbers 1 through 9.
2. Each number can only appear once per row, column, and subgrid.

### **Calcudoku Rules**

1. Fill the grid so that every row and column contains the numbers 1 through N (grid size).
2. Satisfy the arithmetic clues for each cage (sum, product, difference, or division).
3. Numbers may not repeat within any row or column.

## Contributing

Feel free to open issues or submit pull requests if you would like to improve the project.
