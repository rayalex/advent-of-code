from utils.io import read_lines_here
from typing import Tuple


lines = read_lines_here("input.txt", __file__)

def _n_longest(input: str, n: int) -> int:
  """
  Finds the largest possible number that can be created
  by selecting (any) N digits in order they appear.

  We select the largest left-most digit as in decimal it will be the largest,
  regardless what is on the right.

  E.g. for N:2 = 436241 -> 64
                   ^ ^
  The core algorithm is essentially a sliding window that:
  1. Starts at the beginning, and ends at the end - N (to acommodate for the entire number)
  2. Looks for the first largest digit in the window
  3. Uses the digit and moves the window after it, repeating the process until we're at the end
  """
  def find_largest(input: str) -> Tuple[int, int]:
    """
    Looks for the largest digit in the string, returns it alongside it's index
    """
    largest = 0
    largestIndex = 0
    for idx, x in enumerate(input):
      if int(x) > largest:
        largest = int(x)
        largestIndex = idx

    return (largest, largestIndex)
  
  digits = ""

  # sliding window
  # window starts on the left and ends at N (length) to ensure we have enough digits remaining
  left, right = 0, len(input) - n
  for i in range(0, n):
    digit, index = find_largest(input[left:right + 1])
    digits += str(digit)

    # move the start of the window after the largest digit and increment the right
    left += index + 1
    right += 1

  return int(digits)

def total_joltage(lines: list[str], batteries: int) -> int:
  return sum(_n_longest(bank, batteries) for bank in lines)

def part1(lines) -> int:
  return total_joltage(lines, 2)

def part2(lines) -> int:
  return total_joltage(lines, 12)

print(part1(lines))
print(part2(lines))