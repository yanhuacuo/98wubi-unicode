# 使用该脚本，可自动对拆分表的注解进行 unicode 范式的识别
import os
current_path = os.getcwd()


os.makedirs(current_path + "/注解修正/",exist_ok = True)

pua_txt = current_path + "/注解修正/Table_已修正.txt"

aPUA = open(pua_txt, 'w', encoding='utf-16')

cjk_base_20902_B = 0x4e00
cjk_base_20902_E = 0x9fa5

cjk_base_ext_90_B = 0x9fa6
cjk_base_ext_90_E = 0x9fff

cjk_A_6582_B = 0x3400
cjk_A_6582_E = 0x4db5

cjk_A_ext_10_B = 0x4db6
cjk_A_ext_10_E = 0x4dbf

cjk_B_42711_B = 0x20000
cjk_B_42711_E = 0x2a6d6

cjk_B_ext_9_B = 0x2a6d7
cjk_B_ext_9_E = 0x2a6df

cjk_C_4149_B = 0x2a700
cjk_C_4149_E = 0x2b734

cjk_C_ext_5_B = 0x2b735
cjk_C_ext_5_E = 0x2b739

cjk_D_222_B = 0x2b740
cjk_D_222_E = 0x2b81d

cjk_E_5762_B = 0x2b820
cjk_E_5762_E = 0x2cea1

cjk_F_7473_B = 0x2ceb0
cjk_F_7473_E = 0x2ebe0

cjk_G_4939_B = 0x30000
cjk_G_4939_E = 0x3134a

cjk_H_4192_B = 0x31350
cjk_H_4192_E = 0x323af

cjk_I_622_B = 0x2ebf0
cjk_I_622_E = 0x2ee5d
 
cjk_KangXiBuShou_214_B = 0x2f00
cjk_KangXiBuShou_214_E = 0x2fd5
cjk_BuShou_ext_115_B = 0x2e80
cjk_BuShou_ext_115_E = 0x2ef3
cjk_JianRongHanZhi_472_B = 0xf900
cjk_JianRongHanZhi_472_E = 0xfad9
cjk_JianRong_ext_542_B = 0x2f800
cjk_JianRong_ext_542_E = 0x2fa1d
cjk_HanZhiBiHua_36_B = 0x31c0
cjk_HanZhiBiHua_36_E = 0x31e3

def writeToText(aString,aList):
    strSpelling =""
    for spellingData in aList:
        strSpelling = strSpelling + ',' + spellingData
    strSpelling = strSpelling.lstrip(",")
    aPUA.writelines(aString +'\t' + strSpelling + '\n')

with open('纠正后的拆分总表.txt', 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0]
        spelling = alst[1]
        spellingList = spelling.split(',')
        code_point = ord(val)
        hex_pua_B = 0xe000 # PUA E000~F8FF
        hex_pua_E = 0xf8ff # PUA E000~F8FF
        if code_point>= hex_pua_B and code_point <= hex_pua_E:
            spellingList[-1]= "※PUA※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_base_20902_B and code_point <= cjk_base_20902_E:
            spellingList[-1]= "※CJK※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_base_ext_90_B and code_point <= cjk_base_ext_90_E:
            spellingList[-1]= "※CJK_ext※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_A_6582_B and code_point <= cjk_A_6582_E:
            spellingList[-1]= "※CJK-A※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_A_ext_10_B and code_point <= cjk_A_ext_10_E:
            spellingList[-1]= "※CJK-A_ext※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_B_42711_B and code_point <= cjk_B_42711_E:
            spellingList[-1]= "※CJK-B※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_B_ext_9_B and code_point <= cjk_B_ext_9_E:
            spellingList[-1]= "※CJK-B_ext※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_C_4149_B and code_point <= cjk_C_4149_E:
            spellingList[-1]= "※CJK-C※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_C_ext_5_B and code_point <= cjk_C_ext_5_E:
            spellingList[-1]= "※CJK-C_ext※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_D_222_B and code_point <= cjk_D_222_E:
            spellingList[-1]= "※CJK-D※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_E_5762_B and code_point <= cjk_E_5762_E:
            spellingList[-1]= "※CJK-E※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_F_7473_B and code_point <= cjk_F_7473_E:
            spellingList[-1]= "※CJK-F※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_G_4939_B and code_point <= cjk_G_4939_E:
            spellingList[-1]= "※CJK-G※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_H_4192_B and code_point <= cjk_H_4192_E:
            spellingList[-1]= "※CJK-H※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_I_622_B and code_point <= cjk_I_622_E:
            spellingList[-1]= "※CJK-I※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_KangXiBuShou_214_B and code_point <= cjk_KangXiBuShou_214_E:
            spellingList[-1]= "※康熙※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_BuShou_ext_115_B and code_point <= cjk_BuShou_ext_115_E:
            spellingList[-1]= "※部首※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_JianRongHanZhi_472_B and code_point <= cjk_JianRongHanZhi_472_E:
            spellingList[-1]= "※兼容※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_JianRong_ext_542_B and code_point <= cjk_JianRong_ext_542_E:
            spellingList[-1]= "※兼扩※]"
            writeToText(val,spellingList)
        elif code_point>= cjk_HanZhiBiHua_36_B and code_point <= cjk_HanZhiBiHua_36_E:
            spellingList[-1]= "※笔画※]"
            writeToText(val,spellingList) 
        else:
            spellingList[-1]= "※其它※]"
            writeToText(val,spellingList) 
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
        
aPUA.close()
print("unicode规范区位，已修正成功！")
