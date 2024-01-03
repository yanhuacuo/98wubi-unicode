# pip安装模块
# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas tqdm
import os
import re
import time
import linecache
import tkinter as tk
from tkinter import filedialog

current_path = os.getcwd()
os.makedirs(current_path + "/生成结果/",exist_ok = True)
print("已新建【生成结果】文件夹！")

root = tk.Tk()
root.withdraw()
table_path = filedialog.askopenfilename(title='请选择【单行单义】的码表，格式【汉字+Tab+编码】', filetypes=[('Text', '*.txt'), ('All Files', '*')])                          # 单字-编码或拆分 对应表
if table_path == '':
    print("您没有选择任何文件，已停止")
    os._exit(0)
else:
    print(table_path)


# 重新排序

myDicList = []

with open(table_path, 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        code = alst[1] # 编码
        aDic = { "汉字":val, "编码": code }
        myDicList.append(aDic)
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符

print("创建词典列表，以便做汇总排序！")

sorted_DicList = sorted(myDicList, key=lambda x: x["编码"], reverse=False)
del myDicList

sp23 = open(table_path, 'w', encoding='utf-16')

for phrase in sorted_DicList:
    strDic = phrase['汉字'] +'\t' + phrase['编码'] + '\n'
    sp23.writelines(strDic)
sp23.close()
print("已【排序】成功，并覆盖写入！")
del sorted_DicList

import pandas as pd
data = pd.read_csv(table_path, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]
data = data.drop_duplicates()
data.to_csv(table_path, sep='\t',index=False,header=False ,na_rep = 'nan', encoding='utf-16')
print("已【去重】处理，并覆盖写入！")

from tqdm import tqdm  
import time

print("准备制作【fcitx5原生码表】文件，")

mkText = current_path + "/生成结果/fcitx5_" + os.path.basename(table_path)
fcitx5_file = open(mkText, 'w' ,encoding='utf-8')

def fcitx5_progress(content_f1):
    i = 0
    allNum = len(content_f1)
    while i < allNum:
        for i in tqdm(range(allNum)):
            line = content_f1[i]
            line = line.rstrip()
            line = line.lstrip()
            alst = line.split('\t')
            fcitx5_file.write(alst[1]+ ' '+ alst[0] + '\n')
            i += 1

content_f1=[]
with open(table_path, 'r' ,encoding='utf-16') as f1:
    content_f1 = f1.readlines()

if __name__ == "__main__":  
    fcitx5_progress(content_f1)
    content_f1=[]
    fcitx5_file.close()
    print("【fcitx5原生码表】已生成！")