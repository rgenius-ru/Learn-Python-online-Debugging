# Using debugging tools
# Использование инструметов отладки

# Task 1.
# Fix bug: division by zero
# ADD +1 ONLY ONE NUMBER to fix it

# Задание 1.
# Исправить баг: деление на ноль
# ДОБАВЬ +1 ТОЛЬКО ОДНОМУ ЧИСЛУ чтобы исправить это


space_shuttle_data = list(range(100))  # Данные из Космического Шаттла

numbers = space_shuttle_data
print(numbers)

vital_parameters_of_astronauts = [  # Жизненные показатели космонавтов
    [8, 55, 63, 78, 60, 14, 77, 51, 1, 3, 88, 85, 24, 95, 66, 48,
     80, 3, 77, 46, 16, 38, 37, 98, 7, 13, 18, 86, 53, 80, 12,
     94, 22, 89, 44, 23, 91, 32, 15, 2],

    [45, 70, 85, 29, 87, 31, 13, 92, 74, 80, 90, 35, 43, 54, 91,
     15, 26, 48, 76, 81, 66, 18, 10, 57, 89, 61, 97, 17, 27, 67,
     8, 99, 48, 51, 79, 53, 41, 34, 59, 68],

    [50, 34, 12, 86, 94, 17, 40, 7, 59, 62, 52, 43, 61, 59, 49,
     10, 60, 98, 63, 36, 42, 28, 75, 85, 83, 97, 44, 1, 46, 78,
     32, 71, 29, 87, 33, 30, 38, 92, 89, 73],

    [28, 57, 44, 90, 64, 78, 26, 65, 56, 89, 7, 16, 98, 49, 42,
     96, 62, 25, 37, 21, 75, 77, 3, 34, 33, 92, 97, 61, 69, 23,
     25, 95, 59, 66, 73, 72, 12, 30, 13, 8],

    [66, 55, 53, 74, 95, 54, 1, 33, 79, 92, 87, 42, 7, 4, 5, 83,
     84, 64, 65, 29, 72, 10, 12, 15, 56, 13, 22, 8, 2, 20, 57,
     52, 49, 39, 77, 43, 34, 26, 89, 69],

    [73, 54, 68, 43, 87, 39, 56, 28, 90, 5, 26, 81, 62, 27, 41,
     88, 46, 12, 23, 24, 11, 77, 84, 37, 97, 78, 60, 50, 96, 92,
     82, 67, 47, 10, 52, 39, 13, 99, 2, 14],

    [77, 7, 49, 54, 10, 20, 71, 23, 31, 50, 63, 9, 26, 90, 1, 21,
     92, 62, 73, 30, 11, 72, 84, 44, 46, 12, 81, 98, 88, 36, 52,
     74, 22, 5, 83, 13, 14, 19, 64, 75]
    ]

astronaut = 5
i = vital_parameters_of_astronauts[astronaut]
print(i)


try:
    i1 = i[1]
    i2 = i[2]
    i3 = i[3]
    number = numbers[i1] - numbers[i2] - numbers[i3]
    number = numbers[i3] / number

    i1 = i[4]
    i2 = i[5]
    i3 = i[6]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[7]
    i2 = i[8]
    i3 = i[9]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[10]
    i2 = i[11]
    i3 = i[12]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[13]
    i2 = i[14]
    i3 = i[15]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[16]
    i2 = i[17]
    i3 = i[18]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[19]
    i2 = i[20]
    i3 = i[21]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[22]
    i2 = i[23]
    i3 = i[24]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[25]
    i2 = i[26]
    i3 = i[27]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[28]
    i2 = i[29]
    i3 = i[30]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[31]
    i2 = i[32]
    i3 = i[33]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[34]
    i2 = i[35]
    i3 = i[36]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

    i1 = i[37]
    i2 = i[38]
    i3 = i[39]
    number = (numbers[i1] - numbers[i2] - numbers[i3]) / number
    number = numbers[i3] / number

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

if abs(check_sum - 14088) > 1:
    print(
        '[ENG] The parameters should not differ by more than 1.',
        '[РУС] Параметры не должны  отличаться больше чем на 1.'
    )
