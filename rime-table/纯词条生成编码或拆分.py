# -*- coding: utf-8 -*-
import os
import re
import time
import linecache
import tkinter as tk
from tkinter import filedialog
 
root = tk.Tk()
root.withdraw()
target_cizubiao_path =  filedialog.askopenfilename(title='请选择【纯中文词条】文本文件', filetypes=[('Text', '*.txt'), ('All Files', '*')])        # 词组表
if target_cizubiao_path == '':
    print("您没有选择任何文件，已停止")
    os._exit(0)
target_word_path = filedialog.askopenfilename(title='请选择【单行单义】的五笔单字/拆分码表，格式【汉字+Tab+编码】', filetypes=[('Text', '*.txt'), ('All Files', '*')])                          # 单字-编码或拆分 对应表
if target_word_path == '':
    print("您没有选择任何文件，已停止")
    os._exit(0)
    
_line1 = linecache.getline(target_cizubiao_path, 3)
contain_en = bool(re.search('[a-z]|\t', _line1))
if contain_en:
    print("格式错误")
    os._exit(0)
else:
    print("词组文件为：" + target_cizubiao_path)
    
_line2 = linecache.getline(target_word_path, 3)
contain_ = bool(re.search('\t[a-z]+$', _line2))
if contain_:
    print("单字编码文件为：" + target_word_path)
else:
    print("格式错误")
    os._exit(0)


new_cizubiao_path = target_cizubiao_path
new_cizubiao_result_path = './Wubi_ci.txt'


def read_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        temp_list = f.readlines()                   # type: list
    return temp_list


def time_consuming(func, *args, **kwargs):
    """ 耗时统计 """
    start_time = time.time()                                # 开始时间统计
    func(*args, **kwargs)
    end_time = time.time()                                  # 结束时间统计

    print(f'start：{start_time}  end: {end_time}  耗时：{end_time-start_time}')           # 耗时


def draw_word_from_trans():
    """ 从词组-字根 对应表 中提取 词组 """
    words_set = set(read_txt(target_cizubiao_path))
    print(f'词库量：{len(words_set)}')
    with open(new_cizubiao_path, 'w', encoding='utf-8') as f:
        for word in map(lambda word: word.split(' ')[0], words_set):
            f.write(word + '\n')


# 生成字典映射表
word_set = set(read_txt(target_word_path))
word_dict = {}
for word in word_set:
    word_code = word.split('	')
    if word_code and len(word_code) > 1:
        word_dict[word_code[0]] = word_code[1]
error_words = []


def _generate_word(words):
    """
    eg:
        五笔      -> ggte
        中国人    -> klww
        四季如春  -> ltvd
    """

    if '\n' in words:
        words = words[:-1]

    words_len = len(words)
    is_error = False
    code_list = []
    if words_len <= 1:
        is_error = True
        error_words.append(words)
    elif words_len == 2:   #这里定义词长
        for index in range(words_len):
            if words[index] in word_dict:
                code_list.append(word_dict[words[index]][:2]) #这里定义码长
                continue
            else:
                is_error = True
                error_words.append(words)
                break

    elif words_len == 3:
        for index in range(words_len):
            if words[index] in word_dict:
                if index == words_len-1:        # 最后一条
                    code_list.append(word_dict[words[index]][:2])
                else:
                    code_list.append(word_dict[words[index]][0])
                continue
            else:
                is_error = True
                error_words.append(words)
                break

    elif words_len == 4:
        for index in range(words_len):
            if words[index] in word_dict:
                code_list.append(word_dict[words[index]][0])
                continue
            else:
                is_error = True
                error_words.append(words)
                break
    else:
        for index in range(words_len):
            if words[index] in word_dict:
                if index == words_len - 1 or index in [0, 1, 2]:  # 最后一条
                    code_list.append(word_dict[words[index]][0])
                continue
            else:
                is_error = True
                error_words.append(words)
                break

    if is_error:
        return

    return f'{words}	{"".join(code_list)}'


already_print = []


def print_percentage(total, current):
    """ 百分比输出 """
    temp = current/total
    for index in range(10):
        temp_index = (index+1)/10
        if not temp_index in already_print:
            if temp > temp_index:
                print(f'进度：{index*10}%')
                already_print.append(temp_index)


def generate_word_result():
    """ 根据 单字对应表/词库 生成 词库对应表 """

    words_set = set(read_txt(new_cizubiao_path))
    words_len = len(words_set)
    print(f'词库量：{words_len}')

    with open(new_cizubiao_result_path, 'w', encoding='utf-8') as f:
        for word in map(_generate_word, words_set):
            if not word:
                continue
            f.write(word + '\n')


def main():
    #time_consuming(draw_word_from_trans)
    time_consuming(generate_word_result)


if __name__ == '__main__':
    main()
