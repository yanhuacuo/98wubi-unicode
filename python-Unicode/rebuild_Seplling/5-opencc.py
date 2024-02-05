# 使用该脚本，可自动生成 opencc 注解表
import os
current_path = os.getcwd()
os.makedirs(current_path + "/opencc注解表/",exist_ok = True)
text3 = current_path + "/opencc注解表/spelling3.txt"
text2 = current_path + "/opencc注解表/spelling2.txt"
text1 = current_path + "/opencc注解表/spelling1.txt"
sp3 = open(text3, 'w', encoding='utf-8')
sp2 = open(text2, 'w', encoding='utf-8')
sp1 = open(text1, 'w', encoding='utf-8')

scText = current_path + "/处理结果/4-[最终合并]重复项整合结果.txt"

def writeToText3(aList):
    aString = aList[-1]
    aList.pop()
    strSpelling3 = aList[0]
    strSpelling2 = aList[0]
    strSpelling1 = aList[0]
    aNum = len(aList)
    if aNum == 2:
        strSpelling2 = aList[0]+"☯" + aList[1]
        strSpelling3 = aList[0]+"☯" + aList[1]
    if aNum == 3:
        pinyin = aList[2].replace("_","※")
        strSpelling3 = aList[0]+"☯" + aList[1] + "☯" + pinyin
        strSpelling2 = aList[0]+"☯" + aList[1]
    sp3.writelines(aString +'\t' + "〔" + strSpelling3 + "〕" + '\n')
    sp2.writelines(aString +'\t' + "〔" + strSpelling2 + "〕" + '\n')
    sp1.writelines(aString +'\t' + "〔" + strSpelling1 + "〕" + '\n')

with open(scText, 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0] #字符串-汉字
        spelling = alst[1].rstrip() #字符串-[※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※,※GBK※]
        spelling = spelling[1:-1] # 除一个字符串的首字符和尾字符-※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※,※GBK※
        spellingList = spelling.split(',') # [※󰂥※󰄋※󰄋※󰄋※,※ettt※,※shān_xiǎn※]
        spellingList[-1]=val
        writeToText3(spellingList) #执行三重注解表写入
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
sp1.close()
sp2.close()
sp3.close()
print("opencc注解表制作成功！")
