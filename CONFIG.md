# Configuração do Portal RPA

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
SECRET_KEY=sua-chave-secreta-muito-segura-aqui
MAIL_USERNAME=jhonatanunes2012@gmail.com
MAIL_PASSWORD=sua-senha-de-app-gmail
GOOGLE_CLIENT_ID=seu-client-id-google.apps.googleusercontent.com
```

## Como obter a Senha de App do Gmail

1. Acesse: https://myaccount.google.com/
2. Vá em "Segurança"
3. Ative a "Verificação em duas etapas"
4. Acesse: https://myaccount.google.com/apppasswords
5. Selecione "Email" e "Outro (nome personalizado)"
6. Digite "Portal RPA"
7. Clique em "Gerar"
8. Copie a senha gerada (16 caracteres)
9. Use essa senha na variável `MAIL_PASSWORD`

## Como obter o Google Client ID

1. Acesse: https://console.cloud.google.com/
2. Crie um novo projeto ou selecione um existente
3. Vá em "APIs e Serviços" > "Credenciais"
4. Clique em "Criar Credenciais" > "ID do cliente OAuth"
5. Configure:
   - Tipo de aplicativo: Aplicativo da Web
   - Nome: Portal RPA
   - Origens JavaScript autorizadas: http://localhost:5000 (desenvolvimento)
   - URIs de redirecionamento: http://localhost:5000/login/google (desenvolvimento)
6. Para produção, adicione os URLs do seu domínio
7. Copie o Client ID gerado

## Instalação das Dependências

```bash
pip install -r requirements.txt
```

## Executar o Sistema

```bash
python app.py
```

O sistema estará disponível em: http://localhost:5000

