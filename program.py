'''
Запуск программы начинается с функции main(), которая вызывает все остальные функции. В функциях реализовано 
отлавливание исключений (try-except), а также проверки на корректность введённых данных (check_matrix_size, 
check_matrix_on_square), чтобы программа не прерывала свою работу, если пользователь неправильно введёт данные,
программа будет запрашивать ввод до тех пор, пока он не будет осущетсвлён корректно.
'''


def show_menu():  # выводит меню команд
    print("Выберите операцию из списка (укажите номер 1-7):")
    print("1. Умножение матрицы на число")
    print("2. Транспонирование матрицы")
    print("3. Проверка матрицы на симметричность")
    # пункты 4-6 пока не реализованы
    print("4. Сложение двух матриц")
    print("5. Вычитание двух матриц (из первой матрицы вычитается вторая)")
    print("6. Умножение двух матриц (перед этим будет проверка на возможность умножения")
    print("7. Завершение программы")


def check_matrix_size(rows, columns, matrix):  # проверяет матрицу на симметричность
    if len(matrix) != rows:
        return False
    for i in range(rows):
        if len(matrix[i]) != columns:
            return False
    return True


def check_matrix_on_square(matrix):  # проверяет матрицу на квадратность (число строк = числу столбцов)
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    if rows == columns:
        return True
    return False


def check_symmetry_of_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def get_matrix():  # вводит одну матрицу от пользователя
    print("Введите размеры матрицы через пробел (количество строк и столбцов):")
    while True:  # цикл будет работать, пока пользователь не введёт верно размеры матрицы
        try:
            rows, columns = map(int, input().split())
        except ValueError:
            print("Вы ввели данные в неправильном формате, попробуйте снова:")
        else:
            if rows <= 0 or columns <= 0:
                print("В матрице должна быть хотя бы одна строка и хотя бы один столбец, попробуйте снова:")
                continue
            break
    print("Введите матрицу из целых чисел:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                tmp = [int(x) for x in input().split()]
            except ValueError:
                print(f"Вы ввели данные в неправильном формате, попробуйте снова ввести строку №{i + 1}:")
            else:
                matrix.append(tmp)
                break
    check_verdict = check_matrix_size(rows, columns, matrix)
    if check_verdict == False:
        print("Размеры матрицы не соответствуют матрице, попробуйте снова:")
        matrix = get_matrix()
    return matrix


def get_number():  # вводит одно число от пользователя
    print("Введите целое число:")
    while True:  # цикл будет работать, пока пользователь не введёт верно целое число
        try:
            number = int(input())
        except ValueError:
            print("Вы ввели данные в неправильном формате, попробуйте снова:")
        else:
            break
    return number


def show_matrix(matrix):  # выводит матрицу
    print("Итоговая матрица:")
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    for i in range(rows):
        for j in range(columns):
            print(f"{matrix[i][j]:4d}", end=" ")
        print()


def multiply_matrix_by_number(matrix, number):  # умножает матрицу на число
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] *= number
    return matrix


def transpone_matrix(matrix):  # транспонирует матрицу (меняет местами строки и столбцы)
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    new_rows, new_columns = columns, rows
    # изначально заполним новую (транспонированную) матрицу нулями
    new_matrix = []
    for i in range(new_rows):
        tmp = [0] * new_columns
        new_matrix.append(tmp)
    # теперь перезаписываем новую матрицу
    for j in range(columns):
        for i in range(rows):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def main():  # главная функция, к-рая запускает программу
    print("Данная программма реализует операции над матрицами")
    while True:
        show_menu()
        request = input()
        if request == "1":
            matrix = get_matrix()
            number = get_number()
            matrix = multiply_matrix_by_number(matrix, number)
            show_matrix(matrix)
        elif request == "2":
            matrix = get_matrix()
            matrix = transpone_matrix(matrix)
            show_matrix(matrix)
        elif request == "3":
            print("Помните: на симметричность можно проверять только квадратные матрицы")
            while True:  # цикл будет работать, пока пользователь не введёт квадратную матрицу
                matrix = get_matrix()
                check_verdict = check_matrix_on_square(matrix)
                if check_verdict == True:
                    break
                print("Вы ввели не квадратную матрицу, попробуйте снова:")
            check_verdict = check_symmetry_of_matrix(matrix)
            if check_verdict == True:
                print("Матрица симметрична")
            else:
                print("Матрица не симметрична")
        elif request == "7":
            break
        else:
            print("Ваш запрос не является корректным, необходимо ввести число от 1 до 7, попробуйте ещё раз")
    print("Завершение программы")


main()
