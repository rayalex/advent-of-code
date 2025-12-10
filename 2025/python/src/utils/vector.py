from dataclasses import dataclass

LineSegment = tuple['Vector2', 'Vector2']

@dataclass(frozen=True)
class Vector2:
    x: float
    y: float

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)

    def dot(self, other: 'Vector2') -> float:
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self) -> 'Vector2':
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector2(self.x / mag, self.y / mag)
    
    @staticmethod
    def distance(v1: 'Vector2', v2: 'Vector2') -> float:
        return ( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 ) ** 0.5

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other: 'Vector3') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: 'Vector3') -> 'Vector3':
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self) -> 'Vector3':
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector3(self.x / mag, self.y / mag, self.z / mag)
    
    @staticmethod
    def distance(v1: 'Vector3', v2: 'Vector3') -> float:
        return ( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2 ) ** 0.5

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"