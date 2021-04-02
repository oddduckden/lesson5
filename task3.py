"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""


def salary(s):
    person: list = s.split()
    return person[0][:-1], int(person[1])

# first
with open('staff.txt') as f:
    staff_list = [salary(x) for x in f.readlines()]
print(staff_list)
print('Оклад менее 20 тыс.: ', ', '.join([sal[0] for sal in staff_list if sal[1] < 20000]))
print("Средний ежемесячный доход: ", sum([sal[1] for sal in staff_list]) / len(staff_list))
