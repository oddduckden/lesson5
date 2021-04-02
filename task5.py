"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task5_file.txt', 'w') as sum_f:
    sum_f.write(' '.join([str(x) for x in range(1, 21, 2)]))
with open('task5_file.txt', 'r') as sum_f:
    # print(sum([int(x) for x in sum_f.read().replace(' ', '') for x in x]))