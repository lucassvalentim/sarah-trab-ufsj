import tkinter
from tkinter import *
from PIL import ImageTk, Image
from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude
from visao.JanelaHomeMedico import JanelaHomeMedico
from visao.JanelaHomePaciente import JanelaHomePaciente
from visao.JanelaRegistro import JanelaRegistro
from visao.JanelaPadrao import JanelaPadrao
from visao.visaopaciente import Visaopaciente
from visao.visaoprofissional import Visaoprofissional
from controle.ControlePaciente import ControlePaciente
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.PersistenciaPaciente import PersistenciaPaciente


class JanelaLogin(JanelaPadrao):
    def __init__(self, master, visaopaciente: Visaopaciente, visaomedico: Visaoprofissional,
                 controlepaciente: ControlePaciente,
                 persistenciapaciente: PersistenciaPaciente, controlemedico: ControleProfissionalSaude,
                 persitenciamedico: PersistenciaProfissionalSaude,
                 ):

        super().__init__(master)
        self.master = master
        self.visaopaciente = visaopaciente
        self.visaomedico = visaomedico
        self.controlepaciente = controlepaciente
        self.persistenciapaciente = persistenciapaciente
        self.controlemedico = controlemedico
        self.persistenciamedico = persitenciamedico
        self.cpf_valor = None

        # TODO: deixar bonitinho o titulo da pagina (colocar logo)
        self.master.title("Login")

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
        label_cpf = tkinter.Label(label, text='CPF', font=self.fonte, padx=5, pady=5)
        label_cpf.pack()
        self.entry_cpf = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_cpf.pack()


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

    def configurarJanelaRegistro(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaRegistro(self.master, self.visaopaciente, self.visaomedico,
                       self.controlepaciente,
                       self.persistenciapaciente, self.controlemedico,
                       self.persistenciamedico)

    #TODO: INVERTI A TELA DE MEDICO E PACIENTE NA PARTE DE MOSTRAR OS CARDS, ARRUMAR

    # FUNÇÃO RESPONSÁVEL POR CHAMAR A TELA HOME
    def configurarJanelaHome(self):
        self.cpf_valor = self.entry_cpf.get()
        tipo = 0
        row = self.persistenciapaciente.carregar_pacientes()
        for info in row:
            if self.cpf_valor == info.cpf:
                tipo = 1
                break

        if tipo == 1:
            for widget in self.master.winfo_children():
                widget.destroy()
            JanelaHomePaciente(self.master, self.cpf_valor, self.persistenciapaciente, self.controlepaciente,
                               self.visaopaciente, self.visaomedico,
                               self.persistenciamedico, self.controlemedico)

        else:
            for widget in self.master.winfo_children():
                widget.destroy()
            JanelaHomeMedico(self.master, self.cpf_valor, self.persistenciamedico, self.controlemedico,
                             self.visaomedico, self.persistenciapaciente, self.controlepaciente, self.visaopaciente)
