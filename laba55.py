
my_list = [10, 25, 7, 7, 7, 14, 10, 3]

unique_values = set()
repeated_values = set()

for num in my_list:
    if num in unique_values:
        repeated_values.add(num)
    else:
        unique_values.add(num)

if repeated_values:
    print("Повторяющиеся элементы в списке:", repeated_values)
else:
    print("В списке нет повторяющихся элементов")

print("Исходный список:", my_list)


