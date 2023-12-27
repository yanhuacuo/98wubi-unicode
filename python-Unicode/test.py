# 使用该脚本，可自动测试unicode15.1标准下，当前码表所缺失的字符
import os
current_path = os.getcwd()
os.makedirs(current_path + "/缺字目录/",exist_ok = True)

lose_txt = current_path + "/缺字目录/详细缺目.txt"
lose_list = current_path + "/缺字目录/缺少的字符列表.txt"

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

cjk_files_tuple=(
cjk_base_20902,
cjk_base_ext_90,
cjk_A_6582,
cjk_A_ext_10,
cjk_B_42711,
cjk_B_ext_9,
cjk_C_4149,
cjk_C_ext_5,
cjk_D_222,
cjk_E_5762,
cjk_F_7473,
cjk_G_4939,
cjk_H_4192,
cjk_I_622,
cjk_KangXiBuShou_214,
cjk_BuShou_ext_115,
cjk_JianRongHanZhi_472,
cjk_JianRong_ext_542,
cjk_HanZhiBiHua_36
)

cjk_code_tuple_B=(
cjk_base_20902_B,
cjk_base_ext_90_B,
cjk_A_6582_B,
cjk_A_ext_10_B,
cjk_B_42711_B,
cjk_B_ext_9_B,
cjk_C_4149_B,
cjk_C_ext_5_B,
cjk_D_222_B,
cjk_E_5762_B,
cjk_F_7473_B,
cjk_G_4939_B,
cjk_H_4192_B,
cjk_I_622_B,
cjk_KangXiBuShou_214_B,
cjk_BuShou_ext_115_B,
cjk_JianRongHanZhi_472_B,
cjk_JianRong_ext_542_B,
cjk_HanZhiBiHua_36_B
)

cjk_code_tuple_E=(
cjk_base_20902_E,
cjk_base_ext_90_E,
cjk_A_6582_E,
cjk_A_ext_10_E,
cjk_B_42711_E,
cjk_B_ext_9_E,
cjk_C_4149_E,
cjk_C_ext_5_E,
cjk_D_222_E,
cjk_E_5762_E,
cjk_F_7473_E,
cjk_G_4939_E,
cjk_H_4192_E,
cjk_I_622_E,
cjk_KangXiBuShou_214_E,
cjk_BuShou_ext_115_E,
cjk_JianRongHanZhi_472_E,
cjk_JianRong_ext_542_E,
cjk_HanZhiBiHua_36_E
)

lose_txt_file = open(lose_txt, 'w', encoding='utf-16')
lose_list_file = open(lose_list, 'w', encoding='utf-16')

i = 0
while i < 19: 
    text_file = cjk_files_tuple[i]
    code_B = cjk_code_tuple_B[i]
    code_E = cjk_code_tuple_E[i]
    cjk_set = {0x2e9a,0xfa6e,0xfa6f} #预置 unicode15.1 未启用的点位
    with open(text_file, 'r', encoding='utf-16') as afile:
        aline = afile.readline()  # 读取第一行
        while aline:
            aline=aline.rstrip()
            alst = aline.split('\t')
            val = alst[0]
            code_point = ord(val)
            cjk_set.add(code_point)
            aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
    num = code_B
    while num < code_E:
        if num in cjk_set:
            pass
        else:
            lose_txt_file.writelines(text_file + " → loses: " + str(hex(num))  + "【" + chr(num) +"】" +'\n' )
            lose_list_file.writelines("【" + chr(num) +"】" +'\n' )
        num +=1
    i += 1
lose_txt_file.close()
lose_list_file.close()

def is_blank_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip() == '':
                return True
    return False

if is_blank_file(lose_txt):
    print("该码表已完整收录 Unicode15.1 标准规范内的全部汉字！")
else:
    print("检测完毕，结果在【缺字目录】文件夹下！")
