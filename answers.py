# Задание 1
# Создайте новый файл answers.py в Sublime
# Создайте словарь, описывающий типичный диалог. Пример {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
# Создайте функцию get_answer, которая принимает ключ(строку) и словарь и отдает элемент словаря по ключу
# Приведите ключ, передаваемый в функцию к нижнему регистру (например: "ПриВеТ" => "привет"), используйте "ПриВеТ".lower()

# dialogue={'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}

# def get_answer(key,dialogue):
# 	return dialogue.get(key,'чё?')

# print(get_answer('ПриВет'.lower(), dialogue))
# print(get_answer('Как деЛа'.lower(), dialogue))
# print(get_answer('ПоКа'.lower(), dialogue))
# print(get_answer('Fuck this shit'.lower(), dialogue))

dialogue={'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}

def get_answer(key,dialogue):
	return dialogue.get(key,'чё?')

hi1=input('Скажи привет')
print(get_answer('ПриВет'.lower(), dialogue))
hi2=input('Скажи как дела')
print(get_answer('Как деЛа'.lower(), dialogue))
hi3=input('Попрощайся')
print(get_answer('ПоКа'.lower(), dialogue))
shit=input('Что-то ещё')
print(get_answer('Fuck this shit'.lower(), dialogue))