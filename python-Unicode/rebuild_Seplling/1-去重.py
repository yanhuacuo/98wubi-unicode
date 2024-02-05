import os
import shutil
import pandas as pd

current_path = os.getcwd()

achieveText = current_path + "/处理结果/1-已去重.txt"
duplicateText = current_path + "/Wubi98-Unicode15.1.txt"

os.makedirs(current_path + "/处理结果/",exist_ok = True)

data = pd.read_csv(duplicateText, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]
data = data.drop_duplicates()

data.to_csv(achieveText, sep='\t',index=False,header=False ,na_rep = 'nan',encoding='utf-16')
print("去重复条目已完成，结果保存到【处理结果/1-已去重.txt】内！")