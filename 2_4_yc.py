# import re
#
# task_pattern_r = re.compile(r"\\task")
# texts = ["\task", "\\task", "\\\task", "\\\\task", ]
# for text in texts:
#     print(f"Match {text!r}: {task_pattern_r.match(text)}")
#
import re

text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""
tasks = []
r= r"(?P<task_id>\d{3}), (?P<task_title>\w+); (?P<task_desc>.+)"
regex = re.compile(r)
for line in text_data.split("\n"):
    match = regex.match(line)
    if match:
        print(f"{'Matched: ':<12}{match.group()}")
        task= (match.group('task_title'), match.group('task_id'), match.group('task_desc'))
        tasks.append(task)
    else:
        print(f"{'No Match':<12}{line}")

print(tasks)