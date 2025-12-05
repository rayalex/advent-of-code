from dataclasses import dataclass

@dataclass
class Range:
  start: int
  end: int

  def contains(self, value: int) -> bool:
    return self.start <= value <= self.end
  
  def size(self) -> int:
    return self.end - self.start
  
  def size_inclusive(self) -> int:
    # to accomodate ranges being open ended (e.g. 1-1 still has 1 element)
    return self.size() + 1
  
  def can_merge(self, range: "Range") -> bool:
    """
    Checks if ranges can be merged. The given range must start on or after this one.
    """
    if(range.start < self.start):
      raise Exception(f"Merged range {range} must have start offset after the current one {self}")
    
    # if other start falls within start-end(inclusive)
    if self.contains(range.start):
      return True
    
    return False
  
  def merge(self, other: "Range") -> "Range":
    return Range(min(self.start, other.start), max(self.end, other.end))
  
  def __repr__(self) -> str:
    return f"Range({self.start}-{self.end})"
  

def parse_range(line: str) -> Range:
  start_str, end_str = line.strip().split("-")
  return Range(int(start_str), int(end_str))