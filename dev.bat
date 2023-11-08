@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM -- Verifica si sphinx-autobuild está instalado --
python -m pip freeze > temp.txt
findstr /m "sphinx-autobuild" temp.txt
IF !ERRORLEVEL! NEQ 0 (
    echo sphinx-autobuild no está instalado. Instalándolo...
    python -m pip install sphinx-autobuild
)

REM -- Ejecuta sphinx-autobuild si ya está instalado --
echo Ejecutando sphinx-autobuild...
sphinx-autobuild source/ build/html

REM -- Limpia el archivo temporal --
del temp.txt

ENDLOCAL
