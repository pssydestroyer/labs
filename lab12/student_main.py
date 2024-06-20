class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]
    
    def add_element(self, row, col, value):
        self.data[row][col] = value
    
    def sum_of_rows(self):
        return [sum(row) for row in self.data]
    
    def transpose(self):
        transposed_data = [[self.data[row][col] for row in range(self.rows)] for col in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix
    
    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("ашибка.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.columns))
        return result
    
    def is_symmetric(self):
        if self.rows != self.columns:
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.columns):  
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True
    
    def rotate_right(self):
        rotated_data = [[0]*self.rows for _ in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns):
                rotated_data[j][self.rows - 1 - i] = self.data[i][j]
        self.data = rotated_data
        self.rows, self.columns = self.columns, self.rows 
    
    def flatten(self):
        return [element for row in self.data for element in row]
    
    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0]) if rows > 0 else 0
        mat = Matrix(rows, columns)
        for i in range(rows):
            for j in range(len(list_of_lists[i])):
                mat.data[i][j] = list_of_lists[i][j]
        return mat
    
    def diagonal(self):
        if self.rows != self.columns:
            raise ValueError("Matrix is not square.")
        return [self.data[i][i] for i in range(self.rows)]