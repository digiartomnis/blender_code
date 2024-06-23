@echo off
setlocal enabledelayedexpansion

:: 配置部分
set ENV_NAME=blender_env
set ENV_DIR=%cd%\env

:: 检查环境是否存在
if not exist "%ENV_DIR%" (
    echo Environment does not exist. Please run setup_env.bat first.
    exit /b 1
)

:: 激活环境
call conda activate "%ENV_DIR%"
if !errorlevel! neq 0 (
    echo Failed to activate conda environment
    exit /b !errorlevel!
)

:: 设置环境变量
set CONDA_ENV_PROMPT=(%ENV_NAME%)

:: 更新PATH
set PATH=%ENV_DIR%;%ENV_DIR%\Scripts;%PATH%

echo Environment activated successfully.
echo You are now using Python:
python --version

:: 启动新的命令提示符，保持环境激活
cmd /k

:: Vscode重新加载窗口（Ctrl+Shift+P，然后输入 "Reload Window"）。可以让fake-bpy-module起作用