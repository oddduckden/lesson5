"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""
try:
    out_f = open('out_task1.txt', 'w')
    for x in iter(lambda: input('введите строку: '), ''):
        out_f.write(x + '\n')
finally:
    out_f.close()
# another
try:
    out_str = [x + '\n' for x in iter(lambda: input('введите строку: '), '')]
    out_f = open('out_task1.txt', 'a')
    out_f.writelines(out_str)
finally:
    out_f.close()