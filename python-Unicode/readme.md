# python 环境

## pandas 模块

装好 python 后，PowerShell 下输入：

`pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas`

## 介绍

使用方法为：PowerShell 中输入：python + 空格 + 脚本名称

`python test.py`

下列脚本的排序，亦是使用顺序

- test.py

这个脚本，从十六进制生成汉字的角度，对当前【纠正后的拆分总表.txt】进行【查漏】。
如果有漏编的汉字，都会因遍历而被筛查出来。

- spelling.py

该脚本对【纠正后的拆分总表.txt】的拆分内容进行筛查，把混入拆分中的汉字挑出来。

- unicode.py

这个脚本将【纠正后的拆分总表.txt】一下拆分为【CJK】文件夹下20个细目表。
这个主要用来校对、审核拆分文件。

- mk-rime-table.py

这个脚本可以生成【超集多义】、【超集单义】、【超集RIME表】、【wubi98_U.dict.yaml】

- opencc.py

这个脚本可以生成opencc拆分注解文件，单注解、双注解、三注解。虽然现在小狼毫和鼠须管都用不上了，但是同文手机输入法可能还需要它。

- point.py

可以根据汉字的点位，进行 unicode 归类。可以生成新的注解文件，但是目前用不到。作为储备吧。
