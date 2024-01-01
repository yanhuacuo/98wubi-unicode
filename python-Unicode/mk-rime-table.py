# 使用该脚本，可自动生成 rime 码表

# gb单字表.txt 复制为 超集-单义表.txt
# 超集-单义表.txt 中添加【拆分总表】内读到的【全字集数据】，"a" 模式，追加写入
# 只读模式，创建【含重表】的词典列表，以对其内容进行排序 ， 只读为 "r" 模式，
# 排序后覆盖写出一次，引用新模块去重后再写出一次
# 以 vlookup 的等效方式，生成 rime 表

import os
current_path = os.getcwd()
os.makedirs(current_path + "/RIME格式码表/",exist_ok = True)

import shutil
# 定义源文件路径和目标文件路径
src_file = current_path + "/gb单字表.txt"
dst_file = current_path + "/RIME格式码表/超集-单义表.txt"

try:
    # 判断目标文件是否存在，若存在则先删除再进行复制操作
    if os.path.exists(dst_file):
        os.remove(dst_file)    
    # 调用shutil库的copy函数进行复制操作
    shutil.copy2(src_file, dst_file)
    # print("成功将文件从{}复制到{}".format(src_file, dst_file))
    print("准备制作超集表！")
except Exception as e:
    print("gb单字表.txt 缺失，请检查：", str(e))

text2 = dst_file
sp2 = open(text2, 'a', encoding='utf-16')

def writeToText2(aList):
    aString = aList[-1]
    aList.pop()
    strSpelling2 =""
    code_point = ord(aString)
    hex_a = 0xe000 # PUA E000~F8FF
    hex_b = 0xf8ff # PUA E000~F8FF
    if code_point>= hex_a and code_point <= hex_b:
        return
    else:
        strSpelling2= aList[1].replace("※","")
    sp2.writelines(aString +'\t' + strSpelling2 + '\n')

with open('纠正后的拆分总表.txt', 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        spelling = alst[1].rstrip() #字符串-[※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※,※GBK※]
        spelling = spelling[1:-1] # 除一个字符串的首字符和尾字符-※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※,※GBK※
        spellingList = spelling.split(',') # [※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※]
        spellingList[-1]=val
        writeToText2(spellingList) # 生成新的【超集-单义表.txt】
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
sp2.close()

print("【gb单字 + 全集汉字】，含重汇总表【超集-单义表】，制作成功！")

text22 = dst_file

myDicList = []

with open(text22, 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        code = alst[1] # 编码
        aDic = { "汉字":val, "编码": code }
        myDicList.append(aDic)
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符

print("创建【含重汇总表】的词典列表，以便做汇总排序！")

sorted_DicList = sorted(myDicList, key=lambda x: x["编码"], reverse=False)
del myDicList

text23 = dst_file
sp23 = open(text23, 'w', encoding='utf-16')

for phrase in sorted_DicList:
    strDic = phrase['汉字'] +'\t' + phrase['编码'] + '\n'
    sp23.writelines(strDic)
sp23.close()
print("含重汇总表，排序成功，已写入到【超集-单义表】！")
del sorted_DicList

import pandas as pd
data = pd.read_csv(dst_file, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]
data = data.drop_duplicates()
data.to_csv(dst_file, sep='\t',index=False,header=False ,na_rep = 'nan',encoding='utf-16')
print("对含重汇总表，做【去重】处理，并写入到【超集-单义表】")

data["freq"] = range(len(data)*10,len(data)*9,-1) #range(初值, 终值, 步长)
dataGB = pd.read_csv(current_path + "/GB18030-27533.txt", sep='\t',header=None,encoding='utf-16')
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
resultData.to_csv(current_path + "/RIME格式码表/超集-rime格式码表.txt", sep='\t',index=False, header=False ,na_rep = 'nan',encoding='utf-16')
print("【超集-rime格式码表.txt】，已写入！")

resultData.drop(['freq', 'full_code'], axis=1, inplace=True)

print("准备制作【多义码表】文件，")

del resultData

resultData = pd.read_csv(dst_file, sep='\t',header=None, keep_default_na=False,encoding='utf-16')
resultData.columns = ["val", "code"]

# 合并相同编码的词条  
resultData = resultData.groupby('code').agg({'val': ' '.join}).reset_index()
# 按编码排序  
resultData = resultData.sort_values('code')  
# 导出
resultData.to_csv(current_path + "/RIME格式码表/超集-多义表.txt", sep='\t',index=False, header=False ,na_rep = 'nan',encoding='utf-16')

del resultData

content_f1=[]
with open(current_path + "/RIME格式码表/超集-多义表.txt", 'r' ,encoding='utf-16') as f0:
    content_f1 = f0.readlines()
with open(current_path + "/RIME格式码表/超集-多义表.txt", 'w' ,encoding='utf-16') as f0:
    for line in content_f1:
        line = line.replace('\t'," ")
        f0.write(line)
print("制作完成【多义码表】文件！")

# 定义要合并的三个txt文件名
file1 = 'rime表头.txt'
file2 = current_path + "/RIME格式码表/超集-rime格式码表.txt"
file3 = 'rime表尾.txt'
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

output_filename = current_path + "/RIME格式码表/wubi98_U.dict.yaml"
with open(output_filename, 'w' ,encoding='utf-8') as output_file:
    for line in merged_content:
        if line == '\n':
            line = line.strip('\n')
        output_file.write(line)
print("已成功制作【wubi98_U.dict.yaml】")

