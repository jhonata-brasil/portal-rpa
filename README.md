# Portal RPA - Sistema de Orçamentos

Sistema web para gestão de orçamentos de serviços de RPA (Robotic Process Automation) e automação.

## Características

- ✅ Autenticação com Google OAuth
- ✅ Cadastro e gestão de usuários
- ✅ Sistema de orçamentos
- ✅ Envio automático de emails
- ✅ Interface moderna e responsiva
- ✅ Banco de dados SQLite

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone ou baixe este repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente (opcional, para produção):
```bash
# Windows PowerShell
$env:SECRET_KEY="sua-chave-secreta-aqui"
$env:MAIL_PASSWORD="sua-senha-de-app-gmail"

# Linux/Mac
export SECRET_KEY="sua-chave-secreta-aqui"
export MAIL_PASSWORD="sua-senha-de-app-gmail"
```

## Configuração do Email

Para enviar emails através do Gmail:

1. Ative a verificação em duas etapas na sua conta Google
2. Gere uma "Senha de App":
   - Acesse: https://myaccount.google.com/apppasswords
   - Gere uma senha de app para "Email"
   - Use essa senha na variável `MAIL_PASSWORD`

## Configuração do Google OAuth (Produção)

Para usar autenticação real com Google:

1. Acesse: https://console.cloud.google.com/
2. Crie um novo projeto
3. Ative a API "Google Sign-In"
4. Configure as credenciais OAuth 2.0
5. Adicione o Client ID no arquivo `templates/login.html` (substitua `YOUR_GOOGLE_CLIENT_ID`)

## Executando o Sistema

```bash
python app.py
```

O sistema estará disponível em: `http://localhost:5000`

## Acessando Publicamente

Para tornar o sistema acessível publicamente:

### Opção 1: Usando ngrok (Rápido para testes)
```bash
# Instale o ngrok
# Execute o Flask
python app.py

# Em outro terminal
ngrok http 5000
```

### Opção 2: Deploy em Servidor Cloud

#### Render.com
1. Conecte seu repositório GitHub
2. Configure as variáveis de ambiente
3. Deploy automático

#### Heroku
```bash
heroku create seu-app-rpa
heroku config:set SECRET_KEY=sua-chave-secreta
heroku config:set MAIL_PASSWORD=sua-senha-app
git push heroku main
```

#### PythonAnywhere
1. Faça upload dos arquivos
2. Configure o WSGI file
3. Configure as variáveis de ambiente

## Estrutura do Projeto

```
site_SicoobPortal/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── rpa_portal.db         # Banco de dados SQLite (criado automaticamente)
├── templates/             # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── orcamento.html
│   ├── servicos.html
│   └── contato.html
└── README.md
```

## Funcionalidades

- **Página Inicial**: Apresentação dos serviços
- **Login/Registro**: Autenticação com Google
- **Dashboard**: Visualização de orçamentos do usuário
- **Criar Orçamento**: Formulário para solicitar orçamentos
- **Serviços**: Lista detalhada dos serviços oferecidos
- **Contato**: Informações de contato

## Banco de Dados

O sistema utiliza SQLite com duas tabelas principais:

- **User**: Armazena informações dos usuários
- **Orcamento**: Armazena as solicitações de orçamento

## Segurança

⚠️ **Importante para Produção:**

1. Altere o `SECRET_KEY` para uma chave segura
2. Configure corretamente o Google OAuth
3. Use HTTPS em produção
4. Configure adequadamente as permissões do banco de dados
5. Implemente rate limiting para evitar spam

## Suporte

Para dúvidas ou problemas, entre em contato:
- Email: jhonatanunes2012@gmail.com

## Licença

Este projeto é de uso privado.

