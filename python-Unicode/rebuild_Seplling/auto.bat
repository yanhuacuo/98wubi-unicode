@echo off
cd /d "%~dp0"
echo 当前目录是： %cd%
python 1-去重.py
python 2-以字计量.py
python 3-取双列.py
python 4-重复项整合.py
python 5-opencc.py
echo "处理完毕"
pause