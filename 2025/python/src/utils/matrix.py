from typing import TypeVar, Callable, Generic, List

T = TypeVar('T')

class Matrix(Generic[T]):
    def __init__(self, data: List[List[T]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    @staticmethod
    def from_lines(lines: List[str], transform: Callable[[str], T]) -> 'Matrix[T]':
        data = [[transform(char) for char in line] for line in lines]
        return Matrix(data)

    def get(self, row: int, col: int) -> T:
        return self.data[row][col]

    def set(self, row: int, col: int, value: T) -> None:
        self.data[row][col] = value

    def transpose(self) -> 'Matrix[T]':
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)
    
    def __repr__(self) -> str:
        return '\n'.join([''.join([str(item) for item in row]) for row in self.data])