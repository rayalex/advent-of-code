from utils.io import read_lines_here
from utils.vector import Vector3
from collections import defaultdict
from math import prod
from itertools import combinations

points = [Vector3(*map(int, line.split(','))) for line in read_lines_here("input.txt", __file__)]

def part1(points: list[Vector3], lim: int) -> int:
  pairs: list[tuple[float, Vector3, Vector3]] = [] # (distance, point1, point2)
  for i, j in combinations(range(len(points)), 2):
      d = Vector3.distance(points[i], points[j])
      pairs.append((d, points[i], points[j]))

  sorted_pairs = sorted(pairs)[:lim]
  networks: list[set[Vector3]] = []
  for d, p1, p2 in sorted_pairs:
    found_networks = []
    for net in networks:
      if p1 in net or p2 in net:
        found_networks.append(net)

    if len(found_networks) == 0:
      # create new network
      networks.append(set([p1, p2]))
    elif len(found_networks) == 1:
      # add to existing network
      found_networks[0].add(p1)
      found_networks[0].add(p2)
    else:
      # merge networks
      new_net = set()
      for net in found_networks:
        new_net.update(net)
        networks.remove(net)
      new_net.add(p1)
      new_net.add(p2)
      networks.append(new_net)

  # get top 3 largest networks and return product of their sizes
  top_three = sorted(
    networks,
    key = len,
    reverse=True
  )[:3]
  return prod(len(net) for net in top_three)

def part2(points: list[Vector3]) -> int:
  # same as the above, just keep connecting until all points are connected
  # and return x*x of the last two points connected
  pairs: list[tuple[float, Vector3, Vector3]] = [] # (distance, point1, point2)
  for i, j in combinations(range(len(points)), 2):
      d = Vector3.distance(points[i], points[j])
      pairs.append((d, points[i], points[j]))
  sorted_pairs = sorted(pairs)    
  networks: list[set[Vector3]] = []
  last_connected: tuple[Vector3, Vector3] = (points[0], points[0])
  for d, p1, p2 in sorted_pairs:
    found_networks = []
    for net in networks:
      if p1 in net or p2 in net:
        found_networks.append(net)

    if len(found_networks) == 0:
      # create new network
      networks.append(set([p1, p2]))
    elif len(found_networks) == 1:
      # add to existing network
      found_networks[0].add(p1)
      found_networks[0].add(p2)
    else:
      # merge networks
      new_net = set()
      for net in found_networks:
        new_net.update(net)
        networks.remove(net)
      new_net.add(p1)
      new_net.add(p2)
      last_connected = (p1, p2)
      networks.append(new_net)

    if len(networks) == 1:
      break
  return int(last_connected[0].x * last_connected[1].x)

def find_closest(target: Vector3, points: list[Vector3]) -> Vector3:
  return min(
    (p for p in points if p != target),
    key = lambda p: abs(Vector3.distance(p, target))
  )

print("Part 1:", part1(points, 1000))
print("Part 2:", part2(points))