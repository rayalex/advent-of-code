from utils.io import read_lines_here
from utils.range import parse_range, Range
from collections import deque


inventory = [int(x) for x in read_lines_here("inventory.txt", __file__)]
ranges = [parse_range(line) for line in read_lines_here("ranges.txt", __file__)]

def part1() -> int:
  """
  We check each item in the inventory against all ranges.
  Given the size of the dataset, we don't do any optimizations / sorting / range merging, etc.
  """
  num_fresh = 0
  for item in inventory:
    # item is considered fresh if it falls within at least one range
    for range in ranges:
      if range.contains(item):
        num_fresh += 1
        break

  return num_fresh

def part2() -> int:
  """
  For part 2, we need to get the actual number of items that can be considered fresh.
  We need to be careful as the ranges can actually overlap.

  Here, we need to be a bit clever and merge ranges that either touch or overlap
  given the actual bounds are in trillions, so the easiest way to solve this
  is to do the merge and then just individually sizes the ranges and add them up

  How we actually solve it:
  - Sort the ranges by the start
  - Put them in queue, in that order (lowest start first)
  - Grab the current range. Pop the ranges if they are mergable, and merge if we can
  - If not, grab the next one and continue until the queue is empty
  """
  sorted_ranges = deque(sorted(ranges, key=lambda r: r.start))
  print(f"Sorted ranges: {[r.start for r in sorted_ranges]}")
  current_range: Range | None = None
  final_ranges: list[Range] = []
  while sorted_ranges:
    range = sorted_ranges.popleft()

    # if our current_range is None, assign it and continue
    if current_range is None:
      current_range = range
    # otherwise, check if we can merge
    else:
      if current_range.can_merge(range):
        # merge
        current_range = current_range.merge(range)
        print("Merged range", current_range)
      else: # otherwise, current range is complete and push it to final
        final_ranges.append(current_range)
        print("Appended range", current_range)
        current_range = range # start again

  # if any range remains, add it
  if current_range is not None:
    print("Appended range", current_range)
    final_ranges.append(current_range)

  # sum up and return
  return sum([r.size_inclusive() for r in final_ranges])

print("Part 1:", part1())
print("Part 2:", part2())
