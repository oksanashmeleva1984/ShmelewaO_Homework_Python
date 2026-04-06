def month_to_season(num):
    if num in [12, 1, 2]:
        return 'Зима'
    elif num in [3, 4, 5]:
        return 'Весна'
    elif num in [6, 7, 8]:
        return 'Лето'
    elif num in [9, 10, 11]:
        return 'Осень'
    else:
        return 'Неверный ввод номера месяца'
