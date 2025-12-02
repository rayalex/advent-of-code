from dataclasses import dataclass
from utils.io import read_lines_here

lines = read_lines_here("input.txt", __file__)

@dataclass
class Dial:
  position: int = 50
  maximum: int = 100 # exclusive

  def rotate_left(self, count) -> None:
    self.position = (self.position - count) % self.maximum

  def rotate_right(self, count) -> None:
    self.position = (self.position + count) % self.maximum

  def is_zero(self) -> bool:
    return self.position == 0

@dataclass
class CountingDial:
  """
  This dial counts actual movement to simulate the clicks 
  (more reasonable than the math to do it)
  """
  position: int = 50
  maximum: int = 100 # exclusive
  zero_count: int = 0

  def _move(self, tick) -> None:
    self.position += tick

    # handle wrap-arrounds 
    if self.position == self.maximum:
      self.position = 0

    if self.position == -1:
      self.position = self.maximum - 1

    # if we're at 0, count it
    if self.position == 0:
      self.zero_count += 1

  def rotate_left(self, count) -> None:
    for i in range(count):
      self._move(-1)

  def rotate_right(self, count) -> None:
    for i in range(count):
      self._move(1)

def part1(turns: list[str]) -> int:
  dial = Dial(50, 100)
  zero_count = 0

  for turn in turns:
    direction, count = turn[0], int(turn[1:])
    if direction == 'L':
      dial.rotate_left(count)
    else:
      dial.rotate_right(count)

    # check if we're at 0
    if dial.is_zero():
      zero_count += 1
  
  return zero_count

def part2(turns: list[str]) -> int:
  dial = CountingDial(50, 100)

  for turn in turns:
    direction, count = turn[0], int(turn[1:])
    if direction == 'L':
      dial.rotate_left(count)
    else:
      dial.rotate_right(count)

  return dial.zero_count

print("Part 1:", part1(lines))
print("Part 2:", part2(lines))