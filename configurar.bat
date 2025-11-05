@echo off
echo ========================================
echo   CONFIGURADOR DO PORTAL RPA
echo ========================================
echo.
echo Este script ajuda a configurar o Google OAuth Client ID
echo.

set /p CLIENT_ID="Cole seu Google Client ID aqui (ou pressione Enter para pular): "

if "%CLIENT_ID%"=="" (
    echo.
    echo Google Client ID não configurado.
    echo O sistema funcionará em modo de teste.
    echo Para configurar depois, veja o arquivo GUIA_GOOGLE_OAUTH.md
) else (
    echo.
    echo Configurando Google Client ID...
    setx GOOGLE_CLIENT_ID "%CLIENT_ID%" >nul 2>&1
    set GOOGLE_CLIENT_ID=%CLIENT_ID%
    echo.
    echo Google Client ID configurado com sucesso!
    echo.
    echo IMPORTANTE: Feche e reabra o PowerShell para aplicar as mudanças.
    echo Ou execute: $env:GOOGLE_CLIENT_ID="%CLIENT_ID%"
)

echo.
echo ========================================
echo   PRÓXIMOS PASSOS
echo ========================================
echo.
echo 1. Ative o ambiente virtual:
echo    .\venv\Scripts\Activate.ps1
echo.
echo 2. Execute o servidor:
echo    python app.py
echo.
echo 3. Acesse: http://localhost:5000
echo.
pause

