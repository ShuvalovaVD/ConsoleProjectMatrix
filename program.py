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
    print("4. Сложение двух матриц")
    print("5. Вычитание двух матриц (из первой матрицы вычитается вторая)")
    print("6. Умножение двух матриц (перед этим будет проверка на возможность умножения")
    print("7. Завершение программы")


def check_matrix_size(rows, columns, matrix):  # проверяет матрицу на симметричность
    # как только находит что-то несимметричное, сразу возвращает False, иначе в самом конце если ничего не нашло - True
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


def check_symmetry_of_matrix(matrix):  # проверяет матрицу на симметричность
    rows = len(matrix)
    columns = len(matrix[0])  # сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    # как только находит что-то несимметричное, сразу возвращает False, иначе в самом конце если ничего не нашло - True
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def check_addition_of_two_matrix(matrix1, matrix2):  # проверяет две матрицы на определённость сложения
    # len(matrix1/2[0]): сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    rows1, columns1 = len(matrix1), len(matrix1[0])
    rows2, columns2 = len(matrix2), len(matrix2[0])
    if rows1 == rows2 and columns1 == columns2:
        return True
    return False


def check_multiplication_of_two_matrix(matrix1, matrix2):  # проверяет две матрицы на определённость умножения
    # len(matrix1/2[0]): сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    rows1, columns1 = len(matrix1), len(matrix1[0])
    rows2, columns2 = len(matrix2), len(matrix2[0])
    if columns1 == rows2:
        return True
    return False


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


def add_two_matrix(matrix1, matrix2):  # складывает две матрицы
    # результат будет складываться в матрицу matrix1
    rows, columns = len(matrix1), len(matrix1[0])
    for i in range(rows):
        for j in range(columns):
            matrix1[i][j] += matrix2[i][j]
    return matrix1


def subtract_two_matrix(matrix1, matrix2):  # вычитает из первой матрицы вторую
    # matrix1 - matrix2 = matrix1 + (-1 * matrix2)
    matrix2 = multiply_matrix_by_number(matrix2, -1)
    matrix_res = add_two_matrix(matrix1, matrix2)
    return matrix_res


def multiply_two_matrix(matrix1, matrix2):
    # len(matrix1/2[0]): сколько чисел (=сколько столбцов) в первой строке, столько и во всех остальных (логично)
    rows1, columns1 = len(matrix1), len(matrix1[0])
    rows2, columns2 = len(matrix2), len(matrix2[0])
    # умножение двух матриц определено, если кол-во столбцов 2-ой = кол-ву строк 1-ой, это уже проверено
    # размер результирующей матрицы: кол-во строк 1-ой и кол-во столбцов 2-ой
    rows_res, columns_res = rows1, columns2
    # изначально заполним результирующую матрицу нулями
    matrix_res = []
    for i in range(rows_res):
        tmp = [0] * columns_res
        matrix_res.append(tmp)
    # при умножении двух матрицы строки первой покоординатно умножаются на столбцы второй
    for i in range(rows_res):
        for j in range(columns_res):
            # ячейка [i][j] результирующей матрицы - это i-ая строка 1-ой, умноженная покоординатно на j-ый столбец 2-ой
            for k in range(columns1):  # или rows2, неважно, они равны, если умножение матриц определено
                matrix_res[i][j] += matrix1[i][k] * matrix2[k][j]  # постепенно покоординатно умножаем
    return matrix_res



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
        elif request == "4":
            while True:
                matrix1 = get_matrix()
                matrix2 = get_matrix()
                check_verdict = check_addition_of_two_matrix(matrix1, matrix2)
                if check_verdict == True:
                    break
                print("Сложение матриц не определено, они должны быть одинакового размера, попробуйте снова:")
            matrix_res = add_two_matrix(matrix1, matrix2)
            show_matrix(matrix_res)
        elif request == "5":
            while True:
                matrix1 = get_matrix()
                matrix2 = get_matrix()
                check_verdict = check_addition_of_two_matrix(matrix1, matrix2)
                if check_verdict == True:
                    break
                print("Сложение матриц не определено, они должны быть одинакового размера, попробуйте снова:")
            matrix_res = subtract_two_matrix(matrix1, matrix2)
            show_matrix(matrix_res)
        elif request == "6":
            while True:
                matrix1 = get_matrix()
                matrix2 = get_matrix()
                check_verdict = check_multiplication_of_two_matrix(matrix1, matrix2)
                if check_verdict == True:
                    break
                print("Умножение матриц не определено, кол-во столбцов 2-ой должно быть = кол-ву строк 1-ой,\
                 попробуйте снова:")
            matrix_res = multiply_two_matrix(matrix1, matrix2)
            show_matrix(matrix_res)
        elif request == "7":
            break
        else:
            print("Ваш запрос не является корректным, необходимо ввести число от 1 до 7, попробуйте снова:")
    print("Завершение программы")


main()
