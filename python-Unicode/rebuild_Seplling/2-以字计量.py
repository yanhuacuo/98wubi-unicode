import os
import shutil
import pandas as pd

current_path = os.getcwd()

achieveText = current_path + "/处理结果/2-连值.txt"
duplicateText = current_path + "/处理结果/1-已去重.txt"

os.makedirs(current_path + "/处理结果/",exist_ok = True)

data = pd.read_csv(duplicateText, sep='\t',header=None,encoding='utf-16')
data.columns = ["val", "code"]

# 按 val 分组，并连接相应的 code  
result = data.groupby('val')['code'].apply(' '.join).reset_index()  

result.to_csv(achieveText, sep='\t',index=False,header=False ,na_rep = 'nan',encoding='utf-16')
print("以字计量已完成，结果保存到【处理结果/2-连值.txt】内！")