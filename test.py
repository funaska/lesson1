people_dict = { 'Виталик' : { 'city': 'Тула','temperature' : 25, 'wind' : 'NE'} , 'Марина' : { 'city': 'Саров','temperature' : 22, 'wind' : 'NE'}, 'Серёга' : { 'city': 'Воронеж','temperature' : 12, 'wind' : 'NE'} }

name = input('Введите имя: ')

print(people_dict.get(name, 'нет такого пользователя') )
