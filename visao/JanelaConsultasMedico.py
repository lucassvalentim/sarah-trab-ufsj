import tkinter
from visao.JanelaPadrao import JanelaPadrao


class JanelaConsultasMedico(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)

        # INICIALIZANDO OS ATRIBUTOS DA TELA
        self.secondary_window = tkinter.Toplevel()
        self.secondary_window.resizable(0, 0)
        self.secondary_window.title("Consultas")
        self.secondary_window.config(width=600, height=450, bg=self.sidebar_color)

        self.container_agendadas = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_agendadas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

        # VARIAVEIS PARA IMPLEMENTAR A LOGICA DE TROCAR AS INFORMAÇÕES DA CONSULTA EM ANALISE E AGENDA
        self.var_um = 0
        self.var_dois = 0

        self.telamedico()

    def telamedico(self):
        self.consultasagendasmedicos()


    # FRAME RESPONŚAVEL PELAS CONSULTAS AGENDADAS MÉDICOS
    def consultasagendasmedicos(self):

        self.container_agendadas = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_agendadas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

        # TÍTULO
        label_agendadas = tkinter.Label(self.secondary_window, text="Consultas Agendadas", foreground="black",
                                        bg=self.sidebar_color, font=self.fonte_menor)
        label_agendadas.place(x=25, y=3)

        # CONFIGURAÇÃO DO SUBFRAME UM
        consultas_agendadas_um = tkinter.Frame(self.container_agendadas, bg=self.selectionbar_color,
                                             highlightbackground="grey",
                                             highlightthickness=2)
        consultas_agendadas_um.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.15)

        # INFORMAÇÕES DENTRO DO SUBFRAME UM
        label_nome_um = tkinter.Label(consultas_agendadas_um, text="Nome do Paciente: " + 'Rodolfo' + '\t\t\t\t' +
                                                                 'Horário: ' + '14:30', foreground="black",
                                      bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_um.place(x=5, y=5)

        label_especialidade_um = tkinter.Label(consultas_agendadas_um, text="Sintomas: " + 'Dor de cabeça.',
                                               foreground="black",
                                               bg=self.selectionbar_color, font=self.fonte_menor)
        label_especialidade_um.place(x=5, y=30)


        # BOTAO PROXIMO
        botao_prox = tkinter.Button(
            self.container_agendadas,
            text=">",
            command=self.apertoubotaoproxagenda,
            bg=self.selectionbar_color
        )
        botao_prox.place(x=280, y=320)

    # VERIFICA SE APERTOU O BOTÃO PROXIMO, SE SIM CRIA UM BOTÃO ANTERIOR
    def apertoubotaoproxagenda(self):
        self.var_um += 1

        botao_ant = tkinter.Button(
            self.container_agendadas,
            text="<",
            bg=self.selectionbar_color
        )
        botao_ant.place(x=200, y=320)
