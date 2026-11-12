import numpy as np
#список строк по width значений
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.asarray(values, dtype=float)
    if width <=0 or arr.size % width != 0:
        return []
    return arr.reshape(-1, width).tolist()

#участок таблицы: указанные строки и столбцы в заданном порядке
def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows,columns)].tolist()

#среднее по каждому столбцу
def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    return np.round(arr.mean(axis=0),6).tolist()

#размах значений в столбце: наибольшее минус наименьшее
def column_range(matrix: list[list[float]], column: int) -> float:
        arr = np.asarray(matrix, dtype=float)
        if arr.size ==0 :
            return 0.0
        col = arr[:, column]
        return float(round(col.max()-col.min(),6))




import numpy as np


# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# Задание 2. Индексы и срезы в векторе

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

central_fragment = temperatures[0:2, 1:3]

print("\nЗадание 3")
print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:", temperatures[:2, 1:])
print("Центральный фрагмент:\n", central_fragment)
print("Форма центрального фрагмента:", central_fragment.shape)


# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)

first_three_rows = matrix[:3, :]
last_two_rows = matrix[-2:, :]
first_two_columns = matrix[:, :2]
specified_fragment = matrix[1:4, 2:5]
bottom_right_block = matrix[3:5, 3:5]

print("\nЗадание 4")
print("Первые три строки:\n", first_three_rows)
print("Форма:", first_three_rows.shape)

print("Последние две строки:\n", last_two_rows)
print("Форма:", last_two_rows.shape)

print("Первые два столбца:\n", first_two_columns)
print("Форма:", first_two_columns.shape)

print("Строки с индексами 1–3 и столбцы с индексами 2–4:\n",
      specified_fragment)
print("Форма:", specified_fragment.shape)

print("Правый нижний блок 2×2:\n", bottom_right_block)
print("Форма:", bottom_right_block.shape)


# Задание 5. Изменение массивов с помощью срезов

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

print("\nПримеры изменения срезами")
print("vector:", vector)
print("small_matrix:\n", small_matrix)

# copy() создает отдельную копию массива.
# Поэтому изменения changed_hours не изменят исходный hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("\nИзмененный hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Измененная matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)


# Задание 6. Изменение формы

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("numbers:", numbers)
print("Форма numbers:", numbers.shape)

print("table:\n", table)
print("Форма table:", table.shape)

print("transposed:\n", transposed)
print("Форма transposed:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12,
# а в numbers ровно 12 элементов.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а изменить форму массива из 12 элементов на 15 элементов нельзя.
