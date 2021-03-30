country = input('where are you come frome ')
age = input('how old are you')
age = int (age)
if country == '台灣':
	if age >= 18: 
		print('你可以考駕照')
	else: 
		print('not')
elif country == 'American':
	if age >= 16: 
		print('你可以考駕照')
	else: 
		print('not')
else:
	print('only taiwan/ American')	