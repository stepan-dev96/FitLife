print('Добро пожаловать!')

user_name = input('Как Вас зовут? ')
user_age = input('Сколько Вам лет? ')

user_weight = float(input(
    'Укажите Ваш вес в килограммах (например, 80.2): '
))
user_height = float(input(
    'Укажите Ваш рост в метрах (например, 1.65): '
))

bmi = round(user_weight / (user_height ** 2), 1)
print(
    f'\n{user_name}, Ваш индекс массы тела равен: {bmi}',
)

WATER = user_weight * 30/1000
print(f"Рекомендуемая норма воды: {WATER}л.")

report = (
    f'Вот отчет для тебя: {user_name}, {user_age} лет.\n'
    f'Твой индекс массы тела равен: {bmi:.1f}\n'
    f'Рекомендуемая норма воды {WATER:.2f}л.\n'
)
print(f"\n{report}\n")
print("Расчет окончен. Будьте здоровы!")
