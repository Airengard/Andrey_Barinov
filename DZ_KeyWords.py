# 1. Создайте функцию max_number(a, b), которая принимает два числа и возвращает наибольшее из них. Используйте return для возврата результата.
# В функции не должно быть встроенной функции max().
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))


def max_number(a, b):
    if a > b:
        return (a)
    else:
        return (b)


max_digit = max_number(a, b)
print(max_digit)


# 2. Определите функцию empty_function(), которая ничего не делает. Используйте pass в качестве тела функции.
def empty_function():
    pass


print(empty_function())


# 3. Напишите функцию even_numbers( n ) , которая генерирует все четные числа от 0 до n включительно. Используйте yield для возврата каждого четного числа по очереди.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


for num in even_numbers(10):
    print(num)

# 4. Напишите автотест для функции max_number(a, b), созданной в первом задании. Убедитесь, что она возвращает правильные значения для различных пар чисел.
# Используйте assert для проверки условий.
# - Дополнительно, добавьте проверку, что функция правильно работает при передаче одинаковых чисел.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def test_max_number():
    assert max_number(5, 3) == 5, "Ошибка: max_number(5, 3) должно быть 5"
    assert max_number(-1, 1) == 1, "Ошибка: max_number(-1, 1) должно быть 1"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должно быть 0"
    assert max_number(10, 10) == 10, "Ошибка: max_number(10, 10) должно быть 10"
    assert max_number(-5, -10) == -5, "Ошибка: max_number(-5, -10) должно быть -5"


test_max_number()
print("Все тесты пройдены успешно!")
