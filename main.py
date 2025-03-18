try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input("Введите желаемое арифметическое действие (+, -, *, /): ")

    if c not in ("+", "-", "*", "/"):
        print("Ошибка: Введено некорректное действие!")
    else:
        if c == "+":
            result = a + b
        elif c == "-":
            result = a - b
        elif c == "*":
            result = a * b
        elif c == "/":
            if b == 0:
                raise ZeroDivisionError("Ошибка: Деление на ноль!")
            result = a / b
        print(f"Результат: {result}")

except ValueError:
    print("Ошибка: Введите число!")
except ZeroDivisionError as e:
    print(e)
finally:
    print("Выход")