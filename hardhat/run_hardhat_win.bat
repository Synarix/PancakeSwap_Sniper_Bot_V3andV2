@echo off

REM Function to check if nvm is installed
where nvm >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo nvm is not installed. Installing nvm...
    call :install_nvm
) else (
    echo nvm is already installed.
    goto :check_node_version
)

REM Function to install nvm for Windows
:install_nvm
echo Downloading nvm setup...
powershell -Command "Invoke-WebRequest -Uri https://github.com/coreybutler/nvm-windows/releases/download/1.1.9/nvm-setup.zip -OutFile nvm-setup.zip"
powershell -Command "Expand-Archive nvm-setup.zip -DestinationPath ."
powershell -Command "Start-Process .\nvm-setup.exe -Wait -Verb RunAs"
echo nvm installed. Please restart the Command Prompt and re-run this script.
exit /b

REM Function to check the Node.js version
:check_node_version
for /f "tokens=*" %%i in ('node -v 2^>nul') do set "NODE_VERSION=%%i"
if not defined NODE_VERSION (
    echo Node.js is not installed.
    set NODE_VERSION=none
)

if "%NODE_VERSION:~0,4%"=="v18." (
    echo Node.js version 18 is already installed.
) else (
    echo Node.js version 18 is not installed.
    call :install_node
)

REM Function to install Node.js version 18 using nvm
:install_node
echo Installing Node.js version 18...
REM Install Node.js version 18 using nvm
nvm install 18
nvm use 18
nvm alias default 18
echo Node.js version 18 installed.
goto :check_hardhat

REM Function to install Hardhat
:install_hardhat
echo Installing Hardhat...
npm install -g hardhat
echo Hardhat installed.
goto :start_hardhat

REM Check if Hardhat is installed
:check_hardhat
where hardhat >nul 2>nul
if %ERRORLEVEL% neq 0 (
    call :install_hardhat
) else (
    echo Hardhat is already installed.
    goto :start_hardhat
)

REM Start the Hardhat node as administrator
:start_hardhat
echo Starting Hardhat node...
powershell -Command "npx hardhat node"
exit /b