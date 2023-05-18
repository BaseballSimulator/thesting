import numpy as np
from sudoku import Sudoku

# Generate solved Sudoku puzzles
num_puzzles = 1000
puzzles = []
solutions = []

for _ in range(num_puzzles):
    puzzle = Sudoku(3).difficulty(0.7).generate()
    solution = puzzle.solve()
    puzzles.append(puzzle.board)
    solutions.append(solution.board)

# Convert the puzzles and solutions into suitable formats
training_puzzles = np.array(puzzles[:800])
training_solutions = np.array(solutions[:800])
test_puzzles = np.array(puzzles[800:])
test_solutions = np.array(solutions[800:])

# Reshape the puzzle arrays to match the input shape of the model
training_puzzles = training_puzzles.reshape((-1, 9, 9))
test_puzzles = test_puzzles.reshape((-1, 9, 9))
