"""
处理数据，划分需要进行标注的数据
"""

import random

FILENAME = ['zhenjiu', 'tuina']
BASENAME = './origindata/data_'
JUMPWORD = ['。。', '。。', '。 。', '。。']

for name in FILENAME:
    base = 0
    if name == 'tuina':
        base = 0.1
    else:
        base = 0.05

    file_name = BASENAME + name + '.txt'
    print('正在处理文件 ： ' + file_name)
    write_name = 'label_' + name + '.txt'
    write_name_un = 'unlabel_' + name + '.txt'
    label_list = []
    unlabel_list = []
    i = 1
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            print('     正在处理 第 ' + str(i) + ' 行。。。')
            for word in JUMPWORD:
                line = line.replace(word, ' ')
            if random.random() < base:
                label_list.append(line)
            else:
                unlabel_list.append(line)
            i = i + 1
        with open(write_name, 'w', encoding='utf-8') as write_file:
            for strlin in label_list:
                write_file.write(strlin)
        with open(write_name_un, 'w', encoding='utf-8') as write_file:
            for str_un in unlabel_list:
                write_file.write(str_un)
