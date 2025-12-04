from utils.io import read_lines_here
from utils.matrix import Matrix

lines = read_lines_here("input.txt", __file__)

# construct a matrix of single character strings
grid = Matrix.from_lines(lines, lambda x: x)

def is_roll(grid: Matrix, x: int, y: int) -> bool:
  return grid.get(x, y) == '@'

def is_accessible(grid: Matrix, x: int, y: int) -> bool:
  # TODO: This can also check is roll
  # check the bounding box for any rolls
  # ignore out of bounds or self (center)
  roll_count = 0
  max_rolls = 4

  for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
      check_x = x + i
      check_y = y + j

      # skip oob
      if check_x < 0 or check_y < 0 or check_x >= grid.rows or check_y >= grid.cols:
        continue

      # skip self
      if check_x == x and check_y == y:
        continue

      if grid.get(check_x, check_y) == '@':
        roll_count += 1

  return roll_count < max_rolls

def part1(paper_grid: Matrix) -> int:
  """
  Count the accessible rolls of paper. 
  
  The roll is acessible if it's surrounded by fewer than four other rolls.
  """
  accessible_rolls = 0

  for x in range(paper_grid.rows):
    for y in range(paper_grid.cols):
      # check if roll
      if is_roll(paper_grid, x, y):
        accessible_rolls += 1 if is_accessible(paper_grid, x, y) else 0

  return accessible_rolls

def part2(paper_grid: Matrix) -> int:
  """
  Count the rolls of paper that can be removed
  
  The roll is acessible if it's surrounded by fewer than four other rolls.
  We need to keep removing the rolls until there are no more left that are acessible.
  """
  removed_rolls = 0

  def remove_rolls() -> int:
    # TODO: this is not ideal as we're mutating the matrix while iterating
    removed = 0
    for x in range(paper_grid.rows):
      for y in range(paper_grid.cols):
        # check if roll and accessible
        if is_roll(paper_grid, x, y) and is_accessible(paper_grid, x, y):
          # remove it
          paper_grid.set(x, y, '.')
          removed += 1

    return removed
  
  while True:
    newly_removed = remove_rolls()
    if newly_removed == 0:
      break

    removed_rolls += newly_removed

  return removed_rolls 

print("Part 1:", part1(grid))
print("Part 2:", part2(grid))