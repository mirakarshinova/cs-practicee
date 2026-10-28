from tablestats import *

def main():
    #ввод названия файла должен делать пользователь, поэтому with open(input())
    #encoding без него берётся кодировка системы, и на другом компьютере русские названия типов прочитаются неверно.
    #with закрывает файл сам, даже если программа упадёт.
    with open(input(), encoding="utf-8") as table:
        rows = read_rows(table)
    
    #вызов функций и возвращенных значений из tablestats
    counts = count_types(rows) #считает сколько записей каждого типа
    print(len(rows)) #сколько записей прочитано
    print(len(counts)) #сколько различных типов;
    print(total_minutes(rows, "ошибка")) #суммарные минуты записей типа ошибка.

    #записываем в файл summary.csv наши даные, используем to_csv(counts) для формирования строки
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

main()









# Используется для того, чтобы функция запустилась только при прямом запуске, и не работала при import.
#if __name__ == "__main__":
#    main()
