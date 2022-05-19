# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text1.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        s = line.split(' ')
        print(f'Слов {len(s)}')
print(f'Количество строк {len(lines)}')
f.close()
