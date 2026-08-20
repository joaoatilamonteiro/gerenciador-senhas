from tkinter import *
import pyodbc

def conexao():
    caminho = ('DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=Projeto_Compras.db')

    conect = pyodbc.connect(caminho)

    mandante = conect.cursor()
    mandante.execute("Select * From Compradores Where nome = ? And senhas = ?", (tb_nome.get(), tb_senha.get()))
    valores = mandante.fetchall()

    if valores:
        login.destroy()
        tela_2 = Tk()
        tela_2.geometry("640x400")
        tela_2.title("Bem vindo!")

        tela_2.configure(bg="white")
        Label(tela_2, text="Gerenciador de senhas".upper(), bg="white", font="Calibri 15", fg="black").place(x=210, y=10,width=225,height=20)

        def veri():
            global tela_3
            global filtrada

            caminho = ('DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=Projeto_Compras.db')

            conect = pyodbc.connect(caminho)
            mandante = conect.cursor()
            mandante.execute("Select * From Produtos")

            valores = mandante.fetchall()

            tela_3 = Tk()
            tela_3.geometry("640x900")

            tela_3.configure(bg="white")
            tela_3.title("Verifique")
            filtrada = ""

            for va in valores:
                nome = va[1]
                senha = va[2]
                filtrada += ("___ Usuario: {}___ \n ___Senha {}___ \n \n ".format(nome, senha))

            # em vez de valores era para ser o banco de dados usuario
            Label(tela_3, text=filtrada, bg="black", font="Calibri 15", fg="white").grid(padx=2, pady=4, ipady=100,row=200)
            return tela_3

        def novo_cadastro():
            global tela_4

            def gravar_dados():

                mandante.execute("Select * From Produtos")

                mandante.execute("INSERT INTO Produtos (login, senha) Values (?,?)", tb_nome.get(),
                                 tb_nova_senha.get())
                conect.commit()

                tb_nome.delete(0, END)
                tb_nova_senha.delete(0, END)

            tela_4 = Tk()
            tela_4.geometry("300x400")
            tela_4.title("Login")

            tela_4.configure(bg="white")

            # Cria o titulo

            Label(tela_4, text="Usuario", bg="white", font="Calibri 15", fg="black").place(x=95, y=10, width=100,
                                                                                             height=30)
            # Cria o campo de texto e define onde vai estar

            tb_nome = Entry(tela_4)
            tb_nome.place(x=47, y=50, width=200, height=25)

            Label(tela_4, text="Senha", bg="white", font="Calibri 15", fg="black").place(x=95, y=80, width=100,height=30)

            tb_nova_senha = Entry(tela_4)
            tb_nova_senha.place(x=47, y=120, width=200, height=25)

            BBv = Button(tela_4, text="Novo cadastro", command=gravar_dados)
            BBv.place(x=95, y=180, width=100, height=45)

            BBs = Button(tela_4, text="Fechar", command=tela_4.destroy)
            BBs.place(x=95, y=260, width=100, height=45)
            return

        def preto():

            tela_2.configure(bg="black")
            Label(tela_2, text="Gerenciador de senhas".upper(), bg="white", font="Calibri 15", fg="black").place(
                x=210, y=10, width=225, height=20)
            Bv.configure(bg="black", fg="white")
            Bn.configure(bg="black", fg="white")
            tela_3.configure(bg="black")
            Label(tela_3, text="Senhas", bg="#808080", font="Calibri 15", fg="black").place(x=210, y=10, width=225,height=20)


        def branco():
            tela_2.configure(bg="white")
            Label(tela_2, text="Gerenciador de senhas".upper(), bg="white", font="Calibri 15", fg="black").place(x=210,y=10,width=225, height=20)
            Bv.configure(bg="white", fg="black")
            Bn.configure(bg="white", fg="black")
            tela_3.configure(bg="white")
            Label(tela_3, text="Senhas", bg="white", font="Calibri 15", fg="black").place(x=210, y=10, width=225,height=20)


        Bw = Button(tela_2, text="Modo claro", command=branco)
        Bw.place(x=95, y=260, width=100, height=45)

        Bb = Button(tela_2, text="Modo escuro", fg="white", bg="black", command=preto)
        Bb.place(x=440, y=260, width=100, height=45)

        Bv = Button(tela_2, text="Verificiar", command= veri)
        Bv.place(x=270, y=100, width=100, height=45)

        Bn = Button(tela_2, text="Nova senha", command= novo_cadastro)
        Bn.place(x=270, y=180, width=100, height=45)

        tela_2.mainloop()

    else:
        Label(login, text="Usuario ou senha incorreta", bg="red", font="Calibri 15", fg="black").place(x=35, y=150,width=230, height=20)


login = Tk()
login.geometry("300x400")
login.title("Login")

login.configure(bg="#00ffff")

# Cria o titulo

Label(login, text="Usuario", bg="#00ffff", font="Calibri 15", fg="black").place(x=95, y=10, width=100, height=30)
# Cria o campo de texto e define onde vai estar

tb_nome = Entry(login)
tb_nome.place(x=47, y=50, width=200, height=25)

Label(login, text="Senha", bg="#00ffff", font="Calibri 15", fg="black").place(x=95, y=80, width=100, height=30)
tb_senha = Entry(login, show="*")
tb_senha.place(x=47, y=120, width=200, height=25)

BBv = Button(login, text="Verificar", command=conexao)
BBv.place(x=95, y=180, width=100, height=45)

BBs = Button(login, text="Fechar", command=login.destroy)
BBs.place(x=95, y=260, width=100, height=45)

login.mainloop()