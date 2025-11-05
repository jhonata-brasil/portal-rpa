# 🚀 Guia de Deploy no GitHub - Portal RPA

Este guia vai te ajudar a publicar seu projeto no GitHub e depois fazer deploy em uma plataforma gratuita.

## 📋 Pré-requisitos

1. Conta no GitHub (crie em: https://github.com)
2. Git instalado no seu computador
3. Projeto funcionando localmente

---

## 🔧 Passo 1: Preparar o Projeto

### 1.1 Verificar arquivos sensíveis

Certifique-se de que o `.gitignore` está configurado corretamente para não commitar:
- Arquivos `.env` (senhas)
- Pasta `venv/` (ambiente virtual)
- Banco de dados `*.db`
- Arquivos temporários

### 1.2 Criar arquivo README.md (se não existir)

O README já existe com informações básicas.

---

## 📦 Passo 2: Inicializar Git Localmente

Abra o PowerShell na pasta do projeto e execute:

```powershell
# Verificar se Git está instalado
git --version

# Se não estiver instalado, baixe em: https://git-scm.com/downloads
```

### 2.1 Inicializar repositório

```powershell
# Navegue até a pasta do projeto (se ainda não estiver)
cd C:\site_SicoobPortal

# Inicialize o Git
git init

# Configure seu nome e email (se ainda não configurou)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## 🗂️ Passo 3: Adicionar Arquivos

### 3.1 Verificar status

```powershell
git status
```

Você verá quais arquivos serão adicionados.

### 3.2 Adicionar arquivos

```powershell
# Adicionar todos os arquivos (exceto os ignorados pelo .gitignore)
git add .

# Verificar o que será commitado
git status
```

### 3.3 Fazer primeiro commit

```powershell
git commit -m "Primeiro commit: Portal RPA - Sistema de orçamentos"
```

---

## 🌐 Passo 4: Criar Repositório no GitHub

### 4.1 Criar novo repositório

1. Acesse: https://github.com
2. Faça login na sua conta
3. Clique no botão "+" no canto superior direito
4. Selecione "New repository"
5. Preencha:
   - **Repository name**: `portal-rpa` (ou outro nome)
   - **Description**: "Sistema de orçamentos para serviços de RPA"
   - **Visibility**: Público (Public) ✅
   - **NÃO marque** "Initialize with README" (já temos arquivos)
6. Clique em "Create repository"

### 4.2 Copiar URL do repositório

Você verá uma página com instruções. Copie a URL do seu repositório.
Exemplo: `https://github.com/seuusuario/portal-rpa.git`

---

## 🔗 Passo 5: Conectar com GitHub

```powershell
# Adicionar repositório remoto (substitua pela SUA URL)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Verificar se foi adicionado
git remote -v
```

### 5.1 Renomear branch para main (se necessário)

```powershell
# Verificar branch atual
git branch

# Se estiver em 'master', renomeie para 'main'
git branch -M main
```

### 5.2 Fazer push

```powershell
# Fazer push para o GitHub
git push -u origin main
```

**Na primeira vez, o GitHub pedirá suas credenciais:**
- Username: seu usuário do GitHub
- Password: use um **Personal Access Token** (não sua senha normal)

---

## 🔑 Passo 6: Criar Personal Access Token (GitHub)

Se o Git pedir senha, você precisa criar um token:

1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome: "Portal RPA"
4. Selecione escopos:
   - ✅ `repo` (acesso completo aos repositórios)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (você só verá uma vez!)
7. Use esse token como senha quando o Git pedir

---

## ✅ Passo 7: Verificar no GitHub

1. Acesse seu repositório no GitHub
2. Você deve ver todos os arquivos do projeto
3. O README.md deve aparecer na página inicial

---

## 🚀 Passo 8: Deploy Automático (Render.com)

Agora que está no GitHub, você pode fazer deploy automático:

### 8.1 Criar conta no Render

1. Acesse: https://render.com
2. Clique em "Get Started for Free"
3. Escolha "Sign up with GitHub"
4. Autorize o acesso

### 8.2 Criar Web Service

1. No dashboard do Render, clique em "New +"
2. Selecione "Web Service"
3. Clique em "Connect GitHub"
4. Escolha seu repositório `portal-rpa`
5. Configure:
   - **Name**: `portal-rpa`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Root Directory**: (deixe vazio)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### 8.3 Configurar Variáveis de Ambiente

Na seção "Environment Variables", adicione:

```
SECRET_KEY=sua-chave-secreta-muito-longa-aqui
MAIL_PASSWORD=sua-senha-de-app-gmail
MAIL_USERNAME=jhonatanunes2012@gmail.com
```

### 8.4 Deploy

1. Clique em "Create Web Service"
2. Aguarde o deploy (pode levar alguns minutos)
3. Seu site estará em: `https://portal-rpa.onrender.com`

---

## 📝 Checklist Final

Antes de fazer push:

- [ ] Arquivo `.env` NÃO está no Git (verificado pelo .gitignore)
- [ ] Senha de app do Gmail NÃO está no código
- [ ] `rpa_portal.db` NÃO está no Git
- [ ] Pasta `venv/` NÃO está no Git
- [ ] README.md está atualizado
- [ ] Todos os arquivos importantes estão commitados

---

## 🔒 Segurança

**IMPORTANTE - NUNCA FAÇA:**
- ❌ Commit de arquivos `.env` com senhas
- ❌ Commit de senhas no código
- ❌ Commit do banco de dados com dados reais
- ❌ Commit da pasta `venv/`

**SEMPRE FAÇA:**
- ✅ Use variáveis de ambiente
- ✅ Configure `.gitignore` corretamente
- ✅ Use senhas de app (não senhas normais)
- ✅ Revise o que está sendo commitado (`git status`)

---

## 🆘 Solução de Problemas

### Erro: "remote origin already exists"

```powershell
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

### Erro: "failed to push"

- Verifique se criou o Personal Access Token
- Use o token como senha, não sua senha normal

### Arquivos sensíveis foram commitados

```powershell
# Remover do histórico (CUIDADO!)
git rm --cached .env
git commit -m "Remove arquivo sensível"
git push
```

---

## 📚 Próximos Passos

Depois de fazer deploy:

1. ✅ Configure domínio customizado (opcional)
2. ✅ Configure email para produção
3. ✅ Teste todos os recursos
4. ✅ Compartilhe o link!

---

## 🎉 Pronto!

Seu projeto agora está:
- ✅ No GitHub (público)
- ✅ Pronto para deploy automático
- ✅ Versionado e seguro

**URL do seu repositório**: `https://github.com/SEU_USUARIO/portal-rpa`

**URL do site (após deploy)**: `https://portal-rpa.onrender.com`

