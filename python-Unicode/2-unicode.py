# 使用该脚本，可自动分离【纠正后的拆分总表.txt】或其它单行单义表中的PUA字符
import os
current_path = os.getcwd()


os.makedirs(current_path + "/PUA/",exist_ok = True)
os.makedirs(current_path + "/CJK/",exist_ok = True)

pua_txt = current_path + "/PUA/PUA.txt"


cjk_base_20902 = current_path + "/CJK/cjk_base_20902.txt"
cjk_base_ext_90 = current_path + "/CJK/cjk_base_ext_90.txt"
cjk_A_6582 = current_path + "/CJK/cjk_A_6582.txt"
cjk_A_ext_10 = current_path + "/CJK/cjk_A_ext_10.txt"
cjk_B_42711 = current_path + "/CJK/cjk_B_42711.txt"
cjk_B_ext_9 = current_path + "/CJK/cjk_B_ext_9.txt"
cjk_C_4149 = current_path + "/CJK/cjk_C_4149.txt"
cjk_C_ext_5 = current_path + "/CJK/cjk_C_ext_5.txt"
cjk_D_222 = current_path + "/CJK/cjk_D_222.txt"
cjk_E_5762 = current_path + "/CJK/cjk_E_5762.txt"
cjk_F_7473 = current_path + "/CJK/cjk_F_7473.txt"
cjk_G_4939 = current_path + "/CJK/cjk_G_4939.txt"
cjk_H_4192 = current_path + "/CJK/cjk_H_4192.txt"
cjk_I_622 = current_path + "/CJK/cjk_I_622.txt"


cjk_KangXiBuShou_214 = current_path + "/CJK/cjk_KangXiBuShou_214.txt"
cjk_BuShou_ext_115 = current_path + "/CJK/cjk_BuShou_ext_115.txt"
cjk_JianRongHanZhi_472 = current_path + "/CJK/cjk_JianRongHanZhi_472.txt"
cjk_JianRong_ext_542 = current_path + "/CJK/cjk_JianRong_ext_542.txt"
cjk_HanZhiBiHua_36 = current_path + "/CJK/cjk_HanZhiBiHua_36.txt"

others = current_path + "/CJK/others.txt"

aPUA = open(pua_txt, 'w', encoding='utf-16')
cjk_base_20902_file = open(cjk_base_20902, 'w', encoding='utf-16')
cjk_base_ext_90_file = open(cjk_base_ext_90, 'w', encoding='utf-16')
cjk_A_6582_file = open(cjk_A_6582, 'w', encoding='utf-16')
cjk_A_ext_10_file = open(cjk_A_ext_10, 'w', encoding='utf-16')
cjk_B_42711_file = open(cjk_B_42711, 'w', encoding='utf-16')
cjk_B_ext_9_file = open(cjk_B_ext_9, 'w', encoding='utf-16')
cjk_C_4149_file = open(cjk_C_4149, 'w', encoding='utf-16')
cjk_C_ext_5_file = open(cjk_C_ext_5, 'w', encoding='utf-16')
cjk_D_222_file = open(cjk_D_222, 'w', encoding='utf-16')
cjk_E_5762_file = open(cjk_E_5762, 'w', encoding='utf-16')
cjk_F_7473_file = open(cjk_F_7473, 'w', encoding='utf-16')
cjk_G_4939_file = open(cjk_G_4939, 'w', encoding='utf-16')
cjk_H_4192_file = open(cjk_H_4192, 'w', encoding='utf-16')
cjk_I_622_file = open(cjk_I_622, 'w', encoding='utf-16')


cjk_KangXiBuShou_214_file = open(cjk_KangXiBuShou_214, 'w', encoding='utf-16')
cjk_BuShou_ext_115_file = open(cjk_BuShou_ext_115, 'w', encoding='utf-16')
cjk_JianRongHanZhi_472_file = open(cjk_JianRongHanZhi_472, 'w', encoding='utf-16')
cjk_JianRong_ext_542_file = open(cjk_JianRong_ext_542, 'w', encoding='utf-16')
cjk_HanZhiBiHua_36_file = open(cjk_HanZhiBiHua_36, 'w', encoding='utf-16')


others_file = open(others, 'w', encoding='utf-16')

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

