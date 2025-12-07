from utils.io import read_lines_here
from utils.matrix import Matrix
from typing import Tuple

manifold = Matrix.from_lines_col(read_lines_here("input.txt", __file__), lambda x: [char for char in x])

def part1(m: Matrix) -> Tuple[int, Matrix]:
  """
  Run row by row and apply:
    - if row above is S or |, but we're not on a splitter generate a beam
    - If row above is | and we're on the splitter generate a beam on the sides (and count the split)
  """
  splits = 0

  for row in range(1, m.rows):
    for col in range(m.cols):
      above = m.get(row - 1, col)
      current = m.get(row, col)
      if above == '|' or above == 'S':
        if current == '^':
          m.set(row, col - 1, '|')
          m.set(row, col + 1, '|')
          splits += 1
        else:
          m.set(row, col, '|')

  return (splits, m)

def part2(solved_manifold: Matrix) -> int:
  paths = [0] * solved_manifold.cols
  paths[solved_manifold.get_row(0).index('S')] = 1

  for row in range(1, solved_manifold.rows):
    current_paths = [0] * solved_manifold.cols

    for col in range(solved_manifold.cols):
      current = solved_manifold.get(row, col)

      if current == '|':
        current_paths[col] += paths[col]

      elif current == '^':
        v = paths[col]
        current_paths[col - 1] += v
        current_paths[col + 1] += v
    paths = current_paths

  return sum(paths)

p1_solution, p1_manifold = part1(manifold)
print("Part 1:", p1_solution)
print("Part 2:", part2(p1_manifold))