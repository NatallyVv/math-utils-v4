# matrix_operations.py - Математические операции с матрицами

def transpose_matrix(matrix):
    """Транспонирование матрицы"""
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Создаем новую матрицу с перевернутыми размерами
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

def find_min_element(matrix):
    """Нахождение минимального элемента и его индексов"""
    if not matrix:
        return None, -1, -1
    
    min_value = matrix[0][0]
    min_row, min_col = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row, min_col = i, j
    
    return min_value, min_row, min_col

def find_max_element(matrix):
    """Нахождение максимального элемента и его индексов"""
    if not matrix:
        return None, -1, -1
    
    max_value = matrix[0][0]
    max_row, max_col = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j
    
    return max_value, max_row, max_col

def matrix_sum(matrix1, matrix2):
    """Сложение двух матриц"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def scalar_multiply(matrix, scalar):
    """Умножение матрицы на скаляр"""
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j] * scalar)
        result.append(row)
    
    return result

def is_square_matrix(matrix):
    """Проверка, является ли матрица квадратной"""
    if not matrix:
        return False
    return len(matrix) == len(matrix[0])

def get_main_diagonal(matrix):
    """Получение главной диагонали матрицы"""
    if not is_square_matrix(matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    
    return diagonal

def get_secondary_diagonal(matrix):
    """Получение побочной диагонали матрицы"""
    if not is_square_matrix(matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    diagonal = []
    n = len(matrix)
    for i in range(n):
        diagonal.append(matrix[i][n - 1 - i])
    
    return diagonal

if __name__ == "__main__":
    # Пример использования
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Тестовая матрица:")
    for row in test_matrix:
        print(row)
    
    min_val, min_i, min_j = find_min_element(test_matrix)
    print(f"\nМинимальный элемент: {min_val} на позиции [{min_i}][{min_j}]")
    
    max_val, max_i, max_j = find_max_element(test_matrix)
    print(f"Максимальный элемент: {max_val} на позиции [{max_i}][{max_j}]")
