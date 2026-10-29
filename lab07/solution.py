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
#def column_range(matrix: list[list[float]], column: int) -> float:
#        arr = np.asarray(matrix, dtype=float)
#        if arr.size ==0 :
            return 0.0
        col = arr[:, column]
        return float(round(col.max()-col.min(),6))
