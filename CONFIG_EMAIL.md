# 📧 Configuração de Email - Portal RPA

Este guia explica como configurar o envio de emails no portal.

## 🔧 Configuração do Gmail (Recomendado)

### Passo 1: Ativar Verificação em Duas Etapas

1. Acesse: https://myaccount.google.com/
2. Vá em "Segurança"
3. Ative "Verificação em duas etapas"
4. Siga as instruções para configurar

### Passo 2: Gerar Senha de App

1. Acesse: https://myaccount.google.com/apppasswords
2. Se não aparecer, ative a verificação em duas etapas primeiro
3. Selecione:
   - **App**: Email
   - **Dispositivo**: Outro (nome personalizado)
   - Digite: Portal RPA
4. Clique em "Gerar"
5. **Copie a senha gerada** (16 caracteres, sem espaços)
   - Exemplo: `abcd efgh ijkl mnop` → Use: `abcdefghijklmnop`

### Passo 3: Configurar no Sistema

#### Opção A: Variável de Ambiente (Recomendado)

**Windows PowerShell:**
```powershell
$env:MAIL_PASSWORD="sua-senha-de-app-aqui"
```

**Windows CMD:**
```cmd
set MAIL_PASSWORD=sua-senha-de-app-aqui
```

**Linux/Mac:**
```bash
export MAIL_PASSWORD="sua-senha-de-app-aqui"
```

#### Opção B: Arquivo .env

1. Crie um arquivo `.env` na raiz do projeto
2. Adicione:
```
MAIL_USERNAME=jhonatanunes2012@gmail.com
MAIL_PASSWORD=sua-senha-de-app-aqui
```

### Passo 4: Testar

1. Execute o servidor: `python app.py`
2. Crie um orçamento
3. Verifique o terminal - deve aparecer: `✅ Email enviado com sucesso para: ...`

---

## 📮 Outros Provedores de Email

### Outlook/Hotmail

```python
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USERNAME=seu@outlook.com
MAIL_PASSWORD=sua-senha
```

### Yahoo

```python
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USERNAME=seu@yahoo.com
MAIL_PASSWORD=sua-senha-de-app-yahoo
```

### Outros Provedores

Para outros provedores, configure manualmente no código ou use variáveis de ambiente:
- `MAIL_SERVER` - Servidor SMTP
- `MAIL_PORT` - Porta (geralmente 587 para TLS)
- `MAIL_USERNAME` - Seu email
- `MAIL_PASSWORD` - Sua senha ou senha de app

---

## 🔍 Solução de Problemas

### Erro: "ERRO DE AUTENTICAÇÃO"

**Causa:** Senha de app incorreta ou não configurada

**Solução:**
1. Verifique se a senha de app está correta
2. Certifique-se de copiar SEM espaços
3. Regenere uma nova senha de app se necessário

### Erro: "MAIL_PASSWORD não configurado"

**Causa:** Variável de ambiente não configurada

**Solução:**
1. Configure a variável de ambiente (veja Passo 3 acima)
2. Ou crie arquivo `.env` na raiz do projeto
3. Reinicie o servidor após configurar

### Erro: "Email rejeitado"

**Causa:** Email do destinatário inválido

**Solução:**
1. Verifique se o email está correto
2. Certifique-se de que o email existe

### Emails não chegam

**Verificações:**
1. ✅ Verifique a pasta de SPAM
2. ✅ Confirme que a senha de app está correta
3. ✅ Veja os logs no terminal (mensagens de erro)
4. ✅ Teste enviando para seu próprio email primeiro

---

## 🧪 Testar Envio de Email

### Método 1: Criar Orçamento

1. Faça login no portal
2. Crie um novo orçamento
3. Verifique seu email e o terminal

### Método 2: Teste Direto (Python)

Crie um arquivo `test_email.py`:

```python
import os
from app import app, send_email

with app.app_context():
    # Teste enviando para você mesmo
    resultado = send_email(
        subject='Teste de Email',
        body='<h1>Teste</h1><p>Se você recebeu isso, o email está funcionando!</p>',
        to_email='seu@email.com'
    )
    
    if resultado:
        print("✅ Email enviado com sucesso!")
    else:
        print("❌ Erro ao enviar email")
```

Execute:
```bash
python test_email.py
```

---

## 💡 Dicas Importantes

1. **Senha de App ≠ Senha Normal**
   - Use SEMPRE senha de app para Gmail
   - Nunca use sua senha normal do Gmail

2. **Segurança**
   - NUNCA compartilhe sua senha de app
   - NUNCA faça commit do arquivo `.env` no Git
   - Use variáveis de ambiente em produção

3. **Limites do Gmail**
   - Gmail permite até 500 emails por dia na conta gratuita
   - Para mais volume, considere usar SendGrid ou Mailgun

4. **Produção**
   - Em servidores (Render, Heroku, etc.), configure variáveis de ambiente
   - Não use senhas hardcoded no código

---

## 🚀 Alternativas Avançadas

### SendGrid (Gratuito até 100 emails/dia)

1. Crie conta em: https://sendgrid.com
2. Obtenha API Key
3. Instale: `pip install sendgrid`
4. Configure no código

### Mailgun (Gratuito até 5.000 emails/mês)

1. Crie conta em: https://www.mailgun.com
2. Configure API Key
3. Mais confiável para produção

---

## ✅ Checklist

Antes de usar em produção:

- [ ] Verificação em duas etapas ativada
- [ ] Senha de app gerada
- [ ] MAIL_PASSWORD configurada
- [ ] Teste de envio realizado
- [ ] Emails chegando corretamente
- [ ] Variáveis de ambiente configuradas em produção

---

## 📞 Ainda com Problemas?

1. Verifique os logs no terminal onde o servidor está rodando
2. Os erros aparecem em vermelho com detalhes
3. Copie a mensagem de erro completa
4. Verifique se todas as configurações estão corretas

**Mensagens de sucesso aparecem assim:**
```
✅ Email enviado com sucesso para: jhonatanunes2012@gmail.com
```

**Mensagens de erro aparecem assim:**
```
❌ ERRO DE AUTENTICAÇÃO: ...
```

Siga as instruções que aparecem após o erro!

