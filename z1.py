# -*- coding: cp1251 -*-
from random import uniform


def main():
    print("Лабораторная работа №4. Одномерные массивы. Вариант 5.")

    # 1. Ввод данных
    try:
        n = int(input("Введите количество элементов N (N<=30): "))
        if n > 30:
            n = 30
        elif n < 1:
            n = 1

        a = float(input("Введите начало интервала [a, b] для удаления: a = "))
        b = float(input("Введите конец интервала [a, b] для удаления: b = "))

        # Генерация массива
        mas = []
        print("\nИсходный массив:")
        for i in range(n):
            val = uniform(-10, 10)  # Генерируем числа от -10 до 10 для наглядности
            mas.append(val)
            print(f"{val:7.2f}", end="")
        print()

        # --- ЗАДАНИЕ 1: Поиск максимального элемента ---
        max_el = mas[0]
        for i in range(1, n):
            if mas[i] > max_el:
                max_el = mas[i]

        print(f"\n1. Максимальный элемент: {max_el:.2f}")

        # --- ЗАДАНИЕ 2: Сумма элементов до последнего положительного ---
        last_pos_index = -1  # Индекс последнего положительного

        # Ищем индекс последнего положительного элемента
        for i in range(n):
            if mas[i] > 0:
                last_pos_index = i

        sum_before_last_pos = 0.0
        if last_pos_index != -1:
            # Суммируем элементы с 0 по last_pos_index (не включая его)
            for i in range(last_pos_index):
                sum_before_last_pos += mas[i]
            print(
                f"2. Сумма элементов до последнего положительного (индекс {last_pos_index}): {sum_before_last_pos:.2f}")
        else:
            print("2. Положительных элементов в массиве нет.")

        # --- ЗАДАНИЕ 3: Сжатие массива (удаление элементов из [a, b]) ---
        # Алгоритм "сжатия": переписываем нужные элементы в начало списка
        j = 0  # Индекс для записи "хороших" элементов

        for i in range(n):
            # Если элемент НЕ попадает в интервал [a, b], оставляем его
            # Условие попадания в интервал: a <= mas[i] <= b
            # Значит, условие сохранения: not (a <= mas[i] <= b)
            if not (a <= mas[i] <= b):
                mas[j] = mas[i]
                j += 1

        # Заполняем освободившееся место в конце нулями
        for i in range(j, n):
            mas[i] = 0.0

        print(f"\n3. Массив после сжатия (удалены элементы из [{a}, {b}]):")
        for i in range(n):
            print(f"{mas[i]:7.2f}", end="")
        print()

    except ValueError:
        print("Ошибка ввода данных.")


if __name__ == "__main__":
    main()