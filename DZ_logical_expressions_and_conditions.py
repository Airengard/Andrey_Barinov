# Напишите программу, которая проверяет, можно ли человеку голосовать на выборах.
# Условия:
# Возраст должен быть 18 лет или старше.
# Человек должен быть гражданином страны.
# Человек не должен быть дисквалифицирован (например, по причине уголовного наказания).
def can_vote(age, is_citizen, is_disqualified):
    return age >= 18 and is_citizen and not is_disqualified


age = int(input("Введите ваш возраст: "))
is_citizen = input("Вы гражданин страны (да/нет)? ").lower() == 'да'
is_disqualified = input("Имеется ли у Вас судимость (да/нет)? ").lower() == 'да'

if can_vote(age, is_citizen, is_disqualified):
    print("Вы можете голосовать на выборах!")
else:
    print("Вы не можете голосовать на выборах.")
