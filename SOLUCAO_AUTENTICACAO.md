# 🔐 Solução: Erro de Autenticação GitHub

## ⚠️ Problema Detectado

O Git está tentando usar credenciais de outro usuário (`jhonata-4028`), mas o repositório pertence a `jhonata-brasil`.

## ✅ Solução: Criar Personal Access Token

O GitHub não aceita mais senha normal. Você precisa criar um **Personal Access Token**.

### Passo 1: Criar Token

1. Acesse: https://github.com/settings/tokens
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. Preencha:
   - **Note**: `Portal RPA - Deploy`
   - **Expiration**: Escolha uma data (ex: 90 dias)
   - **Scopes**: Marque ✅ **repo** (acesso completo aos repositórios)
4. Clique em **"Generate token"**
5. **COPIE O TOKEN** (você só verá uma vez!)
   - Exemplo: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Passo 2: Limpar Credenciais Antigas

Execute no PowerShell:

```powershell
# Limpar credenciais antigas do Windows
git credential-manager-core erase
```

Ou use o Gerenciador de Credenciais do Windows:
1. Pressione `Windows + R`
2. Digite: `control /name Microsoft.CredentialManager`
3. Vá em "Credenciais do Windows"
4. Procure por "git:https://github.com"
5. Remova/edite as credenciais antigas

### Passo 3: Tentar Push Novamente

Depois de limpar as credenciais, execute:

```powershell
git push -u origin main
```

Quando pedir:
- **Username**: `jhonata-brasil`
- **Password**: Cole o **Personal Access Token** que você copiou

---

## 🔄 Alternativa: Usar SSH (Mais Seguro)

Se preferir usar SSH (mais seguro e não precisa digitar token toda vez):

### 1. Gerar Chave SSH

```powershell
# Verificar se já tem chave SSH
ls ~/.ssh

# Se não tiver, gerar uma nova
ssh-keygen -t ed25519 -C "seu@email.com"
# Pressione Enter para aceitar local padrão
# Opcional: Digite uma senha para proteger a chave
```

### 2. Copiar Chave Pública

```powershell
# Copiar chave pública
cat ~/.ssh/id_ed25519.pub
```

### 3. Adicionar no GitHub

1. Acesse: https://github.com/settings/keys
2. Clique em **"New SSH key"**
3. Cole a chave pública
4. Dê um título: `Portal RPA - PC`
5. Clique em **"Add SSH key"**

### 4. Alterar URL do Repositório para SSH

```powershell
# Remover origin atual
git remote remove origin

# Adicionar com SSH
git remote add origin git@github.com:jhonata-brasil/portal-rpa.git

# Fazer push
git push -u origin main
```

---

## ⚡ Solução Rápida (Recomendada)

1. Crie o Personal Access Token (veja Passo 1 acima)
2. Execute este comando (substitua TOKEN pelo seu token):

```powershell
git remote set-url origin https://TOKEN@github.com/jhonata-brasil/portal-rpa.git
git push -u origin main
```

**OU** use o formato mais seguro:

```powershell
git push -u origin main
# Quando pedir usuário: jhonata-brasil
# Quando pedir senha: cole o token
```

---

## ✅ Depois do Push

Quando o push funcionar, você verá:
- ✅ Todos os arquivos no GitHub
- ✅ Repositório público: https://github.com/jhonata-brasil/portal-rpa

**Depois podemos fazer deploy no Render.com!** 🚀

