from utils.io import read_lines_here
from utils.matrix import Matrix
from math import prod
import re

lines = read_lines_here("input.txt", __file__)

# create a matrix by splitting the strings on space(s)
data = Matrix.from_lines_col(lines, lambda x: x.strip().split())

def part1(data_grid: Matrix) -> int:
  """
  Does column wise sum/product where:
  Rows 0-N are the numbers
  Row N is the operation (+ or *)

  Total all the sub operations and return the result which is our solution to the puzzle.
  """
  total = 0

  for col in range(data_grid.cols):
    op = data_grid.get(data_grid.rows - 1, col)
    sublist = []
    for row in range(data_grid.rows - 1):
      sublist.append(int(data_grid.get(row, col)))

    subtotal = sum(sublist) if op == '+' else prod(sublist)
    total += subtotal

  return total

def part2() -> int:
  """
  Treat the entire vertical column as a matrix of characters
  Transpose it and convert rows to ints
  Do the operation on those

  We need to re-parse though, since the operation is aligned on the boundary
  and not all numbers are aligned the same.
  """
  # re-read the file into matrix, but as characters
  data_grid = Matrix.from_lines_col(read_lines_here("input.txt", __file__), lambda x: [char for char in x])

  total = 0
  ops = "".join(data_grid.get_row(data_grid.rows - 1)) # temp back to string for regex

  # use our regex matches as boundaries
  for m in re.finditer(r"[\+|\*]\s+", ops):
    # start, end correspond to columns where our math block is
    start, end = m.start(), m.end()
    op = m.group()[0]

    math_block = data_grid \
      .submatrix(0, data_grid.rows - 1, start, end) \
    
    # iterate cols and extract the number from each (each row is a digit)
    numbers = [int(s) for col in math_block.cols_iter() if (s := "".join(col).strip())]
    total += sum(numbers) if op == '+' else prod(numbers)

  return total

print("Part 1:", part1(data))
print("Part 2:", part2())