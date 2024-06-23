@echo off
set ENV_NAME=llm_code
set ENV_DIR=%cd%\env

if not exist "%ENV_DIR%" (
    echo Creating new conda environment...
    call conda create --prefix %ENV_DIR% python=3.11 -y
)

call conda activate %ENV_DIR%
if %errorlevel% neq 0 (
    echo Failed to activate conda environment
    exit /b %errorlevel%
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements
    exit /b %errorlevel%
)

echo Environment setup complete
python --version
conda list