# ⚠️ PROBLEMA: Não consigo usar a conta do Google para cadastro

## 🔍 Diagnóstico

O login com Google não está funcionando porque o **Google Client ID não está configurado**. 

Quando você acessa a página de login, o sistema detecta que não há Client ID configurado e entra em **modo de teste**, onde você precisa digitar email e nome manualmente.

## ✅ SOLUÇÃO RÁPIDA (2 opções)

### Opção 1: Usar Modo de Teste (Rápido para testar)

O sistema já tem um modo de teste funcionando:
1. Acesse: http://localhost:5000/login
2. Clique em "Entrar com Google (Modo Teste)"
3. Digite seu email e nome quando solicitado
4. O sistema criará sua conta automaticamente

**Limitação**: Não é o login real do Google, apenas simulação.

### Opção 2: Configurar Google OAuth Real (Recomendado)

Para usar o login real do Google, siga estes passos:

#### Passo 1: Obter Google Client ID

1. Acesse: https://console.cloud.google.com/
2. Crie um projeto ou selecione um existente
3. Vá em "APIs e Serviços" → "Credenciais"
4. Clique em "Criar Credenciais" → "ID do cliente OAuth"
5. Configure:
   - Tipo: **Aplicativo da Web**
   - Nome: Portal RPA
   - **Origens JavaScript autorizadas**: `http://localhost:5000`
   - **URIs de redirecionamento**: `http://localhost:5000/login/google`
6. Copie o Client ID gerado (algo como: `123456789-abc.apps.googleusercontent.com`)

#### Passo 2: Configurar no Sistema

**Método A: Usando PowerShell (Windows)**

```powershell
# Ative o ambiente virtual primeiro
.\venv\Scripts\Activate.ps1

# Configure o Client ID
$env:GOOGLE_CLIENT_ID="SEU_CLIENT_ID_AQUI.apps.googleusercontent.com"

# Execute o servidor
python app.py
```

**Método B: Criar arquivo .env (Melhor para produção)**

1. Crie um arquivo chamado `.env` na raiz do projeto
2. Adicione esta linha:
```
GOOGLE_CLIENT_ID=SEU_CLIENT_ID_AQUI.apps.googleusercontent.com
```

3. Execute o servidor normalmente:
```powershell
.\venv\Scripts\Activate.ps1
python app.py
```

O sistema agora carregará automaticamente o `.env`!

#### Passo 3: Testar

1. Acesse: http://localhost:5000/login
2. Agora você verá o botão oficial do Google
3. Clique e faça login com sua conta Google
4. Pronto! Sua conta será criada automaticamente

## 📚 Documentação Completa

Para mais detalhes, consulte:
- **GUIA_GOOGLE_OAUTH.md** - Guia completo passo a passo
- **CONFIG.md** - Configurações gerais do sistema

## 🆘 Ainda com Problemas?

### Erro: "redirect_uri_mismatch"
- Verifique se o URI está exatamente: `http://localhost:5000/login/google`
- Certifique-se de ter adicionado em "URIs de redirecionamento autorizados"

### Erro: "Token inválido"
- Verifique se o Client ID está correto
- Certifique-se de que está usando a mesma conta Google que criou o projeto

### O botão do Google não aparece
- Verifique se a variável `GOOGLE_CLIENT_ID` está configurada
- No PowerShell: `$env:GOOGLE_CLIENT_ID` deve mostrar seu Client ID
- Verifique o console do navegador (F12) para erros JavaScript

## 💡 Dica

Se você só quer testar o sistema rapidamente, use o **Modo de Teste**. Mas para produção ou uso real, configure o Google OAuth seguindo a Opção 2 acima.

