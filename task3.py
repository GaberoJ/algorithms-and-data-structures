"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def reverse_number(number):
    digit = number % 10
    number = number // 10
    if number == 0:
        return str(digit)
    else:
        return str(digit) + str(reverse_number(number))


user_number = int(input('Введите число: '))
# Проверка на число, оканчивающееся на 0
while str(user_number)[-1] == '0':
    user_number = user_number // 10
print('Перевернутое число:', reverse_number(user_number))























