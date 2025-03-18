try:
    a = int(input("Введите превое число: "))
    b = int(input("Введите второе число: "))
    result = a / b
except ValueError:
    print("Ошибка, введите число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Выход")