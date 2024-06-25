@echo off
cd /d "%~dp0"
echo 当前目录是： %cd%
python mk-fcitx5-auto.py
echo "处理完毕"
::pause