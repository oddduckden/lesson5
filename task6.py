"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def sort_lessons(lessons_list):
    """
    Из исходного списка занятий возвращает упорядоченный по ключу словарь вид:количество
    :param lessons_list:list
    :return: dict
    """
    res_les = {'(л)': 0, '(пр)': 0, '(лаб)': 0}
    for elm in lessons_list:
        if elm.count('(л)') != 0:
            res_les.update({'(л)': int(elm[:elm.index('(л)')])})
        elif elm.count('(пр)') != 0:
            res_les.update({'(пр)': int(elm[:elm.index('(пр)')])})
        elif elm.count('(лаб)') != 0:
            res_les.update({'(лаб)': int(elm[:elm.index('(лаб)')])})
    return res_les


def symbol_clear(s: str):
    """
    Из исходной строки возвращает словарь занятий
    :param s:str(подстрока занятий по предмету из строки файла)
    :return: dict
    """
    in_symb = ('\n', ') ', '\t',  ' ', '.', ',', '-', '—', 'лекции', 'лекц', 'лек', 'практическиеработы', 'практ')
    out_symb = ('', ');', ';', '', '', ';', ';', ';', 'л', 'л', 'л', 'пр', 'пр')
    for sym in [x for x in zip(in_symb, out_symb)]:
        s = s.replace(sym[0], sym[1])
    return sort_lessons(s.split(';'))


def parser(in_str):
    """
    Из исходной строки возвращает список из строки названия предмета и словаря занятий
    :param in_str:str(элемент из списка строк файла)
    :return:list
    """
    res = list()
    res.append(in_str[:in_str.index(':')])
    res.append(symbol_clear(in_str[in_str.index(':') + 1:]))
    # print(res)
    return res


with open('subjects.txt', 'r') as subj:
    subj_list = subj.readlines()
# print(subj_list)
total = dict()
for el in subj_list:
    r = parser(el)
    total.update({r[0]: sum([x for x in r[1].values()])})
print(total)
