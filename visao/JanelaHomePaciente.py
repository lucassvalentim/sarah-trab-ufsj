import tkinter
from tkinter import *
from PIL import ImageTk, Image
from visao.JanelaExcluirInformacoes import JanelaExcluirInformacoes
from visao.JanelaConsultasPaciente import JanelaConsultasPaciente
from visao.JanelaPadrao import JanelaPadrao
from visao.JanelaContainerPaciente import JanelaContainerPaciente
from visao.visaopaciente import Visaopaciente
from controle.ControlePaciente import ControlePaciente
from persistencia.PersistenciaPaciente import PersistenciaPaciente
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude
from controle.ControleProblema import ControleProblema
from visao.visaoproblema import Visaoproblema
from persistencia.PersistenciaProblema import PersistenciaProblema
from controle.ControleAgendamento import ControleAgendamento

class JanelaHomePaciente(JanelaPadrao):
    def __init__(self, master, cpf, visao: Visaopaciente, visaoproblema: Visaoproblema, controlePaciente:ControlePaciente,
                 controlemedico: ControleProfissionalSaude, controleproblema: ControleProblema, controleagendamento: ControleAgendamento):
        super().__init__(master)
        self.paciente = controlePaciente.pesquisar(cpf=cpf)
        self.medico = controlemedico.pesquisar(cpf=cpf)
        self.master = master
        self.cpf_valor = cpf
        self.visaopaciente = visao
        self.visaoproblema = visaoproblema
        self.controlemedico = controlemedico
        self.controlePaciente = controlePaciente
        self.controleproblema = controleproblema
        self.controleagendamento = controleagendamento

        self.tipo = 2

        self.nome = None

        # TODO: deixar bonitinho o título(colocar logo)
        self.master.title("Sarah")

        # ESSA VÁRIVEL EU CRIEI PRA IMPLEMENTAR A LÓGICA DE CHAMAR A JANELACONTAINER
        # MAS ESTÁ FUNCIONANDO SÓ CHAMANDO ELA DENTRO DE CONFIGURARJANELAHOME (Ñ SEI PQ)
        self.var = 0

        self.carregarinformacoes()

    def carregarinformacoes(self):
        row = self.controlePaciente.carregar()
        n = ""
        for info in row:
            if self.cpf_valor == info.cpf:
                n = info.nome
                print(n)
                break
        self.nome = n
        self.configurarJanelaHome()

    def configurarJanelaHome(self):
        # IMAGEM DE FUNDO
        bg_panel = Image.open('assets/tela_inicial_um.png')
        bg_panel_photo = ImageTk.PhotoImage(bg_panel)
        bg_panel = Label(self.master, image=bg_panel_photo)
        bg_panel.image = bg_panel_photo
        bg_panel.pack(fill='both')

        # CORES
        sidebar_color = '#CFCFCF'
        header_color = '#53366b'
        visualisation_frame_color = "#ffffff"
        selectionbar_color = '#eff5f6'
        img_color = '#FCFCFC'

        # if self.var == 0:
        JanelaContainerPaciente(
            master=self.master,
            controleproblema=self.controleproblema,
            visaoproblema=self.visaoproblema,
            controleProfissionalSaude= self.controlemedico,
            paciente= self.paciente,
            medico= self.medico,
            controleagendamento= self.controleagendamento
        )

        # SIDEBAR
        sidebar = tkinter.Frame(self.master, bg=sidebar_color)
        sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        brand_frame = tkinter.Frame(sidebar, bg=sidebar_color)
        brand_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        logo = tkinter.Label(brand_frame)
        logo.place(x=5, y=20)

        img_name = tkinter.Label(brand_frame, text='Nome: ' + self.nome, bg=sidebar_color, font=self.fonte_menor)
        img_name.place(x=20, y=27, anchor="w")

        # SUBMENU
        submenu_frame = tkinter.Frame(sidebar, bg=sidebar_color)
        submenu_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.85)

        botao_consultas = tkinter.Button(submenu_frame, text='Consultas', bg=selectionbar_color,
                                         font=self.fonte_menor, command=self.botaoconsultaspressionado)
        botao_consultas.place(relx=0.3, rely=0.1, anchor=CENTER, width=100, height=30)

        botao_mensagens = tkinter.Button(submenu_frame, text='Sair', bg=selectionbar_color,
                                         font=self.fonte_menor, command=self.FecharApp)
        botao_mensagens.place(relx=0.3, rely=0.2, anchor=CENTER, width=100, height=30)

        botao_excluir_perfil = tkinter.Button(submenu_frame, text='Excluir perfil', bg=selectionbar_color,
                                              font=self.fonte_menor, command=self.Excluirperfil)
        botao_excluir_perfil.place(relx=0.3, rely=0.3, anchor=CENTER, width=100, height=30)

    # FUNÇÃO CHAMA A JANELA DE CONSULTAS
    def botaoconsultaspressionado(self):
        JanelaConsultasPaciente(self.master)

    # FUNÇÃO FECHA O APP CASO CLIQUE EM SAIR
    def FecharApp(self):
        self.master.quit()

    def Excluirperfil(self):
        row = self.controlePaciente.carregar()
        id = 0
        print(self.cpf_valor)
        for info in row:
            if self.cpf_valor == info.cpf:
                id = info.id
                print(id)
                break
        self.visaopaciente.deletar(id)
        JanelaExcluirInformacoes(self.master)

