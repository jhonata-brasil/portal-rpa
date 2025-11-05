# 🚀 Guia Rápido - Criar Repositório no GitHub

## ✅ Passo 1: Criar Repositório no GitHub

1. **Acesse**: https://github.com
2. Faça login na sua conta
3. Clique no botão **"+"** no canto superior direito
4. Selecione **"New repository"**
5. Preencha:
   - **Repository name**: `portal-rpa` (ou outro nome de sua escolha)
   - **Description**: "Sistema de orçamentos para serviços de RPA e automação"
   - **Visibility**: ✅ **Public** (público)
   - **NÃO marque** "Add a README file" (já temos)
   - **NÃO marque** "Add .gitignore" (já temos)
   - **NÃO marque** "Choose a license"
6. Clique em **"Create repository"**

## ✅ Passo 2: Conectar com o Repositório

Depois de criar o repositório, você verá uma página com instruções.

**Copie a URL do seu repositório**. Será algo como:
```
https://github.com/SEU_USUARIO/portal-rpa.git
```

## ✅ Passo 3: Executar Comandos

Volte aqui e me informe:
1. A URL do seu repositório GitHub
2. Ou execute você mesmo os comandos abaixo (substituindo SEU_USUARIO e SEU_REPOSITORIO):

```powershell
# Adicionar repositório remoto (SUBSTITUA pela sua URL)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Verificar se foi adicionado
git remote -v

# Fazer push para o GitHub
git push -u origin main
```

## ⚠️ Se pedir autenticação:

O GitHub não aceita mais senha normal. Você precisa criar um **Personal Access Token**:

1. Acesse: https://github.com/settings/tokens
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. Dê um nome: `Portal RPA`
4. Marque a opção: ✅ **repo** (acesso completo aos repositórios)
5. Clique em **"Generate token"**
6. **COPIE O TOKEN** (você só verá uma vez!)
7. Quando o Git pedir senha, use esse TOKEN (não sua senha normal)

## ✅ Passo 4: Verificar

Acesse seu repositório no GitHub. Você deve ver todos os arquivos!

---

**Agora preciso que você:**
1. Crie o repositório no GitHub
2. Me informe a URL do repositório

Ou execute os comandos acima substituindo SEU_USUARIO e SEU_REPOSITORIO pela URL real do seu repositório.

