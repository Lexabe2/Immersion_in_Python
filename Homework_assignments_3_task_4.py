# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# ** какие вещи взяли все три друга
# ** какие вещи уникальны, есть только у одного друга
# ** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.

friends = {
    'Вася': ('палатка', 'спальник', 'горелка', 'еда'),
    'Петя': ('спальник', 'перекус', 'одежда'),
    'Коля': ('палатка', 'спальник', 'горелка', 'одежда', 'одеяло')
}

all_items = set.intersection(*[set(friends[friend]) for friend in friends])

unique_items = set()
for friend in friends:
    unique_items.update(set(friends[friend]) - all_items)

one_friend_items = {}
for friend in friends:
    for item in set(friends[friend]) - all_items:
        if item in one_friend_items:
            one_friend_items[item].append(friend)
        else:
            one_friend_items[item] = [friend]

print('Вещи, которые взяли все три друга:', ', '.join(all_items))
print('Уникальные вещи:', ', '.join(unique_items))
print('Вещи, которые есть у всех кроме одного:')
for item in one_friend_items:
    if len(one_friend_items[item]) == 2:
        print(item, '- нет у', one_friend_items[item][0])
