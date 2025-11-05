from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Tenta carregar variáveis de ambiente do arquivo .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv não instalado, usa variáveis de ambiente do sistema

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpa_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração de email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'jhonatanunes2012@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')  # Configurar senha de app do Gmail
app.config['MAIL_DEFAULT_SENDER'] = 'jhonatanunes2012@gmail.com'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Modelos do banco de dados
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)  # Senha criptografada (nullable para migração)
    google_id = db.Column(db.String(200), unique=True, nullable=True)  # Opcional para futuro
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        """Define a senha do usuário (criptografada)"""
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        from werkzeug.security import check_password_hash
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nome_empresa = db.Column(db.String(200), nullable=False)
    contato = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(50))
    tipo_servico = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prazo_desejado = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pendente')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('orcamentos', lazy=True))

    def __repr__(self):
        return f'<Orcamento {self.id} - {self.nome_empresa}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def send_email(subject, body, to_email, from_email=None):
    """Envia email usando SMTP com múltiplos provedores"""
    from_email = from_email or app.config['MAIL_DEFAULT_SENDER']
    mail_password = app.config['MAIL_PASSWORD']
    mail_username = app.config['MAIL_USERNAME']
    
    # Se não tem senha configurada, mostra aviso
    if not mail_password or mail_password == '':
        print("⚠️ AVISO: MAIL_PASSWORD não configurado!")
        print("   Configure a senha de app do Gmail para enviar emails.")
        print("   Veja: CONFIG_EMAIL.md")
        return False
    
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html', 'utf-8'))
        
        # Detecta o provedor baseado no email
        if 'gmail.com' in mail_username.lower():
            server = smtplib.SMTP('smtp.gmail.com', 587)
        elif 'outlook.com' in mail_username.lower() or 'hotmail.com' in mail_username.lower():
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        elif 'yahoo.com' in mail_username.lower():
            server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        else:
            # Usa configuração padrão
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        
        server.starttls()
        server.login(mail_username, mail_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        
        print(f"✅ Email enviado com sucesso para: {to_email}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ ERRO DE AUTENTICAÇÃO: {e}")
        print("   Verifique se:")
        print("   1. A senha de app do Gmail está correta")
        print("   2. Você habilitou 'Acesso a apps menos seguros' (se necessário)")
        print("   3. A verificação em duas etapas está ativada")
        return False
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ ERRO: Email rejeitado - {e}")
        return False
    except smtplib.SMTPServerDisconnected as e:
        print(f"❌ ERRO: Conexão com servidor perdida - {e}")
        return False
    except Exception as e:
        print(f"❌ ERRO AO ENVIAR EMAIL: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Por favor, preencha todos os campos.', 'error')
            return render_template('login.html')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user, remember=True)
            flash(f'Bem-vindo de volta, {user.name}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Email ou senha incorretos. Tente novamente.', 'error')
    
    return render_template('login.html')


# ============================================================================
# GOOGLE OAUTH - DESABILITADO
# ============================================================================
# O código abaixo foi comentado para usar sistema de cadastro/login tradicional
# Para reativar no futuro, descomente e configure o GOOGLE_CLIENT_ID
# ============================================================================

# @app.route('/login/google', methods=['POST'])
# def login_google():
#     """Endpoint para login com Google OAuth"""
#     data = request.get_json()
#     
#     # Se receber credential (JWT token do Google)
#     if 'credential' in data:
#         # Validação do token JWT do Google
#         try:
#             import base64
#             import json
#             
#             # Decodifica o token JWT
#             credential = data['credential']
#             parts = credential.split('.')
#             
#             if len(parts) != 3:
#                 return {'success': False, 'message': 'Token JWT inválido'}, 400
#             
#             # Decodifica o payload (segunda parte do JWT)
#             payload = parts[1]
#             # Adiciona padding se necessário
#             padding = len(payload) % 4
#             if padding:
#                 payload += '=' * (4 - padding)
#             
#             decoded = base64.urlsafe_b64decode(payload)
#             user_info = json.loads(decoded)
#             
#             email = user_info.get('email')
#             name = user_info.get('name', user_info.get('given_name', 'Usuário'))
#             google_id = user_info.get('sub')
#             picture = user_info.get('picture', '')
#             
#             if not email:
#                 return {'success': False, 'message': 'Email não encontrado no token'}, 400
#                 
#         except json.JSONDecodeError as e:
#             print(f"Erro ao decodificar JSON: {e}")
#             return {'success': False, 'message': 'Erro ao processar token do Google'}, 400
#         except Exception as e:
#             print(f"Erro ao decodificar token: {e}")
#             return {'success': False, 'message': f'Erro ao processar autenticação: {str(e)}'}, 400
#     else:
#         # Modo de desenvolvimento/teste (fallback)
#         email = data.get('email')
#         name = data.get('name')
#         google_id = data.get('google_id')
#         picture = None
#     
#     if not email or not name:
#         return {'success': False, 'message': 'Email e nome são obrigatórios'}, 400
#     
#     # Verifica se o usuário já existe
#     user = User.query.filter_by(email=email).first()
#     
#     if not user:
#         # Cria novo usuário
#         user = User(
#             email=email,
#             name=name,
#             google_id=google_id or email
#         )
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Bem-vindo, {name}! Sua conta foi criada com sucesso.', 'success')
#     else:
#         # Atualiza informações se necessário
#         if not user.google_id and google_id:
#             user.google_id = google_id
#         if user.name != name:
#             user.name = name
#         db.session.commit()
#         flash(f'Bem-vindo de volta, {name}!', 'info')
#     
#     login_user(user, remember=True)
#     return {'success': True, 'redirect': url_for('dashboard')}


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validações
        if not name or not email or not password:
            flash('Por favor, preencha todos os campos.', 'error')
            return render_template('cadastro.html')
        
        if password != confirm_password:
            flash('As senhas não coincidem. Tente novamente.', 'error')
            return render_template('cadastro.html')
        
        if len(password) < 6:
            flash('A senha deve ter pelo menos 6 caracteres.', 'error')
            return render_template('cadastro.html')
        
        # Verifica se o email já existe
        if User.query.filter_by(email=email).first():
            flash('Este email já está cadastrado. Faça login ou use outro email.', 'error')
            return render_template('cadastro.html')
        
        # Cria novo usuário
        user = User(
            email=email,
            name=name
        )
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Cadastro realizado com sucesso! Bem-vindo, {name}!', 'success')
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao criar conta. Tente novamente.', 'error')
            print(f"Erro ao criar usuário: {e}")
    
    return render_template('cadastro.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado com sucesso!', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    orcamentos = Orcamento.query.filter_by(user_id=current_user.id).order_by(Orcamento.created_at.desc()).all()
    return render_template('dashboard.html', orcamentos=orcamentos)


@app.route('/orcamento', methods=['GET', 'POST'])
@login_required
def criar_orcamento():
    if request.method == 'POST':
        orcamento = Orcamento(
            user_id=current_user.id,
            nome_empresa=request.form['nome_empresa'],
            contato=request.form['contato'],
            email=request.form['email'],
            telefone=request.form.get('telefone', ''),
            tipo_servico=request.form['tipo_servico'],
            descricao=request.form['descricao'],
            prazo_desejado=request.form.get('prazo_desejado', '')
        )
        
        db.session.add(orcamento)
        db.session.commit()
        
        # Envia email com o orçamento para você
        email_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2 style="color: #2c3e50;">Nova Solicitação de Orçamento</h2>
            <p><strong>Cliente:</strong> {orcamento.contato}</p>
            <p><strong>Empresa:</strong> {orcamento.nome_empresa}</p>
            <p><strong>Email:</strong> {orcamento.email}</p>
            <p><strong>Telefone:</strong> {orcamento.telefone}</p>
            <p><strong>Tipo de Serviço:</strong> {orcamento.tipo_servico}</p>
            <p><strong>Prazo Desejado:</strong> {orcamento.prazo_desejado}</p>
            <h3>Descrição:</h3>
            <p style="background-color: #f4f4f4; padding: 15px; border-radius: 5px;">{orcamento.descricao}</p>
            <hr>
            <p style="color: #7f8c8d; font-size: 12px;">Este orçamento foi criado em {orcamento.created_at.strftime('%d/%m/%Y %H:%M')}</p>
        </body>
        </html>
        """
        
        email_enviado_admin = send_email(
            subject=f'Nova Solicitação de Orçamento - {orcamento.nome_empresa}',
            body=email_body,
            to_email='jhonatanunes2012@gmail.com'
        )
        
        # Envia confirmação para o cliente
        confirmacao_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2 style="color: #27ae60;">Orçamento Recebido!</h2>
            <p>Olá {orcamento.contato},</p>
            <p>Recebemos sua solicitação de orçamento com sucesso!</p>
            <p><strong>Empresa:</strong> {orcamento.nome_empresa}</p>
            <p><strong>Tipo de Serviço:</strong> {orcamento.tipo_servico}</p>
            <p>Nossa equipe entrará em contato em breve para discutir os detalhes do seu projeto.</p>
            <p>Atenciosamente,<br>Equipe de RPA</p>
        </body>
        </html>
        """
        
        email_enviado_cliente = send_email(
            subject='Confirmação de Recebimento - Orçamento RPA',
            body=confirmacao_body,
            to_email=orcamento.email
        )
        
        # Feedback para o usuário
        if email_enviado_admin and email_enviado_cliente:
            flash('Orçamento enviado com sucesso! Você receberá uma confirmação por email.', 'success')
        elif email_enviado_admin:
            flash('Orçamento salvo com sucesso! Mas não foi possível enviar email de confirmação. Verifique a configuração de email.', 'warning')
        else:
            flash('Orçamento salvo com sucesso! Mas não foi possível enviar emails. Verifique a configuração de email no servidor.', 'warning')
        
        return redirect(url_for('dashboard'))
    
    return render_template('orcamento.html')


@app.route('/teste-email')
@login_required
def teste_email():
    """Rota para testar envio de email"""
    # Permite apenas o admin testar
    admin_email = 'jhonatanunes2012@gmail.com'
    if current_user.email != admin_email:
        flash('Apenas o administrador pode testar emails.', 'error')
        return redirect(url_for('dashboard'))
    
    teste_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <h2 style="color: #27ae60;">✅ Teste de Email - Portal RPA</h2>
        <p>Se você recebeu este email, a configuração está funcionando corretamente!</p>
        <p><strong>Data/Hora:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        <p>Atenciosamente,<br>Sistema Portal RPA</p>
    </body>
    </html>
    """
    
    resultado = send_email(
        subject='Teste de Email - Portal RPA',
        body=teste_body,
        to_email=admin_email
    )
    
    if resultado:
        flash('✅ Email de teste enviado com sucesso! Verifique sua caixa de entrada (e spam).', 'success')
    else:
        flash('❌ Erro ao enviar email de teste. Verifique os logs no terminal e a configuração de MAIL_PASSWORD.', 'error')
    
    return redirect(url_for('dashboard'))


@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


def migrate_database():
    """Migra o banco de dados se necessário"""
    try:
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        
        # Verifica se a tabela user existe
        if 'user' in inspector.get_table_names():
            columns = [col['name'] for col in inspector.get_columns('user')]
            
            # Se não tem password_hash, adiciona
            if 'password_hash' not in columns:
                print("🔄 Migrando banco de dados: adicionando campo password_hash...")
                try:
                    from sqlalchemy import text
                    with db.engine.begin() as conn:
                        conn.execute(text('ALTER TABLE user ADD COLUMN password_hash VARCHAR(200)'))
                    print("✅ Migração concluída com sucesso!")
                except Exception as e:
                    # Se já existe, ignora o erro
                    if 'duplicate column' not in str(e).lower() and 'already exists' not in str(e).lower():
                        print(f"⚠️ Erro na migração: {e}")
                        print("💡 Dica: Delete o arquivo rpa_portal.db e reinicie o servidor")
        else:
            # Se a tabela não existe, cria tudo
            db.create_all()
    except Exception as e:
        print(f"⚠️ Erro ao verificar migração: {e}")
        # Tenta criar as tabelas normalmente
        try:
            db.create_all()
        except:
            pass


if __name__ == '__main__':
    with app.app_context():
        migrate_database()
    
    # Configuração para produção
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)

