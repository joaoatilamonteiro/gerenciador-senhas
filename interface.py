import streamlit as st
import pandas as pd
from gerenciador_banco import GerenciadorBanco

db = GerenciadorBanco()

st.set_page_config(page_title="Gerenciador de Senhas", layout="centered")

if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'usuario_id' not in st.session_state:
    st.session_state['usuario_id'] = None
if 'usuario_nome' not in st.session_state:
    st.session_state['usuario_nome'] = ""
if 'chave_fernet' not in st.session_state:
    st.session_state['chave_fernet'] = None

usuarios_existentes = db.listar_usuarios()

if not usuarios_existentes:
    st.title("🚀 Configuração Inicial")
    st.write("Bem-vindo! Parece que é a primeira vez que você abre o sistema.")
    st.write("Crie sua conta de Administrador Master para configurar o cofre.")

    with st.form("primeiro_cadastro"):
        novo_usuario = st.text_input("Nome de Usuário")
        nova_senha = st.text_input("Senha Master", type="password")

        if st.form_submit_button("Criar Meu Cofre"):
            novo_usuario_limpo = novo_usuario.strip()

            if novo_usuario_limpo and len(nova_senha) >= 4:
                db.cadastrando(novo_usuario_limpo, nova_senha)
                st.success("✅ Conta criada com sucesso! A página será recarregada para você fazer login.")
                st.rerun()
            else:
                st.error("Preencha o nome e uma senha de no mínimo 4 caracteres.")

elif not st.session_state['autenticado']:
    st.title("🔐 Login do Sistema")
    with st.form("login"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.form_submit_button("Verificar"):

            usuario_limpo = usuario.strip()
            dados_usuario = db.verificar_login(usuario_limpo, senha)

            if dados_usuario:
                st.session_state['autenticado'] = True
                st.session_state['usuario_id'] = dados_usuario[0]
                st.session_state['usuario_nome'] = dados_usuario[1]
                st.session_state['chave_fernet'] = db.gerar_chave_fernet(senha)
                st.rerun()
            else:
                st.error("Usuário ou senha incorreta")

else:
    st.sidebar.title(f"Olá, {st.session_state['usuario_nome']}")
    menu = st.sidebar.radio("Navegação", ["Senhas Salvas", "Nova Senha", "Gerenciar Usuários", "Sair"])

    if menu == "Senhas Salvas":
        st.title("📂 Suas Senhas")
        dados = db.listar_senhas(st.session_state['usuario_id'], st.session_state['chave_fernet'])

        if dados:
            df = pd.DataFrame(dados, columns=["ID", "Corporação", "Login", "Senha"])
            st.dataframe(df, hide_index=True, use_container_width=True)

            st.divider()
            st.subheader("Excluir Cadastro")
            id_excluir = st.number_input("Diga a ID", min_value=1, step=1)
            if st.button("Excluir Login"):
                db.excluir_senha(id_excluir, st.session_state['usuario_id'])
                st.success("Senha removida!")
                st.rerun()
        else:
            st.info("Nenhuma senha salva.")

    elif menu == "Nova Senha":
        st.title("➕ Novo Cadastro")
        with st.form("nova_senha"):
            corp = st.text_input("Corporação")
            log = st.text_input("Usuario (Login)")
            sen = st.text_input("Senha", type="password")
            if st.form_submit_button("Salvar Dados"):
                db.cadastra_senha(st.session_state['usuario_id'], st.session_state['chave_fernet'], corp, log, sen)
                st.success("Salvo com sucesso!")

    elif menu == "Gerenciar Usuários":
        st.title("👥 Administradores")
        users = db.listar_usuarios()
        df_users = pd.DataFrame(users, columns=["ID", "Nome"])
        st.dataframe(df_users, hide_index=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Cadastrar")
            novo_usu = st.text_input("Novo Usuário")
            nova_sen = st.text_input("Nova Senha", type="password")
            if st.button("Inserir Usuário"):
                novo_usu_limpo = novo_usu.strip()
                db.cadastrando(novo_usu_limpo, nova_sen)
                st.rerun()
        with col2:
            st.subheader("Excluir")
            id_del = st.number_input("ID para Excluir", min_value=1, step=1)
            if st.button("Deletar Admin"):
                db.excluir_usuario(id_del)
                st.rerun()

    elif menu == "Sair":
        st.session_state.clear()
        st.rerun()