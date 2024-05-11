# контейнеры данных
# списки и кортеджи
# содержать другие обьекты

# основное различие изменяемость (mutability)

# list - список изменяемый
# можно добавитьновые элементы к концу,
# вставить в середину,
# изменить и
# удалить элекменты

# list: append, extend, remove

# numbers = [1, 2,3]
# numbers.insert(0, 0)
# numbers.append(4)
# numbers.extend([5, 6, 7])
# numbers.remove(6)
# del numbers[3]
# print(numbers)
#
#
# integer_tuple = (1,2,3)
# # integer_tuple[0]=(4)
# try:
#     integer_tuple[0]=(4)
# except:
#     print("Не получилось")
# else:
#     print("Получилось")
# task_list = []
# task_list.extend(((2,3),(4,5)))
# print(task_list)
# print(task_list.__sizeof__())
#
# tuple_list = (1, "21", task_list)
# print(tuple_list)
# print(tuple_list.__sizeof__())
#
# numbers = ([1,2], [1, 2])
# print(numbers)
# numbers[0].append(3)
# print(numbers)

# название, описание и координаты
# (ширина и долгота) - постоянные

def using_urgency_level(task):
    return task['urgency']
def using_title_sort(task):
    return task['title']
def using_len_desc(task):
    return len(task['desc'])
tasks = [
    {'title':'Laundry', 'desc' :'Wash clothes', 'urgency':1},
    {'title':'Homework', 'desc' :'Physics + Math', 'urgency':5},
    {'title':'Muserum', 'desc' :'Egyptian things', 'urgency':2}
]

tasks.sort(key=using_len_desc, reverse=True)
for task in tasks:
    print(f"{task}  {len(task['desc'])}")


#
# tasks.sort(key=str)
# for task in tasks:
#     print(task)
#
# tasks.sort(key=using_title_sort )
# for task in tasks:
#     print(task)
#
# tasks.sort(key=using_urgency_level)
# for task in tasks:
#     print(task)
#
#
# tasks.sort(key=lambda x:x['desc'])
# for task in tasks:
#     print(task)
# numbers =  [12,4,1,3,7,5,9,8]
# numbers.sort()
# print(numbers)
# names = ['Danny', 'Aaron', 'Zack', 'Jennife', 'Mike', 'David']
# names.sort()
# print(names)
#
# mixed = [3,1, 2, 'John', ['c', 'd'], ['a','b']]
# mixed.sort(key = str)
# print(mixed)


