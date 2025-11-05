# Portal RPA - Guia de Início Rápido

## Instalação Rápida

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar Email (Opcional para testes)
Configure a senha de app do Gmail:
- Acesse: https://myaccount.google.com/apppasswords
- Gere uma senha de app
- Defina a variável de ambiente:
```bash
# Windows PowerShell
$env:MAIL_PASSWORD="sua-senha-de-app-aqui"

# Linux/Mac
export MAIL_PASSWORD="sua-senha-de-app-aqui"
```

### 3. Executar o Sistema
```bash
python app.py
```

### 4. Acessar o Portal
Abra seu navegador em: http://localhost:5000

## Funcionalidades Disponíveis

✅ **Página Inicial** - Apresentação dos serviços  
✅ **Login com Google** - Autenticação OAuth (configurar Client ID)  
✅ **Dashboard** - Visualização de orçamentos  
✅ **Criar Orçamento** - Formulário completo de solicitação  
✅ **Serviços** - Detalhamento dos serviços oferecidos  
✅ **Contato** - Informações de contato  

## Configuração para Produção

### 1. Configurar Google OAuth
1. Acesse: https://console.cloud.google.com/
2. Crie um projeto
3. Configure OAuth 2.0
4. Defina variável de ambiente:
```bash
export GOOGLE_CLIENT_ID="seu-client-id.apps.googleusercontent.com"
```

### 2. Configurar SECRET_KEY
```bash
export SECRET_KEY="chave-secreta-muito-segura-aqui"
```

### 3. Deploy Público

#### Opção A: Render.com (Recomendado)
1. Conecte seu repositório GitHub
2. Configure variáveis de ambiente
3. Deploy automático

#### Opção B: Heroku
```bash
heroku create seu-app-rpa
heroku config:set SECRET_KEY=sua-chave
heroku config:set MAIL_PASSWORD=senha-app
heroku config:set GOOGLE_CLIENT_ID=client-id
git push heroku main
```

#### Opção C: ngrok (Testes Rápidos)
```bash
# Terminal 1
python app.py

# Terminal 2
ngrok http 5000
```

## Estrutura de Arquivos

```
site_SicoobPortal/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── templates/          # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── orcamento.html
│   ├── servicos.html
│   └── contato.html
├── rpa_portal.db      # Banco de dados (criado automaticamente)
├── README.md          # Documentação completa
└── CONFIG.md          # Guia de configuração
```

## Fluxo de Uso

1. **Usuário acessa o portal** → Página inicial
2. **Clica em "Entrar com Google"** → Login
3. **Após login** → Dashboard
4. **Cria novo orçamento** → Formulário completo
5. **Envia orçamento** → Email enviado para jhonatanunes2012@gmail.com

## Suporte

Para dúvidas: jhonatanunes2012@gmail.com

