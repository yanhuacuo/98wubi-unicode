import os
import shutil
import pandas as pd

current_path = os.getcwd()

achieveText = current_path + "/处理结果/4-temp.txt"
duplicateText = current_path + "/处理结果/3-原表歧义多拆细目.txt"

os.makedirs(current_path + "/处理结果/",exist_ok = True)

data = pd.read_csv(duplicateText, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]

# 按 val 分组，并连接相应的 code  
result = data.groupby('val')['code'].apply(' '.join).reset_index()  

result.to_csv(achieveText, sep='\t',index=False,header=False ,na_rep = 'nan',encoding='utf-16')

print("已对单义格式的【歧义表】作以字计量分组，结果保存到【4-temp.txt】内！")

############待做

duplicateText = current_path + "/处理结果/4-temp.txt"
achieveText = current_path + "/处理结果/4-[变化部分]重复项整合结果.txt"

sp1 = open(achieveText, 'w', encoding='utf-16')

# 间隔符定义，用于歧义拆分的间隔之中
ne = "·" 

with open(duplicateText, 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        spellStrItemList = []
        spellStrItem = ""
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        spelling = alst[1].strip() #字符串-[※󰄋※󰁪※󰄦※󰂘※,※tuwc※,※GBK※] [※󰄋※󰁪※󰄒※󰂘※,※tuuc※,※GBK※]
        spellingList = spelling.split(' ') # 以空格切分，得到 [三重注解项一、三重注解项二、三重注解项三]
        for item in spellingList:
            spellStrItem = item.split(',')[0].replace("[※","")
            spellStrItem = spellStrItem.replace("※","")
            spellStrItemList.append(spellStrItem)
        # 使用空格作为分隔符拼接列表元素成字符串
        strNewSpelling = ne.join(spellStrItemList)
        strNewSpelling = val + '\t' + "[※" + strNewSpelling + "※,※GBK※]"
        sp1.writelines(strNewSpelling+'\n')
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
sp1.close()


 
def copy_file(src, dest):
    shutil.copy2(src, dest)

source_file = current_path + "/处理结果/3-[二分法]无歧义部分.txt"
destination_file = current_path + "/处理结果/4-[最终合并]重复项整合结果.txt"
copy_file(source_file, destination_file)

def merge(file1,file2):
    f1 = open(file1,'a+',encoding='utf-16')
    with open(file2,'r',encoding="utf-16") as f2:
        # f1.write('\n')
        for i in f2:
            f1.write(i)

merge(destination_file,achieveText)

source_file = current_path + "/wb_spelling.txt"
wb_spelling_file = current_path + "/处理结果/4-[最终合并]wb_spelling.txt"

copy_file(source_file, wb_spelling_file)

merge(wb_spelling_file, destination_file)

import codecs
source_file = current_path + "/处理结果/4-[最终合并]wb_spelling.txt"
wb_spelling_file = current_path + "/处理结果/wb_spelling.dict.yaml"

# 读取UTF-16编码的文件
with codecs.open(source_file, 'r', 'utf-16') as f:
    content = f.read()
 
# 将内容写入UTF-8编码的文件
with codecs.open(wb_spelling_file, 'w', 'utf-8') as f:
    f.write(content)

print("重复项整合已完成！")