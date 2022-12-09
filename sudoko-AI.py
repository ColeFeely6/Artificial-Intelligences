# Define the function to solve a Sudoku puzzle
def solve_sudoku(grid):
  # Function to find the next empty cell in the grid
  def find_empty_cell(grid):
    for row in range(9):
      for col in range(9):
        if grid[row][col] == 0:
          return (row, col)
    return None

  # Function to check if a number is valid in a given cell
  def is_valid(grid, row, col, num):
    # Check if the number is already in the row or column
    for i in range(9):
      if grid[row][i] == num or grid[i][col] == num:
        return False

    # Check if the number is already in the 3x3 grid
    start_row = row - row%3
    start_col = col - col%3
    for i in range(3):
      for j in range(3):
        if grid[start_row + i][start_col + j] == num:
          return False

    return True

  # Recursive function to solve the puzzle
  def solve(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
      return True

    row, col = empty_cell

    for num in range(1, 10):
      if is_valid(grid, row, col, num):
        grid[row][col] = num

        if solve(grid):
          return True

        grid[row][col] = 0

    return False

  # Solve the puzzle
  if solve(grid):
    return grid
  else:
    return None
