import pyodbc
from tkinter import *

#falta eu ajeitar a largura e comprimento do filtrada linha 40 e criar a nova fução de adicionar senha

tela_2 = Tk()
tela_2.geometry("640x400")
tela_2.title("Bem vindo!")

tela_2.configure(bg="black")
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
    Label(tela_3, text=filtrada, bg="black", font="Calibri 15", fg="white").grid(padx = 2, pady = 4, ipady = 100, row = 200 )

    conteudo = Text(tela_3, bg="black", font="Calibri 15", fg="white")
    conteudo.insert(1.0, filtrada)
    conteudo.grid(padx=1, pady=4, ipady=350, row=200)

    # chamo a scroll
    scrollbar = Scrollbar(tela_3)
    # identifico qual tipo de rolagem vai ser
    scrollbar.config(command=conteudo.yview)
    # confirmo
    conteudo.config(yscrollcommand=scrollbar.set)
    # posiciono
    scrollbar.grid(row=200, column=1, sticky="ns")

    return tela_3


def novo_cadastro():
    global tela_4

    def gravar_dados():
        caminho = ('DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=Projeto_Compras.db')

        conect = pyodbc.connect(caminho)
        mandante = conect.cursor()
        mandante.execute("Select * From Produtos")

        mandante.execute("INSERT INTO Produtos (login, senha) Values (?,?)", tb_nome.get(), tb_nova_senha.get())
        mandante.commit()

        tb_nome.delete(0, END)
        tb_nova_senha.delete(0, END)


    tela_4 = Tk()
    tela_4.geometry("300x400")
    tela_4.title("Login")

    tela_4.configure(bg="#00ffff")

    # Cria o titulo

    Label(tela_4, text="Usuario", bg="#00ffff", font="Calibri 15", fg="black").place(x=95, y=10, width=100, height=30)
    # Cria o campo de texto e define onde vai estar

    tb_nome = Entry(tela_4)
    tb_nome.place(x=47, y=50, width=200, height=25)

    Label(tela_4, text="Senha", bg="#00ffff", font="Calibri 15", fg="black").place(x=95, y=80, width=100, height=30)

    tb_nova_senha = Entry(tela_4)
    tb_nova_senha.place(x=47, y=120, width=200, height=25)

    BBv = Button(tela_4, text="Novo cadastro", command=gravar_dados)
    BBv.place(x=95, y=180, width=100, height=45)

    BBs = Button(tela_4, text="Fechar", command=tela_4.destroy)
    BBs.place(x=95, y=260, width=100, height=45)
    return

def preto():

    tela_2.configure(bg="black")
    Label(tela_2, text="Gerenciador de senhas".upper(), bg="#808080", font="Calibri 15", fg="black").place(x=210, y=10,width=225,height=20)
    Bv.configure(bg="black", fg= "white")
    Bn.configure(bg="black", fg="white")
    tela_3.configure(bg="black")
    Label(tela_3, text="Senhas", bg="#808080", font="Calibri 15", fg="black").place(x=210, y=10, width=225, height=20)
    tela_4.configure(bg="black")


def branco():
    tela_2.configure(bg="white")
    Label(tela_2, text="Gerenciador de senhas".upper(), bg="white", font="Calibri 15", fg="black").place(x=210, y=10, width=225,height=20)
    Bv.configure(bg="white", fg="black")
    Bn.configure(bg="white", fg="black")
    tela_3.configure(bg="white")
    Label(tela_3, text="Senhas", bg="white", font="Calibri 15", fg="black").place(x=210, y=10, width=225, height=20)

Bw = Button(tela_2, text="Modo claro", command= branco)
Bw.place(x =95, y =260, width =100, height =45)
Bw.configure(bg="white")

Bb = Button(tela_2, text="Modo escuro",fg="white", bg= "black", command=preto)
Bb.place(x =440, y =260, width =100, height =45)

Bv = Button(tela_2, text="Verificiar", command= veri)
Bv.place(x =270, y =100, width =100, height =45)

Bn = Button(tela_2, text="Nova senha", command= novo_cadastro)
Bn.place(x =270, y =180, width =100, height =45)

Bv.configure(bg="white")
Bn.configure(bg="white")

tela_2.mainloop()