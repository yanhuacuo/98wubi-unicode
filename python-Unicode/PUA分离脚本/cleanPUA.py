# 使用该脚本，可自动分离【超集-rime格式码表.txt】或其它单行单义表中的PUA字符
aPUA = open('PUA.txt', 'w', encoding='utf-16')
aRE = open('Unicode-Standard.txt', 'w', encoding='utf-16')
with open('超集-rime格式码表.txt', 'r', encoding='utf-16') as afile:
    aline = afile.readline()  # 读取第一行
    while aline:
        aline=aline.rstrip()
        alst = aline.split('\t')
        val = alst[0]
        code_point = ord(val)
        hex_a = 0xe000 # PUA E000~F8FF
        hex_b = 0xf8ff # PUA E000~F8FF
        if code_point>= hex_a and code_point <= hex_b:
            aPUA.writelines(aline +'\n')
        else:
            aRE.writelines(aline  +'\n')
        aline = afile.readline()  # 继续读取下一行，直到文件末尾返回空字符
aPUA.close()
aRE.close()
print("over!!")
