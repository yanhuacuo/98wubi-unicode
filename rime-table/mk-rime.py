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
print("排序成功，已覆盖写入！")
del sorted_DicList

import pandas as pd
data = pd.read_csv(table_path, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]
data = data.drop_duplicates()
data.to_csv(table_path, sep='\t',index=False,header=False ,na_rep = 'nan', encoding='utf-16')
print("对含重汇总表，做【去重】处理，并写入到【超集-单义表】")

data["freq"] = range(len(data)*10,len(data)*9,-1) #range(初值, 终值, 步长)
dataGB = pd.read_csv(current_path + "/lib/GB18030-27533.txt", sep='\t',header=None,encoding='utf-16')
dataGB.columns = ["val", "full_code"]

#print("data 数据表共有", data.shape[1], "列")
#print("dataGB 数据表共有", dataGB.shape[1], "列")

resultData = pd.merge(data, dataGB, how='left', on='val')

del data
del dataGB

cNum = 0
allNum = resultData.shape[0]

while cNum < allNum:
    if type(resultData.iloc[cNum, 3])!=type('a'): 
        resultData.iloc[cNum, 3] = resultData.iloc[cNum, 1]
    cNum += 1
resultData.to_csv(current_path + "/生成结果/超集-rime格式码表.txt", sep='\t',index=False, header=False ,na_rep = 'nan', encoding='utf-16')
print("【超集-rime格式码表.txt】，已写入！")

resultData.drop(['freq', 'full_code'], axis=1, inplace=True)

print("准备制作【多义码表】文件，")

del resultData

resultData = pd.read_csv(table_path, sep='\t',header=None, keep_default_na=False,encoding='utf-16')
resultData.columns = ["val", "code"]
# 合并相同编码的词条  
resultData = resultData.groupby('code').agg({'val': ' '.join}).reset_index()
# 按编码排序  
resultData = resultData.sort_values('code')  
# 导出
resultData.to_csv(current_path + "/生成结果/超集-多义表.txt", sep='\t',index=False, header=False , encoding='utf-16')

del resultData

content_f1=[]
with open(current_path + "/生成结果/超集-多义表.txt", 'r' ,encoding='utf-16') as f0:
    content_f1 = f0.readlines()
with open(current_path + "/生成结果/超集-多义表.txt", 'w' ,encoding='utf-16') as f0:
    for line in content_f1:
        line = line.replace('\t'," ")
        f0.write(line)
print("制作完成【多义码表】文件！")

# 定义要合并的三个txt文件名
file1 = current_path +'/lib/rime表头.txt'
file2 = current_path + "/生成结果/超集-rime格式码表.txt"
file3 = current_path +'/lib/rime表尾.txt'
content_f1=[]
content_f2=[]
content_f3=[]
# 打开第一个txt文件进行读取
with open(file1, 'r' ,encoding='utf-8') as f1:
    content_f1 = f1.readlines()
# 打开第二个txt文件进行读取
with open(file2, 'r' ,encoding='utf-16') as f2:
    content_f2 = f2.readlines()
# 打开第三个txt文件进行读取
with open(file3, 'r' ,encoding='utf-8') as f3:
    content_f3 = f3.readlines()
# 创建一个新的txt文件，并将所有内容写入其中
merged_content = content_f1 + ['\n'] + content_f2 + ['\n'] +  content_f3

output_filename = current_path + "/生成结果/wubi98_U.dict.yaml"
with open(output_filename, 'w' ,encoding='utf-8') as output_file:
    for line in merged_content:
        if line == '\n':
            line = line.strip('\n')
        output_file.write(line)
print("已成功制作【wubi98_ci.dict.yaml】")

