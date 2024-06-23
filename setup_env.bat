@echo off
setlocal enabledelayedexpansion

:: 配置部分
set ENV_NAME=blender_env
set PYTHON_VERSION=3.11
set ENV_DIR=%cd%\env

:: 检查是否已存在环境
if exist "%ENV_DIR%" (
    echo Environment already exists. Updating...
    call conda activate "%ENV_DIR%"
) else (
    echo Creating new conda environment...
    call conda create --prefix "%ENV_DIR%" python=%PYTHON_VERSION% -y
    if !errorlevel! neq 0 (
        echo Failed to create conda environment
        exit /b !errorlevel!
    )
    call conda activate "%ENV_DIR%"
)

:: 安装或更新 conda 依赖
if exist environment.txt (
    echo Installing/Updating conda dependencies...
    for /F "tokens=*" %%A in (environment.txt) do (
        conda install --yes %%A
        if !errorlevel! neq 0 (
            echo Failed to install %%A
            exit /b !errorlevel!
        )
    )
) else (
    echo environment.txt not found. Skipping conda package installation.
)

:: 安装或更新 pip 依赖
if exist requirements.txt (
    echo Installing/Updating pip dependencies...
    pip install -r requirements.txt
    if !errorlevel! neq 0 (
        echo Failed to install pip requirements
        exit /b !errorlevel!
    )
) else (
    echo requirements.txt not found. Skipping pip package installation.
)

:: 设置环境变量
setx CONDA_ENV_PROMPT "(%ENV_NAME%)"

echo Environment setup complete
echo To activate this environment, run start_env.bat

endlocal