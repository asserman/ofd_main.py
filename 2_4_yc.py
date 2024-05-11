# import re
#
# task_pattern_r = re.compile(r"\\task")
# texts = ["\task", "\\task", "\\\task", "\\\\task", ]
# for text in texts:
#     print(f"Match {text!r}: {task_pattern_r.match(text)}")
#
import re

text_data = '''
533, random; record
101, Homework; Complete physics and math some random nonsense
102, Laundry; Wash all the clothes today
103, Museum; All about Egypt
1234, random; record
Another random record
'''


# # tasks = []
# r= r"(?P<task_id>\d{3}), (?P<task_title>\w+); (?P<task_desc>.+)]"
# regex = re.compile(r)
# # print(text_data, )
# print(regex.match(text_data))
# for ma in regex.match(text_data):
#     if ma:
#         print(ma.groupdict())



# for line in text_data.split("\n"):
#     match = regex.match(line)
#     if match:
#         print(f"{'Matched: ':<12}{match.group()}")
#         task= (match.group('task_title'), match.group('task_id'), match.group('task_desc'))
#         tasks.append(task)
#     else:
#         print(f"{'No Match':<12}{line}")
#
# print(tasks)
# s = regex.findall(text_data)
#
# print(type(s))
# for da  in s:
#     print(f"{da[0]:<10}{da[1]:<20}{da[2]:^40}")