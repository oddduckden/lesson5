"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
# используем файл, созданный в задании 1
f = open('out_task1.txt', 'r')
source_list = [list(x.split()) for x in f.readlines()]
f.close()
print('Число строк: ', len(source_list))
for i in source_list:
    print(f'В строке "', ' '.join(i), '" слов: ', len(i), sep ='')