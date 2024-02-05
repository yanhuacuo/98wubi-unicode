import os
import shutil
import pandas as pd
import codecs

current_path = os.getcwd()

achieveText = current_path + "/处理结果/3-单映射无重表.txt"
duplicateText = current_path + "/处理结果/2-连值.txt"

text1 = current_path + "/处理结果/3-原表歧义多拆细目.txt"

text2 = current_path + "/处理结果/3-[二分法]无歧义部分.txt"
text3 = current_path + "/处理结果/3-[二分法]有歧义多拆部分.txt"

sp1 = open(achieveText, 'w', encoding='utf-16')
sp2 = open(text1, 'w', encoding='utf-16')

sp3 = open(text2, 'w', encoding='utf-16') #3-[二分法]无重部分.txt
sp4 = open(text3, 'w', encoding='utf-16') #3-[二分法]有歧义多拆部分.txt

with open(duplicateText, 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        spelling = alst[1].strip() #字符串-[※󰄋※󰁪※󰄦※󰂘※,※tuwc※,※GBK※] [※󰄋※󰁪※󰄒※󰂘※,※tuuc※,※GBK※]
        spellingList = spelling.split(' ') # 以空格切分
        i = len(spellingList)
        if i == 1:
            sp1.writelines(aline  + '\n')
            sp3.writelines(aline  + '\n')
        else:
            sp1.writelines(val + '\t' + spellingList[0] + '\n')
            for item in spellingList:
                sp2.writelines(val + '\t' + item + '\n') # 遇到歧议，分行写入
                sp4.writelines(val + '\t' + item + '\n') # 遇到歧义，分行写入 
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
sp1.close()
sp2.close()
sp3.close()
sp4.close()

print("取双列已完成！")