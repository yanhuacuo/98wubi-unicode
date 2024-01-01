
## 成品

到 [98五笔资源库](http://98wb.ysepan.com/) 中，下载【小狼毫98五笔】与【字体支持】

## 存档

- [github/98wubi-unicode](https://github.com/yanhuacuo/98wubi-unicode/tree/master)

- [gitee/wubi98-unicode](https://gitee.com/wubi98/wubi98-unicode)

## 先做字体适配

一、安装字体

计有六款矢量字体，黑体风格与宋体风格两种。
超集方案的候选与拆分一律采用宋体风格，而单字与含词选单则采用GB国标字集与黑体风格。

- 98WB-0.ttf
- 98WB-1.otf
- 98WB-2.otf
- 98WB-3.ttf
- 98WB-U.ttf
- 98WB-V.ttf

二、合并注册表

合并注册表后，矢量字体才能被操作系统识别，这一步非常重要。

## 再安装小狼毫

安装完毕后，在【托盘】中，有【小狼毫输入法】的【设置】入口，可以仅勾选您所需的方案：

- 单字（GB国标）
- 含词（GB国标）
- 超集（Unicode15.1全集）

## 明细

完整收录Unicode15.1全部汉字：

| 文件 | 区位 | 
| :-----| :-----|
|cjk_A_6582.txt|中日韩统一表意文字扩展-A|
|cjk_A_ext_10.txt|中日韩统一表意文字扩展-A补充|
|cjk_base_20902.txt|中日韩统一表意文字|
|cjk_base_ext_90.txt|中日韩统一表意文字-补充|
|cjk_B_42711.txt|中日韩统一表意文字扩展-B|
|cjk_B_ext_9.txt|中日韩统一表意文字扩展-B补充|
|cjk_C_4149.txt|中日韩统一表意文字扩展-C|
|cjk_C_ext_5.txt|中日韩统一表意文字扩展-C补充|
|cjk_D_222.txt|中日韩统一表意文字扩展-D|
|cjk_E_5762.txt|中日韩统一表意文字扩展-E|
|cjk_F_7473.txt|中日韩统一表意文字扩展-F|
|cjk_G_4939.txt|中日韩统一表意文字扩展-G|
|cjk_H_4192.txt|中日韩统一表意文字扩展-H|
|cjk_I_622.txt|中日韩统一表意文字扩展-I|
|cjk_BuShou_ext_115.txt|中日汉字部首补充|
|cjk_HanZhiBiHua_36.txt|中日韩笔画|
|cjk_JianRongHanZhi_472.txt|中日韩兼容表意义字|
|cjk_JianRong_ext_542.txt|中日韩兼容表意义字补充|
|cjk_KangXiBuShou_214.txt|康熙字典部首|
|others.txt|日制文字|

剔除PUA点位之后，计 99049 个汉字。

## python脚本工具

#### 码表解离

- [unicode.py](https://gitee.com/wubi98/wubi98-unicode/blob/master/python-Unicode/unicode.py)

该脚本，将目标码表解离成 20 个子码表。


#### 缺失点位检测

- [test.py](https://gitee.com/wubi98/wubi98-unicode/blob/master/python-Unicode/test.py)

按照 [unicode15.1](https://www.unicode.org/Public/15.1.0/charts/CodeCharts.pdf) 的规范点位检测码表中缺失的汉字，并生成检测报告。


## 汉字分类表

[CJK-目录](https://gitee.com/wubi98/wubi98-unicode/tree/master/python-Unicode/CJK)

## 单行单义表转换

rime-table 文件夹下，有 `mk-rime.py` 可以从任意指定的「单行单义表」转为：

- 多义格式码表
- rime格式码表
- wubi98_ci.dict.yaml 范例
- fcitx5原生码表_(编码_词条).txt

