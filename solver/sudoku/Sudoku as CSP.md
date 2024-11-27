# Sudoku as CSP

## **Components of Sudoku as a CSP**

1. **Variables**:
   - Each cell in the Sudoku grid is a variable. For a standard \(9 \times 9\) Sudoku, there are 81 variables (\(V_{1,1}, V_{1,2}, \ldots, V_{9,9}\)).

2. **Domains**:
   - Each variable's domain is the set of possible values it can take, typically \(\{1, 2, 3, \ldots, 9\}\).
   - Pre-filled cells have a domain restricted to their assigned value.

3. **Constraints**:
   Sudoku has three main types of constraints:
   - **Row Constraint**: Each number \(1\) through \(9\) must appear exactly once in each row.
   - **Column Constraint**: Each number \(1\) through \(9\) must appear exactly once in each column.
   - **Subgrid Constraint**: Each \(3 \times 3\) subgrid (or "box") must contain each number \(1\) through \(9\) exactly once.

   These constraints ensure that no two variables in the same row, column, or subgrid can have the same value.

4. **Objective**:
   - Assign a value to every variable such that all constraints are satisfied.

---

## **Formulating Sudoku as a CSP**

1. **Representation**:
   - Variables: Represent each cell as \(V_{i,j}\), where \(i\) is the row index and \(j\) is the column index.
   - Domains: Each \(V_{i,j}\) has a domain of \(\{1, 2, 3, \ldots, 9\}\), or a single fixed value if pre-filled.
   - Constraints: Use binary constraints to ensure that any two variables in the same row, column, or subgrid have different values.

2. **Example**:
   Consider a partial Sudoku grid:

   ```text
   5 3 . | . 7 . | . . .
   6 . . | 1 9 5 | . . .
   . 9 8 | . . . | . 6 .
   ------+-------+------
   8 . . | . 6 . | . . 3
   4 . . | 8 . 3 | . . 1
   7 . . | . 2 . | . . 6
   ------+-------+------
   . 6 . | . . . | 2 8 .
   . . . | 4 1 9 | . . 5
   . . . | . 8 . | . 7 9
   ```

   - Variables: \(V_{1,1} = 5\), \(V_{1,2} = 3\), \(V_{1,3} = \{1, 2, 4, 6, 8, 9\}\), etc.
   - Constraints:
     - \(V_{1,3} \neq V_{1,4}, V_{1,3} \neq V_{2,3}, \ldots\) for row, column, and subgrid constraints.

---

## **Techniques to Solve Sudoku as a CSP**

1. **Constraint Propagation**:
   - **Forward Checking**: Whenever a value is assigned to a variable, remove that value from the domain of all connected variables.
   - **Arc Consistency (AC-3)**: Ensure that for every pair of connected variables, there exists a consistent assignment.

2. **Search Algorithms**:
   - **Backtracking Search**: Try assigning values to variables sequentially while checking constraints.
   - **Heuristics**:
     - **Minimum Remaining Values (MRV)**: Choose the variable with the smallest remaining domain.
     - **Degree Heuristic**: Choose the variable involved in the most constraints.
     - **Least Constraining Value (LCV)**: Choose the value that leaves the most options for neighboring variables.

3. **Combining Propagation and Search**:
   - Use constraint propagation to simplify the puzzle and reduce domains before applying backtracking.

---

## **Comparison: Sudoku vs Calcudoku as CSPs**

| Feature           | Sudoku                                | Calcudoku                             |
|--------------------|---------------------------------------|---------------------------------------|
| **Variables**      | 81 cells in a \(9 \times 9\) grid     | Cells in an \(N \times N\) grid       |
| **Domains**        | \(\{1, 2, \ldots, 9\}\)              | \(\{1, 2, \ldots, N\}\)               |
| **Constraints**    | Row, Column, Subgrid                 | Row, Column, Cage                     |
| **Operations**     | No arithmetic operations             | Arithmetic operations (+, -, *, /)    |

---

## **Conclusion**

Sudoku can indeed be expressed as a CSP, as like Calcudoku. In fact, CSP techniques like constraint propagation and backtracking are commonly used in solving Sudoku puzzles programmatically. Both Sudoku and Calcudoku share a similar CSP structure, but Calcudoku introduces additional complexity with its arithmetic constraints.
