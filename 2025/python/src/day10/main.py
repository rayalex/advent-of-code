from utils.io import read_lines_here
from dataclasses import dataclass
from itertools import combinations
import re as regex

@dataclass(frozen=True)
class Machine:
  lights: list[bool]
  buttons: set[tuple] # set of sets? list of sets? list of tuples? so many endless possibilities!!!

  def __repr__(self) -> str:
    return f"[{''.join(['#' if l else '.' for l in self.lights])}] {self.buttons}"

lines = read_lines_here("input.txt", __file__)
machines: list[Machine] = []

def parse_input():
  for line in lines:
    # extract [#..#] pattern and fill the lights array
    # pattern match is not really needed here, but being pedantic
    lights = regex.findall(r'\[([\.|#]+)\]', line)[0]
    lights = [c == '#' for c in lights] 

    buttons = regex.findall(r'\(.+?\)', line)
    buttons = {tuple(map(int, b.strip("()").split(","))) for b in buttons}

    machine = Machine(lights=lights, buttons=buttons)
    machines.append(machine)

def min_presses(machine: Machine) -> int:
  # pressing the button twice is the same as not pressing it at all (cancels out)
  # so for part1, it's sufficient to evaluate all combinations of buttons
  # and find the minimal one, as search space is very small
  target = machine.lights
  n_lights = len(target)
  n_buttons = len(machine.buttons)

  # try combinations of increasing button lenghts
  for combo_size in range(1, n_buttons + 1):
    for buttons_combo in combinations(machine.buttons, combo_size):
      lights = [False] * n_lights

      # push the button, push, push the button...
      for button_to_push in buttons_combo:
        # flip the light where button indicates
        for light in button_to_push:
          lights[light] = not lights[light]

      # as we're "counting up", return on first match
      if lights == target:
        return combo_size

def part1():
  return sum(min_presses(machine) for machine in machines)

def part2():
  pass 

parse_input()
print("Part 1:", part1())
print("Part 2:", part2())