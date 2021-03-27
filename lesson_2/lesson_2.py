# Using debugging tools inside functions
# Использование инструментов отладки внутри функций

# Task 1.
# Fix bug: division by zero
# ADD +1 ONLY ONE NUMBER to fix it

# Задание 1.
# Исправить баг: деление на ноль
# ДОБАВЬ +1 ТОЛЬКО ОДНОМУ ЧИСЛУ чтобы исправить это


import central_control_panel as ccp

names = [
    'Cтепан Пекшин',
    'Артем Кондрашов',
    'Гумников Александр',
    'Романов Александр',
    'Столповский Алексей',
    'Матвей Лазарев',
    'Влад Федоров'
]


shuttle1 = ccp.SpaceShuttle()


numbers = shuttle1.data
print(numbers)


astronaut0 = ccp.Astronaut(
    astronaut_id=0,
    name=names[0],
    parameters=[
        8, 55, 63, 78, 60, 14, 77, 51, 1, 3, 88, 85, 24, 95, 66, 48,
        80, 3, 77, 46, 16, 38, 37, 98, 7, 13, 18, 86, 53, 80, 12,
        94, 22, 89, 44, 23, 91, 32, 15, 2
    ]
)

astronaut1 = ccp.Astronaut(
    astronaut_id=1,
    name=names[1],
    parameters=[
        45, 70, 85, 29, 87, 31, 13, 92, 74, 80, 90, 35, 43, 54, 91,
        15, 26, 48, 76, 81, 66, 18, 10, 57, 89, 61, 97, 17, 27, 67,
        8, 98, 48, 51, 79, 53, 41, 34, 59, 68
    ]
)

astronaut2 = ccp.Astronaut(
    astronaut_id=2,
    name=names[2],
    parameters=[
        50, 34, 12, 86, 94, 17, 40, 7, 59, 62, 52, 43, 61, 59, 49,
        10, 60, 98, 63, 36, 42, 28, 75, 85, 83, 97, 44, 1, 46, 78,
        32, 71, 29, 87, 33, 30, 38, 92, 89, 73
    ]
)

astronaut3 = ccp.Astronaut(
    astronaut_id=3,
    name=names[3],
    parameters=[
        28, 57, 44, 90, 64, 78, 26, 65, 56, 89, 7, 16, 98, 49, 42,
        96, 62, 25, 37, 21, 75, 77, 3, 34, 33, 92, 97, 61, 69, 23,
        25, 95, 59, 66, 73, 72, 12, 30, 13, 8
    ]
)

astronaut4 = ccp.Astronaut(
    astronaut_id=4,
    name=names[4],
    parameters=[
        66, 55, 53, 74, 95, 54, 1, 33, 79, 92, 87, 42, 7, 4, 5, 83,
        84, 64, 65, 29, 72, 10, 12, 15, 56, 13, 22, 8, 2, 20, 57,
        52, 49, 39, 77, 43, 34, 26, 89, 69
    ]
)

astronaut5 = ccp.Astronaut(
    astronaut_id=5,
    name=names[5],
    parameters=[
        73, 54, 68, 43, 87, 39, 56, 28, 90, 5, 26, 81, 62, 27, 41,
        88, 46, 12, 23, 24, 11, 77, 84, 37, 97, 78, 60, 50, 96, 92,
        82, 67, 47, 10, 52, 39, 13, 98, 2, 14
    ]
)

astronaut6 = ccp.Astronaut(
    astronaut_id=6,
    name=names[6],
    parameters=[
        77, 7, 49, 54, 10, 20, 71, 23, 31, 50, 63, 9, 26, 90, 1, 21,
        92, 62, 73, 30, 11, 72, 84, 44, 46, 12, 81, 98, 88, 36, 52,
        74, 22, 5, 83, 13, 14, 19, 64, 75
    ]
)


vital_parameters_of_astronauts = [
    astronaut0.vital_parameters,
    astronaut1.vital_parameters,
    astronaut2.vital_parameters,
    astronaut3.vital_parameters,
    astronaut4.vital_parameters,
    astronaut5.vital_parameters,
    astronaut6.vital_parameters
]


astronaut_id = 0
i = vital_parameters_of_astronauts[astronaut_id]
print(i)


try:
    number = ccp.Calculation(1, 2, 3, i).result(1)
    number = ccp.Calculation(4, 5, 6, i).result(number)
    number = ccp.Calculation(7, 8, 9, i).result(number)
    number = ccp.Calculation(10, 11, 12, i).result(number)
    number = ccp.Calculation(13, 14, 15, i).result(number)
    number = ccp.Calculation(16, 17, 18, i).result(number)
    number = ccp.Calculation(19, 20, 21, i).result(number)
    number = ccp.Calculation(22, 23, 24, i).result(number)
    number = ccp.Calculation(25, 26, 27, i).result(number)
    number = ccp.Calculation(28, 29, 30, i).result(number)
    number = ccp.Calculation(31, 32, 33, i).result(number)
    number = ccp.Calculation(34, 35, 36, i).result(number)
    number = ccp.Calculation(37, 38, 39, i).result(number)
except ZeroDivisionError:
    number = None
    print('[ENG] Cannot divide by zero', '[РУС] Нельзя делить на ноль')


# Критический параметр полёта космического корабля
# Critical parameter of the spacecraft flight
critical_parameter = number
print('Critical parameter =', critical_parameter)


# Check
# Проверка
check_sum = 0
for astronaut in vital_parameters_of_astronauts:
    check_sum += sum(astronaut)

print('Check_sum =', check_sum)


ccp.Check(
    val1=abs(check_sum - 14085),
    val2=1,
    err_text='[ENG] The parameters should not differ by more than 1.' + '\n' +
             '[РУС] Параметры не должны отличаться больше чем на 1.'
).val1_more_than_val2()
