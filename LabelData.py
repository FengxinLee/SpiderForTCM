"""
标注文本
-------------------------

命名实体识别   BIO标注法
标注声明：BIO标注法
症状  SYM   symbol
疾病  DIS   disease
穴位  ACU  acupoint
经络  MCC   main and collateral channels
部位  BOD   body
药品  DRU   drug
器具  APP   appliance
疗法  CUR   cure

"""
STRSET = ['B-SYM', 'I-SYM', 'B-DIS', 'I-DIS', 'B-ACU', 'I-ACU', 'B-BOD', 'I-BOD',
          'B-MCC', 'I-MCC', 'B-DRU', 'I-DRU', 'B-APP', 'I-APP', 'B-CRU', 'I-CRU', 'O']
already_labeled = int(input('请输入已标注行数: '))
print(already_labeled)

now_line = 1
with open('labeldata/label_tuina.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print('当前标注行数： ' + str(now_line))
        now_line = now_line + 1
        if already_labeled != 0:
            already_labeled = already_labeled - 1
            continue

        print('     开始标注')
        line_len = len(line)
        if line_len < 3:
            print('         该行字符数过少，已删除')
            continue
        print('         当前行内容：'+line)
        for word in line:
            char_label = input('         请标注： ' + word)
            if char_label == '':
                with open('labeldata/data_tuina.txt', 'a', encoding='utf-8') as data_file:
                    data_file.write(word + ' O\n')
                continue
            char_label = int(char_label)
            if char_label == 17:    # 删除字符
                continue
            elif char_label == 18:   # 结束当前句子
                with open('labeldata/data_tuina.txt', 'a', encoding='utf-8') as data_file:
                    data_file.write('\n\n')
                    continue
            with open('labeldata/data_tuina.txt', 'a', encoding='utf-8') as data_file:
                data_file.write(word + ' ' + STRSET[char_label] + '\n')
        print('     标注结束')

