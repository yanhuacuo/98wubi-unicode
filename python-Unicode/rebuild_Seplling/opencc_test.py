# -*- coding: utf-8 -*-

# Opencc 语法检测脚本
# 
# 作者： Shitlime
# 2023年7月26日
# 
# log:
#    fix: 去除文件拖入命令行中带入的单引号
#    fix: 去除文件拖入命令行中带入的空格

def read_file(path:str):
    with open(path, 'r', encoding='utf-16') as f:
        return f.read().split('\n')


def ckeck(lines:str):
    count = {}
    for index, line in enumerate(lines):
        line_number = index + 1
        l = line.split('\t')
        # 行内语法检测
        if len(l) != 2:
            print(f"-> {line_number} |{line}")
            print("    [错误]请检查此行是否按照 `[内容1]{制表符}[内容2]` 的格式编写\n")
            continue
        if l[0] == '':
            print(f"-> {line_number} |{line}")
            print("    [错误]请检查此行中的键是否为空\n")
            continue
        if l[1] == '':
            print(f"-> {line_number} |{line}")
            print("    [警告]请检查此行中的值是否为空\n")
            continue
            
        
        # 统计key是否重复
        if count.get(l[0]):
            count[l[0]] += 1
            print(f"-> {line_number} |{line}")
            print(f"    [错误]请检查此行中的键 `{l[0]}` 是否已经存在其他行中\n")
        else:
            count[l[0]] = 1
    


if __name__ == '__main__':
    print("提示：有错误将按照下面的格式输出⬇")
    print("```")
    print("-> [行号] |[该行的内容]")
    print("    [提示信息]")
    print("\n```")

    file = input("请输入（拖入）要检查的opencc文件：\n").rstrip()
    file = file[1:-1] if file[0] in ('"', "'") and file[-1] == file[0] else file
    lines = read_file(file)
    print("文件读取完成，开始检查...")
    ckeck(lines)
    print("检查完毕。")