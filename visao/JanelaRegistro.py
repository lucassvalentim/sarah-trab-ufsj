import tkinter
from tkinter import *
from PIL import ImageTk, Image
from visao.JanelaPadrao import JanelaPadrao
from visao.JanelaRegistroMedico import JanelaRegistroMedico
from visao.JanelaRegistroPaciente import JanelaRegistroPaciente
from visao.visaopaciente import Visaopaciente
from visao.visaoprofissional import Visaoprofissional
from controle.ControlePaciente import ControlePaciente
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.PacienteDAO import PacienteDAO
from persistencia.ProfissionalSaudeDAO import ProfissionalSaudeDAO
from controle.ControleProblema import ControleProblema
from visao.visaoproblema import Visaoproblema
from persistencia.ProblemaDAO import ProblemaDAO
from controle.ControleConsulta import ControleConsulta

class JanelaRegistro(JanelaPadrao):
    def __init__(self, master, visaopaciente: Visaopaciente, controlepaciente: ControlePaciente,
                 visaomedico: Visaoprofissional, controlemedico: ControleProfissionalSaude,
                 controleConsulta: ControleConsulta, visaoproblema: Visaoproblema, controleproblema: ControleProblema):

        super().__init__(master)
        self.master = master
        self.cpf_valor = None
        self.visaopaciente = visaopaciente
        self.controlepaciente = controlepaciente
        self.visaomedico = visaomedico
        self.controlemedico = controlemedico
        self.controleConsulta = controleConsulta
        self.visaoproblema = visaoproblema
        self.controleproblema = controleproblema

        # TODO: deixar bonitinho o título(colocar logo)
        self.master.title("Cadastro")

        self.var = StringVar()
        self.holder_list = []

        self.configurarJanelaRegistro()

    def configurarJanelaRegistro(self):
        # IMAGEM DE FUNDO DA TELA
        bg_panel = Image.open('assets/sarah_registro.png')
        bg_panel_photo = ImageTk.PhotoImage(bg_panel)
        bg_panel = Label(self.master, image=bg_panel_photo)
        bg_panel.image = bg_panel_photo
        bg_panel.pack(fill='both')

        # CRIANDO FRAME ONDE VAI FICAR AS CAIXINHAS DE PACIENTE E MÉDICO
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # CRIANDO BOTÃO PACIENTE
        paciente = Radiobutton(label, text="Paciente", variable=self.var, value='Paciente',
                               command=self.purchase)
        paciente.config(indicatoron=0, width=12, value='Paciente')
        paciente.grid(row=0, column=0)

        # ADICIONANDO O BOTÃO NA HOLDER_LIST --> ISSO SERVE PRA PODER APAGAR ELES DPS NA FUNÇÃO
        # PURCHASE
        self.holder_list.append(paciente)

        # CRIANDO BOTÃO MÉDICO
        medico = Radiobutton(label, text="Medico", variable=self.var, value='Medico',
                             command=self.purchase)
        medico.config(indicatoron=0, width=12, value='Medico')
        medico.grid(row=0, column=1)
        # ADICIONANDO O BOTÃO NA HOLDER_LIST --> ISSO SERVE PRA PODER APAGAR ELES DPS NA FUNÇÃO
        # PURCHASE
        self.holder_list.append(medico)

    # FUNÇÃO RESPONSÁVEL POR DELETAR AS CAIXINHAS DE ESCOLHA PACIENTE E MÉDICO :D
    def purchase(self):
        # TO FAZENDO ISSO SO PRA PRINTAR OS VALORES DA LISTA PRA VER SE TAVA DANDO
        # CERTO
        print(self.holder_list)
        selected_value = self.var.get()
        # VERIFICANDO SE É PACIENTE, SE FOR CHAMA A FUNÇÃO CAMPOSPACIENTE()
        if selected_value == 'Paciente':
            print(selected_value)
            for widget in self.holder_list:
                widget.grid_remove()

            self.holder_list = []
            self.master.update_idletasks()
            self.camposPaciente()

        # VERIFICANDO SE É MÉDICO, SE FOR CHAMA A FUNÇÃO CAMPOSPROFISSIONAL()
        elif selected_value == 'Medico':
            print(selected_value)
            for widget in self.holder_list:
                widget.grid_remove()

            self.holder_list = []
            self.master.update_idletasks()
            self.camposProfissional()

    def camposPaciente(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaRegistroPaciente(
            master=self.master,
            cpf=self.cpf_valor,
            visao=self.visaopaciente,
            controle=self.controlepaciente,
            controlemedico=self.controlemedico,
            visaoproblema=self.visaoproblema,
            controleproblema=self.controleproblema,
            controleConsulta=self.controleConsulta
        )

    def camposProfissional(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaRegistroMedico(
            master=self.master,
            cpf=self.cpf_valor,
            visao=self.visaomedico,
            controle=self.controlemedico,
            controleConsulta=self.controleConsulta,
            controleProblema=self.controleproblema
        )
