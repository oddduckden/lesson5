"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open('enterprises_rus.txt', 'r') as in_f:
    firms = [x[:-1].split('\t') for x in in_f]
    print(firms)
profit_list = [x for x in [int(item[-2]) - int(item[-1]) for item in firms] if x >= 0]
average_profit = {'average_profit': sum(profit_list) / len(profit_list)}
profit_dict = dict()
for item in firms:
    item.append(int(item[2]) - int(item[3]))
    profit_dict.update({item[0]: item[-1]})
res = [profit_dict, average_profit]
print(res)
with open('task7_file.json', 'w') as json_f:
    json.dump(res, json_f)
