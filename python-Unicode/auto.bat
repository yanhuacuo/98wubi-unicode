@echo off
cd /d "%~dp0"
echo 当前目录是： %cd%
python 1-spelling.py
python 2-unicode.py
python 3-test.py
python 4-mk-rime-table.py
echo "处理完毕"
pause