import sqlite3
import hashlib
import base64
from cryptography.fernet import Fernet

class GerenciadorBanco:
    def __init__(self, nome_banco = "Dados.db"):
        self.nome_banco = nome_banco
        self.criar_banco_dados()

    def _conectar(self):
        return sqlite3.connect(self.nome_banco, check_same_thread=False)

    def gerar_chave_fernet(self, senha_plana):
        chave_bytes = hashlib.sha256(senha_plana.encode()).digest()
        return Fernet(base64.urlsafe_b64encode(chave_bytes))

    def _hash_senha(self, senha_plana):
        return hashlib.sha256(senha_plana.encode()).hexdigest()

    def criar_banco_dados(self):
        with self._conectar() as connect:
            mandante = connect.cursor()

            mandante.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "nome" TEXT,
                "senhas" TEXT
            );
            ''')

            mandante.execute('''
            CREATE TABLE IF NOT EXISTS dados_usuarios (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "usuario_id" INTEGER,
                "corporacao" TEXT,
                "login" TEXT,
                "senha" TEXT,
                FOREIGN KEY("usuario_id") REFERENCES usuarios("id")
            );
            ''')
            connect.commit()

    def verificar_login(self, nome, senha_plana):
        senha_hash = self._hash_senha(senha_plana)
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("SELECT id, nome FROM usuarios WHERE nome = ? AND senhas = ?", (nome, senha_hash))
            return mandante.fetchone()

    def atualizar_senha(self, id_usuario, nova_senha):
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("UPDATE usuarios SET senhas = ? WHERE id = ?", (nova_senha, id_usuario))
            connect.commit()

    def cadastrando(self, nome, senha_plana):
        senha_hash = self._hash_senha(senha_plana)
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("INSERT INTO usuarios (nome, senhas) Values (?,?)", (nome, senha_hash))
            connect.commit()

    def listar_usuarios(self):
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("SELECT id, nome FROM usuarios")
            return mandante.fetchall()

    def excluir_usuario(self, ide):
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("DELETE FROM dados_usuarios WHERE usuario_id = ?", (ide,))
            mandante.execute("DELETE FROM usuarios WHERE id = ?", (ide,))
            connect.commit()

    def cadastra_senha(self, usuario_id, chave_fernet, corporacao, login, senha):
        senha_cripto = chave_fernet.encrypt(senha.encode()).decode()
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("INSERT INTO dados_usuarios (usuario_id, corporacao, login, senha) Values (?,?,?,?)",
                             (usuario_id, corporacao, login, senha_cripto))
            connect.commit()

    def listar_senhas(self, usuario_id, chave_fernet):
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("SELECT id, corporacao, login, senha FROM dados_usuarios WHERE usuario_id = ?",
                             (usuario_id,))
            linhas = mandante.fetchall()

            resultados = []
            for linha in linhas:
                ide, corp, login, senha_cripto = linha
                try:
                    senha_limpa = chave_fernet.decrypt(senha_cripto.encode()).decode()
                except:
                    senha_limpa = "[NÃO CRIPTOGRAFADA]"
                resultados.append((ide, corp, login, senha_limpa))
            return resultados

    # CORREÇÃO: Adicionado usuario_id para segurança e evitar crash
    def excluir_senha(self, ide, usuario_id):
        with self._conectar() as connect:
            mandante = connect.cursor()
            mandante.execute("DELETE FROM dados_usuarios WHERE id = ? AND usuario_id = ?", (ide, usuario_id))
            connect.commit()