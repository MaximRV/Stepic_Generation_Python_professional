def get_weekday(weekDayNumber: int):
    weekdays = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота",
                7: "Воскресенье", }
    weekDayNumbers = list(range(1,8))
    try:
        if isinstance(weekDayNumber, int):
            raise TypeError('Аргумент не является целым числом')
        if weekDayNumber not in weekDayNumbers:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        return weekdays[weekDayNumber]

    except (TypeError,ValueError) as err:
        print(err)
        return  type(err)

