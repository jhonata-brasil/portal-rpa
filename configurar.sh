#!/bin/bash
# Script de configuração para Linux/Mac

echo "========================================"
echo "  CONFIGURADOR DO PORTAL RPA"
echo "========================================"
echo ""
echo "Este script ajuda a configurar o Google OAuth Client ID"
echo ""

read -p "Cole seu Google Client ID aqui (ou pressione Enter para pular): " CLIENT_ID

if [ -z "$CLIENT_ID" ]; then
    echo ""
    echo "Google Client ID não configurado."
    echo "O sistema funcionará em modo de teste."
    echo "Para configurar depois, veja o arquivo GUIA_GOOGLE_OAUTH.md"
else
    echo ""
    echo "Configurando Google Client ID..."
    export GOOGLE_CLIENT_ID="$CLIENT_ID"
    echo "export GOOGLE_CLIENT_ID=\"$CLIENT_ID\"" >> ~/.bashrc
    echo ""
    echo "Google Client ID configurado com sucesso!"
    echo ""
    echo "IMPORTANTE: Execute 'source ~/.bashrc' ou feche e reabra o terminal."
fi

echo ""
echo "========================================"
echo "  PRÓXIMOS PASSOS"
echo "========================================"
echo ""
echo "1. Ative o ambiente virtual:"
echo "   source venv/bin/activate"
echo ""
echo "2. Execute o servidor:"
echo "   python app.py"
echo ""
echo "3. Acesse: http://localhost:5000"
echo ""

