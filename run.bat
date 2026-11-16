@echo off
chcp 65001 >nul
title AMD AI Developer Program RegisterHub
echo ========================================================
echo   AMD AI Developer Program RegisterHub
echo   AMD 官方 AI 开发者计划全自动入职与凭据获取工具
echo ========================================================
echo.
echo [1] 默认启动运行 (生成 1 个账号凭据)
echo [2] 批量运行 (生成 3 个账号凭据)
echo [3] 无头后台运行 (--headless)
echo.
set /p opt="请选择运行模式 (默认 1): "
if "%opt%"=="" set opt=1
if "%opt%"=="1" python main.py -n 1
if "%opt%"=="2" python main.py -n 3
if "%opt%"=="3" python main.py --headless -n 1
echo.
pause
