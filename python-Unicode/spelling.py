# 使用该脚本，可自动测试unicode15.1标准下，当前码表所缺失的字符
import os
current_path = os.getcwd()
os.makedirs(current_path + "/注解修正/",exist_ok = True)
pua_txt = current_path + "/注解修正/Table_已修正.txt"
aPUA = open(pua_txt, 'w', encoding='utf-16')

right_tuple=(
"󰂼",
"󰂝",
"󰅪",
"󰃏",
"󰂚",
"󰄸",
"󰄋",
"󰄎",
"󰂯",
"󰂱",
"󰃚",
"󰃙",
"󰃕",
"󰂶",
"󰄅",
"󰄌",
"󰃽",
"󰃖",
"󰄍",
"󰄼",
"󰄔",
"󰂿",
"󰄤",
"󰂘",
"󰃩",
"󰂰",
"󰄆",
"󰂮",
"󰂆",
"󰂺",
"󰃖",
"󰄳",
"󰃺",
"󰃴",
"󰃨",
"󰃥",
"󰃮",
"󰃢",
"󰄩",
"󰂬",
"󰂳",
"󰃝",
"󰄦",
"󰂴",
"󰃷",
"󰃊",
"󰃅",
"󰄥",
"󰂍",
"󰂟",
"󰂭",
"󰂾",
"󰂜",
"󰄟",
"󰃪",
"󰄠",
"󰂗",
"󰂹",
"󰂨",
"󰁷",
"󰃘",
"󰃍",
"󰄀",
"󰄨",
"󰂣",
"󰂓",
"󰃾",
"󰄒",
"󰂷",
"󰃉",
"󰂫",
"󰄖",
"󰃎",
"󰂸",
"󰂤",
"󰂡",
"󰂧",
"󰃙"
)

bad_tuple=(
"目",
"大",
"",
"口",
"巴",
"方",
"丿",
"彳",
"士",
"十",
"贝",
"田",
"皿",
"一",
"木",
"禾",
"白",
"车",
"⺮",
"丶",
"辛",
"卜",
"人",
"又",
"火",
"干",
"丁",
"土",
"工",
"丨",
"車",
"言",
"儿",
"金",
"灬",
"羽",
"辶",
"心",
"幺",
"毛",
"寸",
"乙",
"八",
"甘",
"勿",
"日",
"小",
"亻",
"子",
"古",
"二",
"止",
"三",
"女",
"米",
"刀",
"皮",
"夫",
"用",
"隹",
"山",
"虫",
"斤",
"几",
"犬",
"也",
"手",
"丷",
"王",
"刂",
"力",
"艹",
"川",
"五",
"戊",
"厂",
"月",
"由"
)

def writeToText(aString,aCode):
    strSpelling =""
    for spellingChar in aCode:
        index = 0
        while index < 78:
            if bad_tuple[index] == spellingChar:
                spellingChar = right_tuple[index]
                break
            index += 1
        strSpelling = strSpelling + spellingChar
    aPUA.writelines(aString +'\t' + strSpelling + '\n')

with open('纠正后的拆分总表.txt', 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0]
        spelling = alst[1]
        writeToText(val,spelling)
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
aPUA.close()
print("注解修正成功！")
