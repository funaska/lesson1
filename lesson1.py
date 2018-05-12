dict = {'city' : 'Москва', 'temperature' : 20, 'wind' : 'Восточный'}
print(dict['city'])

dict['temperature'] = 21
print(dict['temperature'])

print(len(dict))

print(dict.get('country', 'поля "country" нет в словаре'))

dict ['date'] = '27.05.2017'
print (dict)

dict1 = {'city': 'Москва', 'wind': 'Восточный', 'date': '27.05.2017', 'temperature': 20}
dict2 = {'city': 'Москва', 'wind': 'Северный', 'date': '28.05.2017', 'temperature': 21}
dict3 = {'city': 'Москва', 'wind': 'Западный', 'date': '29.05.2017', 'temperature': 22}

templist = []
templist.append(dict1)
templist.append(dict2)
templist.append(dict3)

print(templist)
