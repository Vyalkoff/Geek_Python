# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
#   в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
#   а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
#   в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    dict_name = {}
    for name in args:
        find_space = name[name.find(' ') + 1]
        if find_space not in dict_name:
            dict_name[find_space] = dict()

        if name[0] in dict_name[find_space]:
            dict_name[find_space][name[0]].append(name)
        else:
            dict_name[find_space].setdefault(name[0], [name])
    return dict_name


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Гванов", "Анна Савельева"))
