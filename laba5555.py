

group1 = ["Иванов", "Кательникова", "Сидоров", "Козловский", "Айропетов", "Квашонкин", "Малой", "Андреев", "Мерзализаде", "Качмазов"]
group2 = ["Аранова", "Лалаева", "Пушкин", "Иванов", "Малой", "Овечкин", "Колыбелкин", "Орлов", "Еременко", "Коваль"]

sports_team = tuple(group1[:5] + group2[:5])

print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", sports_team)

print("Длина кортежа:", len(sports_team))

sorted_team = tuple(sorted(sports_team))
print("Отсортированная команда:", sorted_team)

ivanov_count = sorted_team.count("Иванов")
if ivanov_count > 0:
    print("Фамилия Иванов входит в команду.")
    print("Количество вхождений фамилии Иванов в команду:", ivanov_count)
else:
    print("Фамилия Иванов не входит в команду.")


