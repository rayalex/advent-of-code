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
    
    @staticmethod
    def from_lines_col(lines: List[str], col_transform: Callable[[str], List[T]]) -> 'Matrix[T]':
        data = [col_transform(line) for line in lines]
        return Matrix(data)

    def get(self, row: int, col: int) -> T:
        return self.data[row][col]
    
    def get_row(self, row: int) -> List[T]:
        return self.data[row]
    
    def rows_iter(self):
        for row in self.data:
            yield row

    def cols_iter(self):
        for col in range(self.cols):
            yield [self.data[row][col] for row in range(self.rows)]

    def set(self, row: int, col: int, value: T) -> None:
        self.data[row][col] = value

    def transpose(self) -> 'Matrix[T]':
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)
    
    def submatrix(self, row_start: int, row_end: int, col_start: int, col_end: int) -> 'Matrix[T]':
        sub_data = [row[col_start:col_end] for row in self.data[row_start:row_end]]
        return Matrix(sub_data)
    
    def __repr__(self, sep = '') -> str:
        return '\n'.join([sep.join([str(item) for item in row]) for row in self.data])