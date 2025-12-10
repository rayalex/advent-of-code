from utils.io import read_lines_here
from utils.vector import Vector2
from utils.geometry import Rectangle
from itertools import combinations

points = [Vector2(*map(int, line.split(','))) for line in read_lines_here("input.txt", __file__)]

def part1(points: list[Vector2]) -> int:
  max_area = 0
  for i, j in combinations(range(len(points)), 2):
    area = (abs(points[i].x - points[j].x) +1) * (abs(points[i].y - points[j].y) +1)
    if area > max_area:
      max_area = area

  return int(max_area)

def part2(points: list[Vector2]) -> int:
  """
  We seem to have 100k x 100k matrix which we can't 
  reasonably store in our current type (without resorting to numpy backend and/or coordinate compression).

  So instead we create polygon and test against that. We can simplify further
  by testing if within any AABB of a potential rectangle, does any other point falls
  inside of it, or any segments that cross it. If none do (boundaries are fine), it's a valid rectangle
  """
  max_area = 0

  segments: list[tuple[Vector2, Vector2]] = []

  # create all segments between points in sequence - with wrap around last to first
  for i in range(len(points)):
    p1 = points[i]
    p2 = points[(i + 1) % len(points)]
    segments.append((p1, p2))

  for i, j in combinations(range(len(points)), 2):
    p1: Vector2 = points[i]
    p2: Vector2 = points[j]

    # normalize to AABB
    min_x = min(p1.x, p2.x)
    max_x = max(p1.x, p2.x)
    min_y = min(p1.y, p2.y)
    max_y = max(p1.y, p2.y)

    rect = Rectangle(
        x=min_x,
        y=min_y,
        width=max_x - min_x,
        height=max_y - min_y
    )

    # continue if directly contains any other points
    if any(
      rect.contains_vector(points[k]) 
      for k in range(len(points)) 
      if k != i and k != j
    ):
      continue

    if any(
      rect.intersects_segment(seg)
      for seg in segments
    ):
      continue

    area = (max_x - min_x +1) * (max_y - min_y +1)
    if area > max_area:
      max_area = area

  return int(max_area)

print("Part 1:", part1(points))
print("Part 2:", part2(points))
