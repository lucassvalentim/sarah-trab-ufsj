import tkinter
from tkinter import *
from PIL import ImageTk, Image
from gui.JanelaRegistro import JanelaRegistro
from gui.JanelaPadrao import JanelaPadrao
from gui.JanelaHome import JanelaHome
from visao.VisaoProfissional import VisaoProfissionalSaude

class JanelaLogin(JanelaPadrao):
    def __init__(self, master, visao:VisaoProfissionalSaude, tipo):
        super().__init__(master)
        self.master = master

        self.visao = visao

        # TODO: deixar bonitinho o titulo da pagina (colocar logo)
        self.master.title("Login")

        # SETANDO O TIPO PARA PACIENTE
        self.tipo = tipo

        self.configurarJanelaLogin()

    def configurarJanelaLogin(self):

        # CONFIGURA A APARENCIA DA TELA
        bg_panel = Image.open('assets/sarah_login_um.png')
        bg_panel_photo = ImageTk.PhotoImage(bg_panel)
        bg_panel = Label(self.master, image=bg_panel_photo)
        bg_panel.image = bg_panel_photo
        bg_panel.pack(fill='both')

        # FRAME RESPONSÁVEL POR FICAR OS LABELS USUÁRIO E SENHA
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        # LABEL USUÁRIO
        label_nome = tkinter.Label(label, text='CPF', font=self.fonte, padx=5, pady=5)
        label_nome.pack()
        entry_nome = tkinter.Entry(label, font=self.fonte_menor)
        entry_nome.pack()

        # LABEL SENHA
        label_senha = tkinter.Label(label, text='Senha', font=self.fonte, padx=5, pady=5)
        label_senha.pack()
        entry_senha = tkinter.Entry(label, show='*', font=self.fonte_menor)
        entry_senha.pack()

        # CONFIGURA OS BOTÕES LOGIN E REGISTRAR
        frame_botoes = tkinter.Frame(label)
        frame_botoes.pack(padx=15, pady=15)

        # BOTÃO REGISTRAR
        botao_registrar = tkinter.Button(frame_botoes, text='Registrar',
                                    font=self.fonte_menor, command=self.configurarJanelaRegistro)
        botao_registrar.grid(row=0, column=0, padx=15, ipadx=2, ipady=2)

        # BOTÃO LOGIN
        botao_login = tkinter.Button(frame_botoes, text='Login',
                                         font=self.fonte_menor, command=self.configurarJanelaHome)
        botao_login.grid(row=0, column=1, padx=15, ipadx=2, ipady=2)


    # FUNÇÃO RESPONŚAVEL POR CHAMAR A TELA REGISTRO
    def configurarJanelaRegistro(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaRegistro(self.master, self.visao)

    # FUNÇÃO RESPONSÁVEL POR CHAMAR A TELA HOME
    def configurarJanelaHome(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaHome(self.master, self.tipo)
