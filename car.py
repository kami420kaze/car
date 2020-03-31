country = input('泥哪國啦: ')
age = input('幾歲啦你: ')
age = int(age)
if country == 'TW':
	if age >= 18:
		print('你可以考駕照了喔')
	else:
		print('乖乖走路')
elif country == 'US':
	if age >= 16:
		print('you can drive lol')
	else:
		print('walk bitch')