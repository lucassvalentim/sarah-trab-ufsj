import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from gui.JanelaPadrao import JanelaPadrao
from gui.JanelaRegistro import JanelaRegistro

class JanelaCadastro(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.geometry('960x540')
        self.master.resizable(0, 0)

        self.configurarJanelaLogin()

    def configurarJanelaLogin(self):

        self.master.bg_panel = Image.open('/home/izzy/Documentos/ATT-gui/sarah-trab-ufsj/gui/sarah_login_um.png')
        photo = ImageTk.PhotoImage(self.master.bg_panel)
        self.master.bg_panel = Label(self.master, image=photo)
        self.master.bg_panel.image = photo
        self.master.bg_panel.pack(fill='both', expand='yes')

        fonte = ('Arial', 14)
        fonte_menor = ('Arial', 12)

        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx =0.5, rely=0.6, anchor=tkinter.CENTER)

        label_nome = tkinter.Label(label, text='Usuário', font=fonte, padx=5, pady=5)
        label_nome.pack()
        entry_nome = tkinter.Entry(label, font=fonte_menor)
        entry_nome.pack()

        label_senha = tkinter.Label(label, text='Senha', font=fonte, padx=5, pady=5)
        label_senha.pack()
        entry_senha = tkinter.Entry(label, show='*', font=fonte_menor)
        entry_senha.pack()

        frame_botoes =tkinter.Frame(label)
        frame_botoes.pack(padx=15, pady=15)

        botao_registrar = tkinter.Button(frame_botoes, text='Registrar',
                                    font=fonte_menor, command=self.configurarJanelaRegistro)
        botao_registrar.grid(row=0, column=0, padx=15, ipadx=2, ipady=2)


        botao_login = tkinter.Button(frame_botoes, text='Login',
                                         font=fonte_menor)
        botao_login.grid(row=0, column=1, padx=15, ipadx=2, ipady=2)


    def configurarJanelaRegistro(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaRegistro(self.master)