with open('纠正后的拆分总表.txt', 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0]
        code_point = ord(val)
        hex_pua_B = 0xe000 # PUA E000~F8FF
        hex_pua_E = 0xf8ff # PUA E000~F8FF
        if code_point>= hex_pua_B and code_point <= hex_pua_E:
            aPUA.writelines(aline +'\n')
        elif code_point>= cjk_base_20902_B and code_point <= cjk_base_20902_E:
            cjk_base_20902_file.writelines(aline  +'\n')
        elif code_point>= cjk_base_ext_90_B and code_point <= cjk_base_ext_90_E:
            cjk_base_ext_90_file.writelines(aline  +'\n')
        elif code_point>= cjk_A_6582_B and code_point <= cjk_A_6582_E:
            cjk_A_6582_file.writelines(aline  +'\n')
        elif code_point>= cjk_A_ext_10_B and code_point <= cjk_A_ext_10_E:
            cjk_A_ext_10_file.writelines(aline  +'\n')
        elif code_point>= cjk_B_42711_B and code_point <= cjk_B_42711_E:
            cjk_B_42711_file.writelines(aline  +'\n')
        elif code_point>= cjk_B_ext_9_B and code_point <= cjk_B_ext_9_E:
            cjk_B_ext_9_file.writelines(aline  +'\n')
        elif code_point>= cjk_C_4149_B and code_point <= cjk_C_4149_E:
            cjk_C_4149_file.writelines(aline  +'\n')
        elif code_point>= cjk_C_ext_5_B and code_point <= cjk_C_ext_5_E:
            cjk_C_ext_5_file.writelines(aline  +'\n')
        elif code_point>= cjk_D_222_B and code_point <= cjk_D_222_E:
            cjk_D_222_file.writelines(aline  +'\n')
        elif code_point>= cjk_E_5762_B and code_point <= cjk_E_5762_E:
            cjk_E_5762_file.writelines(aline  +'\n')
        elif code_point>= cjk_F_7473_B and code_point <= cjk_F_7473_E:
            cjk_F_7473_file.writelines(aline  +'\n')
        elif code_point>= cjk_G_4939_B and code_point <= cjk_G_4939_E:
            cjk_G_4939_file.writelines(aline  +'\n')
        elif code_point>= cjk_H_4192_B and code_point <= cjk_H_4192_E:
            cjk_H_4192_file.writelines(aline  +'\n')
        elif code_point>= cjk_I_622_B and code_point <= cjk_I_622_E:
            cjk_I_622_file.writelines(aline  +'\n')
        elif code_point>= cjk_KangXiBuShou_214_B and code_point <= cjk_KangXiBuShou_214_E:
            cjk_KangXiBuShou_214_file.writelines(aline  +'\n')
        elif code_point>= cjk_BuShou_ext_115_B and code_point <= cjk_BuShou_ext_115_E:
            cjk_BuShou_ext_115_file.writelines(aline  +'\n')
        elif code_point>= cjk_JianRongHanZhi_472_B and code_point <= cjk_JianRongHanZhi_472_E:
            cjk_JianRongHanZhi_472_file.writelines(aline  +'\n')
        elif code_point>= cjk_JianRong_ext_542_B and code_point <= cjk_JianRong_ext_542_E:
            cjk_JianRong_ext_542_file.writelines(aline  +'\n')
        elif code_point>= cjk_HanZhiBiHua_36_B and code_point <= cjk_HanZhiBiHua_36_E:
            cjk_HanZhiBiHua_36_file.writelines(aline  +'\n')    
        else:
            others_file.writelines(aline  +'\n')
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
        
aPUA.close()
cjk_base_20902_file.close()
cjk_base_ext_90_file.close()
cjk_A_6582_file.close()
cjk_A_ext_10_file.close()
cjk_B_42711_file.close()
cjk_B_ext_9_file.close()
cjk_C_4149_file.close()
cjk_C_ext_5_file.close()
cjk_D_222_file.close()
cjk_E_5762_file.close()
cjk_F_7473_file.close()
cjk_G_4939_file.close()
cjk_H_4192_file.close()
cjk_I_622_file.close()

cjk_KangXiBuShou_214_file.close()
cjk_BuShou_ext_115_file.close()
cjk_JianRongHanZhi_472_file.close()
cjk_JianRong_ext_542_file.close()
cjk_HanZhiBiHua_36_file.close()

others_file.close()

print("分离成功！")
