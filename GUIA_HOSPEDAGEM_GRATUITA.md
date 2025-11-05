# 🌐 Guia de Hospedagem Gratuita - Portal RPA

Este guia apresenta as melhores opções gratuitas para hospedar seu portal RPA.

## 🎯 Opções Recomendadas (Gratuitas)

### 1. **Render.com** ⭐ RECOMENDADO

**Por que escolher:**
- ✅ Gratuito para projetos pessoais
- ✅ Deploy automático via GitHub
- ✅ SSL/HTTPS gratuito
- ✅ Fácil configuração
- ✅ Banco de dados PostgreSQL gratuito (opcional)

**Passo a Passo:**

1. **Criar conta no Render:**
   - Acesse: https://render.com
   - Crie uma conta gratuita (use GitHub ou email)

2. **Preparar o projeto:**
   ```bash
   # Criar arquivo render.yaml na raiz do projeto
   ```

3. **Configurar no Render:**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     - **Name**: portal-rpa
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

4. **Adicionar variáveis de ambiente:**
   - SECRET_KEY (gere uma chave segura)
   - MAIL_PASSWORD (senha de app do Gmail)
   - MAIL_USERNAME (seu email)

5. **Deploy automático!**
   - Render faz deploy automaticamente quando você faz push no GitHub

**Limitação Gratuita:**
- Aplicação "dorme" após 15 minutos de inatividade
- Leva alguns segundos para acordar quando alguém acessa

---

### 2. **PythonAnywhere** ⭐ FÁCIL

**Por que escolher:**
- ✅ Gratuito para iniciantes
- ✅ Interface web simples
- ✅ Python já instalado
- ✅ Banco de dados MySQL gratuito

**Passo a Passo:**

1. **Criar conta:**
   - Acesse: https://www.pythonanywhere.com
   - Clique em "Sign up for free"

2. **Fazer upload dos arquivos:**
   - Vá em "Files" → "Upload a file"
   - Faça upload de todos os arquivos do projeto

3. **Configurar Web App:**
   - Vá em "Web" → "Add a new web app"
   - Escolha "Flask" → Python 3.10
   - Configure o arquivo WSGI

4. **Configurar banco de dados:**
   - Use SQLite (já funciona) ou MySQL gratuito

**Limitação Gratuita:**
- 1 aplicação web
- Domínio: seuusuario.pythonanywhere.com

---

### 3. **Railway.app** ⭐ MODERNO

**Por que escolher:**
- ✅ Moderno e rápido
- ✅ Deploy via GitHub
- ✅ SSL automático
- ✅ $5 de crédito gratuito por mês

**Passo a Passo:**

1. Acesse: https://railway.app
2. Conecte seu GitHub
3. Clique em "New Project" → "Deploy from GitHub repo"
4. Selecione seu repositório
5. Configure variáveis de ambiente
6. Deploy automático!

---

### 4. **Fly.io** ⭐ PERFORMANCE

**Por que escolher:**
- ✅ Muito rápido
- ✅ Global CDN
- ✅ SSL automático
- ✅ $5 de crédito gratuito

**Passo a Passo:**

1. Instale o CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. No diretório do projeto: `fly launch`
4. Siga as instruções

---

### 5. **Heroku** (Limitado)

**⚠️ ATENÇÃO:** Heroku removeu o plano gratuito, mas ainda pode ser usado para testes.

---

## 📋 Preparação do Projeto para Deploy

### 1. Criar arquivo `Procfile` (para Render, Heroku, etc.)

Crie um arquivo `Procfile` na raiz do projeto:
```
web: gunicorn app:app
```

### 2. Atualizar `requirements.txt`

Adicione gunicorn para produção:
```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Werkzeug==3.0.1
python-dotenv==1.0.0
gunicorn==21.2.0
```

### 3. Modificar `app.py` para produção

Adicione no final do arquivo:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### 4. Criar `runtime.txt` (opcional)

Para especificar versão do Python:
```
python-3.11.0
```

---

## 🚀 Guia Rápido: Render.com (Recomendado)

### Passo 1: Preparar Projeto

```bash
# No terminal, na pasta do projeto
pip install gunicorn
pip freeze > requirements.txt
```

### Passo 2: Criar `Procfile`

Crie arquivo `Procfile` (sem extensão):
```
web: gunicorn app:app
```

### Passo 3: Criar Conta no Render

1. Acesse: https://render.com
2. Clique em "Get Started for Free"
3. Conecte com GitHub

### Passo 4: Criar Web Service

1. Clique em "New +" → "Web Service"
2. Conecte seu repositório GitHub
3. Configure:
   - **Name**: portal-rpa
   - **Region**: Oregon (US West)
   - **Branch**: main
   - **Root Directory**: (deixe vazio)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### Passo 5: Variáveis de Ambiente

Na seção "Environment Variables", adicione:
```
SECRET_KEY=sua-chave-secreta-muito-longa-aqui
MAIL_PASSWORD=sua-senha-de-app-gmail
MAIL_USERNAME=jhonatanunes2012@gmail.com
```

### Passo 6: Deploy

1. Clique em "Create Web Service"
2. Aguarde o deploy (pode levar alguns minutos)
3. Seu site estará em: `https://portal-rpa.onrender.com`

---

## 🔧 Configurações Importantes

### Banco de Dados

Para produção, considere usar PostgreSQL (Render oferece gratuito):
- Vá em "New +" → "PostgreSQL"
- Escolha plano Free
- Atualize `SQLALCHEMY_DATABASE_URI` no código

### Email

Configure corretamente:
- Senha de app do Gmail obrigatória
- Variável `MAIL_PASSWORD` deve estar configurada

### Domínio Customizado

Todas as plataformas permitem adicionar domínio próprio:
- Render: Settings → Custom Domain
- PythonAnywhere: Web → Static files / domains

---

## 📊 Comparação das Plataformas

| Plataforma | Facilidade | Performance | Domínio | Recomendado |
|------------|-----------|-------------|---------|-------------|
| Render.com | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ✅ Sim |
| PythonAnywhere | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ Sim |
| Railway.app | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ Sim |
| Fly.io | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | Para avançados |

---

## 🆘 Solução de Problemas

### Erro: "Application error"

1. Verifique os logs na plataforma
2. Confirme que todas as variáveis de ambiente estão configuradas
3. Verifique se o `Procfile` está correto

### Banco de dados não funciona

- SQLite pode não funcionar em algumas plataformas
- Use PostgreSQL (gratuito no Render)

### Email não envia

- Verifique `MAIL_PASSWORD` (senha de app do Gmail)
- Confirme que o email está correto

---

## ✅ Checklist Antes de Fazer Deploy

- [ ] Arquivo `Procfile` criado
- [ ] `gunicorn` adicionado ao `requirements.txt`
- [ ] Variáveis de ambiente configuradas
- [ ] `SECRET_KEY` definida (não use a padrão!)
- [ ] `MAIL_PASSWORD` configurada
- [ ] Código commitado no GitHub
- [ ] Testado localmente

---

## 🎉 Pronto!

Após seguir os passos, seu portal estará online e acessível publicamente!

**URL será algo como:**
- Render: `https://seu-app.onrender.com`
- PythonAnywhere: `https://seuusuario.pythonanywhere.com`
- Railway: `https://seu-app.railway.app`

**Precisa de ajuda?** Verifique os logs na plataforma escolhida para ver erros específicos.

