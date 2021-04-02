"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def number_dictionary(number):
    dictionary = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    return dictionary[number]


def parser(next_string: str):
    el = next_string[:-1].split() if next_string[:-1] == '\n' else next_string.split()
    el[0] = number_dictionary(int(el[-1]))
    return ' '.join(el)

# first
in_f = open('numbers.txt', 'r')
out_f = open('result.txt', 'w')
for line in in_f:
    out_f.writelines(parser(line) + '\n')
in_f.close()
out_f.close()
