import tkinter
from tkinter import *
import sqlite3
import os


def criar_banco_dados():
    if not os.path.isfile("Dados.db"):
        conect = sqlite3.connect("Dados.db")
        mandante = conect.cursor()

        mandante.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            "id"	INTEGER,
            "nome"	TEXT,
            "senhas"	TEXT,
            PRIMARY KEY("id")
        );
        ''')

        mandante.execute('''
        CREATE TABLE IF NOT EXISTS dados_usuarios (
            "id"	INTEGER,
            "corporacao" TEXT,
            "login"	TEXT,
            "senha"	TEXT,
            PRIMARY KEY("id")
        );
        ''')

        mandante.execute('''INSERT INTO usuarios (nome, senhas) VALUES ("usuario", "a81295373")''')

        conect.commit()
        conect.close()


criar_banco_dados()


def conexao():
    conect = sqlite3.connect("Dados.db")
    mandante = conect.cursor()

    mandante.execute("SELECT * FROM usuarios WHERE nome = ? AND senhas = ?", (tb_nome.get(), tb_senha.get()))
    conect.commit()
    valores = mandante.fetchall()

    if valores:
        login.destroy()
        tela_2 = Tk()
        tela_2.geometry("640x400")
        tela_2.title("Bem vindo!")

        tela_2.configure(bg="#444444")
        Label(tela_2, text="Gerenciador de senhas".upper(), bg="#444444", font="Calibri 15", fg="white").place(x=210,
                                                                                                               y=10,
                                                                                                               width=225,
                                                                                                               height=20)

        def veri():

            mandante.execute("Select * From dados_usuarios")

            valores = mandante.fetchall()

            tela_3 = Tk()
            tela_3.geometry("640x600")
            senha_apara = tkinter.Label(tela_3, text="Senhas", bg="#444444", font="Calibri 25", fg="white")
            senha_apara.grid(padx=210, pady=10, ipady=5, ipadx=1)

            tela_3.configure(bg="#444444")
            tela_3.title("Verifique")

            lista = tkinter.Listbox(tela_3, bg="#444444", font="Calibri 15", fg="white")
            lista.grid(padx=80, pady=0, ipady=100, ipadx=150, row=1)

            for va in valores:
                ide = va[0]
                corporação = va[1]
                nome = va[2]
                senha = va[3]
                lista.insert(tkinter.END, "\n")
                lista.insert(tkinter.END, "__ Corporação: {}__".format(corporação))
                lista.insert(tkinter.END, "___ Usuario: {}___".format(nome))
                lista.insert(tkinter.END, " ___Senha: {}___ ".format(senha))
                lista.insert(tkinter.END, "__ ID: {}__".format(ide))

            scroll = tkinter.Scrollbar(tela_3)
            scroll.grid(row=1, column=1, sticky=tkinter.N)
            lista["yscrollcommand"] = scroll.set

            return tela_3

        def novo_cadastro():

            def gravar_dados():
                mandante.execute("Select * From dados_usuarios")
                mandante.execute("INSERT INTO dados_usuarios (corporacao,login, senha) Values (?,?,?)",
                                 (tb_corporação.get(), tb_nome.get(), tb_nova_senha.get()))
                conect.commit()

                tb_corporação.delete(0, END)
                tb_nome.delete(0, END)
                tb_nova_senha.delete(0, END)

            tela_4 = Tk()
            tela_4.geometry("300x450")
            tela_4.title("Login")

            corpoy = 15

            Label(tela_4, text="corporação".capitalize(), bg="#444444", font="Calibri 16", fg="white").place(x=95,
                                                                                                             y=corpoy,
                                                                                                             width=100,
                                                                                                             height=30)
            tb_corporação = Entry(tela_4)

            tb_corporação.place(x=47, y=corpoy + 45, width=200, height=25)

            usuy = 100

            Label(tela_4, text="usuario".capitalize(), bg="#444444", font="Calibri 16", fg="white").place(x=95, y=usuy,
                                                                                                          width=100,
                                                                                                          height=30)

            tb_nomey = 145

            tb_nome = Entry(tela_4)
            tb_nome.place(x=47, y=tb_nomey, width=200, height=25)

            Label(tela_4, text="senha".capitalize(), bg="#444444", font="Calibri 15", fg="white").place(x=95,
                                                                                                        y=usuy + 80,
                                                                                                        width=100,
                                                                                                        height=30)
            tb_nova_senha = Entry(tela_4)
            tb_nova_senha.place(x=47, y=tb_nomey + 80, width=200, height=25)

            BBvy = 280
            BBv = Button(tela_4, text="novo cadastro".capitalize(), font="Calibri 11", command=gravar_dados)
            BBv.place(x=95, y=BBvy, width=100, height=45)

            BBs = Button(tela_4, text="fechar".capitalize(), font="Calibri 15", command=tela_4.destroy)
            BBs.place(x=95, y=BBvy + 80, width=100, height=45)

            BBs.configure(bg="#444444", fg="white")
            BBv.configure(bg="#444444", fg="white")

            tela_4.configure(bg="#444444")


        def insere_usu():
            def cadastrando():
                mandante.execute("Select * From usuarios")
                mandante.execute("INSERT INTO usuarios (nome, senhas) Values (?,?)",
                                 (tb_usuario.get(), tb_senha1.get()))
                conect.commit()
                tb_usuario.delete(0, END)
                tb_senha1.delete(0, END)

            tela_6 = Tk()
            tela_6.geometry("300x400")

            tela_6.title("Cadastrar")

            tela_6.configure(bg="#444444")

            Label(tela_6, text="Usuario", bg="#444444", font="Calibri 15", fg="white").place(x=95, y=10, width=100,
                                                                                             height=30)
            tb_usuario = Entry(tela_6)
            tb_usuario.place(x=47, y=50, width=200, height=25)

            Label(tela_6, text="Senha", bg="#444444", font="Calibri 15", fg="white").place(x=95, y=80, width=100,
                                                                                           height=30)
            tb_senha1 = Entry(tela_6)

            tb_senha1.place(x=47, y=120, width=200, height=25)

            BBv = Button(tela_6, text="Verificar", font="Calibri 12", command=cadastrando)

            BBv.place(x=95, y=180, width=100, height=45)

            BBs = Button(tela_6, text="Fechar", font="Calibri 12", command=tela_6.destroy)

            BBs.place(x=95, y=260, width=100, height=45)


#apaga os dados de login do gerenciador
        def excluir_cadastro():
            def excluir():
                mandante.execute("Select * From usuarios")
                valores_excluir = mandante.fetchall()
                print(valores_excluir)

                ide = tb_excluir.get()

                mandante.execute("DELETE FROM usuarios WHERE id = {}".format(ide))

                tb_excluir.delete(0, END)
                conect.commit()

            tela_5 = Tk()
            tela_5.geometry("320x200")
            tela_5.title("Login")
            tela_5.configure(bg="#444444")

            Label(tela_5, text="Diga a ID", bg="#444444", font="Calibri 15", fg="white").place(x=105, y=10, width=100,
                                                                                             height=30)

            tb_excluir = Entry(tela_5)
            tb_excluir.place(x=57, y=50, width=200, height=25)

            BBex = Button(tela_5, text="Fechar", font="Calibri 12", command=excluir).place(x=57, y=90, width=200, height=25)

        # Chama a função para executar o código
        def fechar():
            conect.close()
            tela_2.destroy()


        def veri_cadastro():

            mandante.execute("Select * From usuarios")

            valores = mandante.fetchall()

            tela_7 = Tk()
            tela_7.geometry("640x900")
            senha_apara = tkinter.Label(tela_7, text="Senhas", bg="#444444", font="Calibri 25", fg="white")
            senha_apara.grid(padx=210, pady=10, ipady=5, ipadx=1)

            tela_7.configure(bg="#444444")
            tela_7.title("Verifique")

            lista = tkinter.Listbox(tela_7, bg="#444444", font="Calibri 15", fg="white")
            lista.grid(padx=80, pady=0, ipady=250, ipadx=150, row=1)

            for va in valores:
                ide = va[0]
                nome = va[1]
                senhas = va[2]
                lista.insert(tkinter.END, "\n")
                lista.insert(tkinter.END, "___ Usuario: {}___".format(nome))
                lista.insert(tkinter.END, " ___Senha: {}___ ".format(senhas))
                lista.insert(tkinter.END, "__ ID: {}__".format(ide))


            scroll = tkinter.Scrollbar(tela_7)
            scroll.grid(row=1, column=1, sticky=tkinter.N)
            lista["yscrollcommand"] = scroll.set


        def excluir_login():
            def excluir():
                mandante.execute("Select * From dados_usuarios")
                valores_excluir = mandante.fetchall()
                print(valores_excluir)

                ide = tb_excluir.get()

                mandante.execute("DELETE FROM dados_usuarios WHERE id = {}".format(ide))

                tb_excluir.delete(0, END)
                conect.commit()

            tela_8 = Tk()
            tela_8.geometry("320x200")
            tela_8.title("Login")
            tela_8.configure(bg="#444444")

            Label(tela_8, text="Diga a ID", bg="#444444", font="Calibri 15", fg="white").place(x=105, y=10, width=100,
                                                                                             height=30)

            tb_excluir = Entry(tela_8)
            tb_excluir.place(x=57, y=50, width=200, height=25)

            BBex = Button(tela_8, text="Fechar", font="Calibri 12", command=excluir)
            BBex.place(x=57, y=90, width=200, height=25)


        buttons = 100
        Bv = Button(tela_2, text="verificar login".capitalize(), command=veri)
        Bv.place(x=270, y=buttons - 40, width=100, height=45)  # y =60

        Bn = Button(tela_2, text="nova senha".capitalize(), command=novo_cadastro)
        Bn.place(x=270, y=buttons + 40, width=100, height=45)
        # 80 a diferença
        Bu = Button(tela_2, text="excluir cadastro".capitalize(), command=excluir_cadastro)
        Bu.place(x=270, y=buttons + 120, width=100, height=45)

        Bv.configure(bg="white", fg="#444444")
        Bn.configure(bg="white", fg="#444444")

        Bi = Button(tela_2, text="Cadastrar", command=insere_usu)
        Bi.place(x=270, y=buttons + 200, width=100, height=45)

        Bf = Button(tela_2, text="Salvar e fechar", command=fechar)
        Bf.place(x=95, y=260, width=100, height=45)

        Bb = Button(tela_2, text="Verificar cadastros", fg="black", bg="white", command=veri_cadastro)
        Bb.place(x=445, y=260, width=110, height=45)

        Bvl = Button(tela_2, text="Excluir login", fg="black", bg="white", command=excluir_login)
        Bvl.place(x=95, y=100, width=100, height=45)

        tela_2.mainloop()

    else:
        Label(login, text="Usuario ou senha incorreta", bg="red", font="Calibri 15", fg="black").place(x=35, y=150,
                                                                                                       width=230,
                                                                                                       height=20)
        tb_nome.delete(0, "end")
        tb_senha.delete(0, "end")

login = Tk()
login.geometry("300x400")
login.title("Login")

login.configure(bg="#444444")

Label(login, text="Usuario", bg="#444444", font="Calibri 15", fg="white").place(x=95, y=10, width=100, height=30)

tb_nome = Entry(login)

tb_nome.place(x=47, y=50, width=200, height=25)

Label(login, text="Senha", bg="#444444", font="Calibri 15", fg="white").place(x=95, y=80, width=100, height=30)
tb_senha = Entry(login, show="*")
tb_senha.place(x=47, y=120, width=200, height=25)

BBv = Button(login, text="Verificar", font="Calibri 12", command=conexao)
BBv.place(x=95, y=180, width=100, height=45)

BBs = Button(login, text="Fechar", font="Calibri 12", command=login.destroy)
BBs.place(x=95, y=260, width=100, height=45)

login.mainloop()
