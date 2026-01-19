@echo off

REM Run this script from the Task Scheduler each week or so.
REM Check "Run whether user is logged on or not" to hide the
REM batch script window and to hide also the opened browser
REM in case it runs in non-headless mode.
REM Attention: do not use the SYSTEM account because Python 
REM            is usually installed for a specific user which 
REM            has user specific libraries installed!

REM An endlocal is implicitly called when this script terminates, 
REM endlocal does not reset the errorlevel variable
setlocal

REM This batch file's directory (has trailing backslash)
set batchdir=%~dp0

REM Remove old log file if existing
set logfile=%~dpn0-log.txt
if exist "%logfile%" del "%logfile%"

REM Load settings from .env file which must follow:
REM 1. Values can be unquoted or double-quoted if having special chars.
REM 2. Only #-comments at start of line.
for /F "usebackq tokens=* eol=#" %%i in ("%batchdir%.env") do set %%i

REM Set default for USE_PYTHON_VER if not defined
if not defined USE_PYTHON_VER set USE_PYTHON_VER=3

REM Call the freedns.py autologin script
REM Attention: use the correct version because the libraries 
REM            are only install for a given Python version!
echo AUTOLOGIN to freedns (at %time% on %date%)>> "%logfile%" 2>&1
py -%USE_PYTHON_VER% "%batchdir%freedns.py" >> "%logfile%" 2>&1
call :CHECKEXITCODE

REM Call more scripts here
REM ...

REM Send log file by email
echo SENDING EMAIL>> "%logfile%" 2>&1
"%batchdir%mailsend-go\mailsend-go.exe" -t %EMAIL_TO% -f %EMAIL_FROM% -fname "Autologin Sites" -port %EMAIL_PORT% -smtp %EMAIL_SMTP% -sub "Autologin Sites ended at %time% on %date%" body -file "%logfile%" auth -user %EMAIL_USER% -pass %EMAIL_PW%
call :CHECKEXITCODE

REM Do end script
goto :eof

:CHECKEXITCODE
if %ERRORLEVEL% neq 0 echo ERROR: previous command failed (code %ERRORLEVEL%)>> "%logfile%" 2>&1
echo ************************************************************************>> "%logfile%" 2>&1
exit /B
