camping_kit = {"Спички": 1, "Туалетная бумага": 1, "Вода": 1, "Еда": 2,
               "Фонарик": 1}
list_inventory = []
size = int(input("Введите размер рюкзака в кг.: "))
remained = []

for key, value in camping_kit.items():
    if value <= size:
        size -= value
        list_inventory.append(key)

if len(camping_kit) > len(list_inventory):
    for i in camping_kit:
        if i not in list_inventory:
            remained.append(i)
    print(f"Поместилось {list_inventory}, не поместилось {remained}")
else:
    print(f"Постилось {list_inventory}, ничего не осталось")
