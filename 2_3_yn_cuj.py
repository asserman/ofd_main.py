# settings ={"font_size": "large", "font": "Arial", "color":"black","align": "center"}
# sets = map(settings.keys(), settings.values())
# print(', '.join(settings.values()))

# merges_style = ', '.join(sets)
# print(merges_style)
#
# tasks = ["HomeWork", "Grocery", "Landry", "Museum Trip", "Buy Furniture"]
# note = ", ".join(tasks)
# print("Remaining Tasks: ", note)
# tasks.remove("Buy Furniture")
# tasks.remove("HomeWork")
# note = ", ".join(tasks)
# print("Remaining Tasks: ", note)
#
# tasks_data = """1001, Homework, 5
# 1002, Laundry, 3
# 1003, Grocery, 4"""
# processed_tasks= []
# for data_line in tasks_data.split("\n"):
#     processed_task = data_line.split(",")
#     processed_tasks.append(processed_task)
# print(processed_tasks)