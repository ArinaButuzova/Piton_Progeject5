
days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

num_weekend = int(input("Сколько выходных дней на неделе вы хотите? "))


if num_weekend > len(days_of_week) -2:
    print("Ошибка! В неделе всего 7 дней, включая выходные.")
else:
    weekend_days = list(days_of_week[-num_weekend:])
    work_days = list(days_of_week[:-num_weekend])

    print("Ваши выходные дни:", ", ".join(weekend_days))
    print("Ваши рабочие дни:", ", ".join(work_days))
