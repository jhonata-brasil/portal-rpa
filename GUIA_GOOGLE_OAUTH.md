# Guia Passo a Passo - Configurar Google OAuth

## 🎯 Objetivo
Configurar o login com Google para que os usuários possam fazer cadastro usando suas contas Google.

## 📋 Passo a Passo Detalhado

### Passo 1: Criar Projeto no Google Cloud Console

1. Acesse: https://console.cloud.google.com/
2. Faça login com sua conta Google (jhonatanunes2012@gmail.com)
3. Clique em "Selecionar um projeto" no topo
4. Clique em "Novo Projeto"
5. Nome do projeto: `Portal RPA` (ou outro nome de sua escolha)
6. Clique em "Criar"

### Passo 2: Configurar Tela de Consentimento OAuth

1. No menu lateral, vá em "APIs e Serviços" → "Tela de consentimento OAuth"
2. Escolha "Externo" e clique em "Criar"
3. Preencha os campos:
   - **Nome do aplicativo**: Portal RPA
   - **Email de suporte ao usuário**: jhonatanunes2012@gmail.com
   - **Email do desenvolvedor**: jhonatanunes2012@gmail.com
4. Clique em "Salvar e Continuar"
5. Na próxima tela, clique em "Adicionar ou Remover Escopos"
6. Selecione os escopos necessários:
   - `.../auth/userinfo.email`
   - `.../auth/userinfo.profile`
   - `openid`
7. Clique em "Atualizar" e depois "Salvar e Continuar"
8. Na tela "Usuários de teste", você pode adicionar emails de teste (opcional)
9. Clique em "Salvar e Continuar"
10. Revise e clique em "Voltar ao painel"

### Passo 3: Criar Credenciais OAuth 2.0

1. No menu lateral, vá em "APIs e Serviços" → "Credenciais"
2. Clique em "Criar Credenciais" → "ID do cliente OAuth"
3. Selecione "Aplicativo da Web"
4. Configure:
   - **Nome**: Portal RPA Web Client
   - **Origens JavaScript autorizadas**: 
     ```
     http://localhost:5000
     http://127.0.0.1:5000
     ```
     (Para produção, adicione também seu domínio público)
   - **URIs de redirecionamento autorizados**: 
     ```
     http://localhost:5000/login/google
     http://127.0.0.1:5000/login/google
     ```
     (Para produção, adicione também seu domínio público)
5. Clique em "Criar"
6. **IMPORTANTE**: Copie o **ID do cliente** que aparece na tela (algo como: `123456789-abc123def456.apps.googleusercontent.com`)

### Passo 4: Configurar no Sistema

#### Opção A: Windows PowerShell

Abra o PowerShell na pasta do projeto e execute:

```powershell
# Ative o ambiente virtual primeiro
.\venv\Scripts\Activate.ps1

# Configure o Client ID
$env:GOOGLE_CLIENT_ID="SEU_CLIENT_ID_AQUI.apps.googleusercontent.com"

# Execute o servidor
python app.py
```

#### Opção B: Criar arquivo .env (Recomendado)

1. Crie um arquivo chamado `.env` na raiz do projeto
2. Adicione o conteúdo:
```
GOOGLE_CLIENT_ID=SEU_CLIENT_ID_AQUI.apps.googleusercontent.com
SECRET_KEY=sua-chave-secreta-aqui
MAIL_PASSWORD=sua-senha-de-app-gmail
```

3. Instale python-dotenv:
```bash
pip install python-dotenv
```

4. Modifique o `app.py` para carregar o .env automaticamente

### Passo 5: Testar o Login

1. Execute o servidor: `python app.py`
2. Acesse: http://localhost:5000
3. Clique em "Entrar com Google"
4. Deve aparecer a tela de login do Google
5. Faça login com uma conta Google
6. Permita o acesso ao aplicativo
7. Você deve ser redirecionado para o dashboard

## ⚠️ Problemas Comuns

### "Erro 400: redirect_uri_mismatch"
- Verifique se o URI de redirecionamento está exatamente como configurado no Google Cloud Console
- Certifique-se de que está usando `http://localhost:5000/login/google` (não `http://localhost:5000/`)

### "Token inválido"
- Verifique se o Client ID está correto
- Certifique-se de que está usando a mesma conta Google que criou o projeto

### "Google OAuth não configurado"
- Verifique se a variável de ambiente `GOOGLE_CLIENT_ID` está configurada
- No PowerShell: `$env:GOOGLE_CLIENT_ID` deve mostrar seu Client ID

## 🔒 Segurança

- **NUNCA** compartilhe seu Client ID publicamente
- **NUNCA** faça commit do arquivo `.env` no Git
- Em produção, use HTTPS
- Configure URLs específicas no Google Cloud Console para produção

## 📞 Suporte

Se tiver problemas, verifique:
1. Console do navegador (F12) para erros JavaScript
2. Terminal onde o Flask está rodando para erros do servidor
3. Google Cloud Console → APIs e Serviços → Credenciais para verificar configurações

