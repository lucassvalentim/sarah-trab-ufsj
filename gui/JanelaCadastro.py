from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gui.JanelaPadrao import JanelaPadrao

class JanelaCadastro(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)
        self.configurarJanelaLogin()

    def configurarJanelaLogin(self):
        self.master.attributes("-alpha", 0.9)
        #criando os quadrados da esquerda e direita
        letFrame = Frame(self.master, width=400, height=620, bg="#8B0000", relief="raise")
        rightFrame = Frame(self.master, width=670, height=620, bg="#8B0000", relief="raise")

        #titulo da pagina da esquerda
        titleLabel = Label(letFrame, text="SARAH", bg="#8B0000", font=("Georgia", 50, "bold"), fg="White")

        #colocando os elementos na tela da esquerda
        letFrame.pack(side=LEFT)
        titleLabel.place(x=60, y=250)
        rightFrame.pack(side=RIGHT)

        #criando os campos de cadastro
        userLabel = Label(rightFrame, text="Usuario", bg="#8B0000", font=("Arial", 30, "bold"), fg="White")
        userLabel.place(x=220, y=200)

        userEntry = ttk.Entry(rightFrame, width=50)
        userEntry.place(x=150, y=260)

        passLabel = Label(rightFrame, text="Senha", bg="#8B0000", font=("Arial", 30, "bold"), fg="White")
        passLabel.place(x=230, y=290)

        passEntry = ttk.Entry(rightFrame, width=50, show="*")
        passEntry.place(x=150, y=350)

        #criando os botoes
        loginButton = ttk.Button(rightFrame, text="Entrar", width=30)
        loginButton.place(x=200, y=400)

        # criando os botoes
        registerButton = ttk.Button(rightFrame, text="Registrar", width=30)
        registerButton.place(x=200, y=440)