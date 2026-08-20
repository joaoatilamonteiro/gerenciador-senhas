# 🔐 Gerenciador de Senhas

Este projeto é um gerenciador de senhas moderno e seguro, desenvolvido em Python. Ele utiliza uma interface web local com **Streamlit** e um motor de banco de dados **SQLite**, aplicando conceitos avançados de criptografia e arquitetura *Zero-Knowledge*.

---

## 🚀 Funcionalidades Principais

* **First Setup Automático:** Cria o banco de dados dinamicamente e exige a criação de um Administrador Master no primeiro acesso, eliminando senhas padrão expostas no código.
* **Criptografia Zero-Knowledge:** As senhas do cofre são criptografadas com nível militar (AES-128 via Fernet). A chave de segurança nunca é salva em disco; ela é gerada dinamicamente na memória usando o hash (SHA-256) da senha de login do usuário.
* **Isolamento de Dados (Tenant Isolation):** Cada administrador cadastrado possui seu próprio cofre isolado. Um usuário não tem acesso às credenciais de outro.
* **Sanitização de Dados:** Tratamento de inputs para prevenir falhas de autenticação geradas por espaços em branco acidentais.
* **Gerenciamento de Administradores:** Controle total para adicionar ou remover outros usuários de acesso ao sistema.

---

## 🛠️ Como Usar

### 1. Instalação e Execução
Certifique-se de ter o Python 3 instalado. No terminal do repositório, instale as dependências executando:
> `pip install -r requirements.txt`

Para rodar o projeto localmente e abrir a interface no seu navegador, execute:
> `streamlit run interface.py`
*(Se preferir, utilize o lançador `.bat` disponibilizado na pasta para executar com duplo clique).*

### 2. Primeiro Acesso (Setup Inicial)
Por questões de segurança, o sistema não possui credenciais padrão. Ao executar o projeto em um ambiente limpo (sem o arquivo `Dados.db`), a tela de **Configuração Inicial** será exibida. Crie o seu usuário e a sua senha Master. **Atenção:** Guarde bem essa senha, pois ela será a única forma de descriptografar o seu cofre futuramente.

### 3. Navegação (Painel Principal)
Após o login bem-sucedido, utilize o menu lateral para navegar pelas funcionalidades:
* **📂 Senhas Salvas:** Visualize a lista de senhas, descriptografadas em tempo real na tela.
* **➕ Nova Senha:** Cadastre uma nova corporação, login e senha. Os dados são criptografados antes de chegar ao banco.
* **👥 Gerenciar Usuários:** Adicione ou exclua contas de outros administradores do sistema.

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Web:** Streamlit
* **Manipulação de Tabelas:** Pandas
* **Banco de Dados:** SQLite3 (Nativo)
* **Segurança e Criptografia:** Cryptography (Fernet) e Hashlib (SHA-256)

---