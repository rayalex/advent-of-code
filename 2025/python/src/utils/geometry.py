from dataclasses import dataclass
from utils.vector import Vector2, LineSegment

@dataclass(frozen=True)
class Rectangle:
    x: float
    y: float
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

    def contains_vector(self, v: 'Vector2') -> bool:
        return self.contains_point(v.x, v.y)

    def contains_point(self, px: float, py: float) -> bool:
        return (self.x < px < self.x + self.width) and (self.y < py < self.y + self.height)
    
    @staticmethod
    def segments_intersect(seg1: 'LineSegment', seg2: 'LineSegment') -> bool:
        """
        Check if two line segments properly intersect (cross each other).
        """
        p1, p2 = seg1
        p3, p4 = seg2
        
        def cross_product(o: Vector2, a: Vector2, b: Vector2) -> float:
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
        
        # TODO:: Cross product is already part of Vector2/Vector2
        d1 = cross_product(p3, p4, p1)
        d2 = cross_product(p3, p4, p2)
        d3 = cross_product(p1, p2, p3)
        d4 = cross_product(p1, p2, p4)
        
        # Segments properly intersect if they cross each other
        # This happens when the endpoints are on opposite sides of each other
        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
            ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True
        
        # If we reach here, segments don't properly cross
        # They might touch or be collinear, but that's allowed
        return False

    def intersects_segment(self, seg: 'LineSegment') -> bool:
        # any point of segment inside rectangle?
        if self.contains_vector(seg[0]) or self.contains_vector(seg[1]):
            return True
        
        # intersect with rectangle edges?
        edges = [
            (Vector2(self.x, self.y), Vector2(self.x + self.width, self.y)),  # bottom
            (Vector2(self.x + self.width, self.y), Vector2(self.x + self.width, self.y + self.height)),  # right
            (Vector2(self.x + self.width, self.y + self.height), Vector2(self.x, self.y + self.height)),  # top
            (Vector2(self.x, self.y + self.height), Vector2(self.x, self.y)),  # left
        ]

        for edge in edges:
            if Rectangle.segments_intersect(seg, edge):
                return True
            
        return False

    def intersects(self, other: 'Rectangle') -> bool:
        return not (self.x + self.width < other.x or
                    self.x > other.x + other.width or
                    self.y + self.height < other.y or
                    self.y > other.y + other.height)
    