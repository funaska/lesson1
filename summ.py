def get_summ(one, two, delimeter=' '):
	return str(one.upper()) + str(delimeter) + str(two.upper())

result = get_summ('Hello','world',',')
print(result)
