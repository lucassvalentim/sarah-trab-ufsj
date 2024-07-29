import tkinter
from gui.JanelaPadrao import JanelaPadrao


class JanelaConsultas(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)

        # INICIALIZANDO OS ATRIBUTOS DA TELA
        self.secondary_window = tkinter.Toplevel()
        self.secondary_window.resizable(0, 0)
        self.secondary_window.title("Consultas")
        self.secondary_window.config(width=600, height=500, bg=self.sidebar_color)
        self.button_close = tkinter.Button(
            self.secondary_window,
            text="Fechar",
            command=self.secondary_window.destroy,
            bg=self.selectionbar_color

        )
        self.button_close.place(x=490, y=450)

        # INICIALIZANDO A CONFIGURAÇÃO DOS CONTAINERS COM AS INFORMAÇÕES
        self.container_agendadas = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_agendadas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

        self.container_analise = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_analise.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)

        # VARIAVEIS PARA IMPLEMENTAR A LOGICA DE TROCAR AS INFORMAÇÕES DA CONSULTA EM ANALISE E AGENDA
        self.var_um = 0
        self.var_dois = 0

        self.configurarjanelacurtir()

    def configurarjanelacurtir(self):
        self.consultasagendas()
        self.consultasemanalise()

    # FRAME RESPONŚAVEL PELAS CONSULTAS AGENDADAS
    def consultasagendas(self):
        # TÍTULO
        label_agendadas = tkinter.Label(self.secondary_window, text="Consultas Agendadas", foreground="black",
                                        bg=self.sidebar_color, font=self.fonte_menor)
        label_agendadas.place(x=25, y=3)

        # CONFIGURAÇÃO DO SUBFRAME UM
        consultas_agendadas_um = tkinter.Frame(self.container_agendadas, bg=self.selectionbar_color,
                                             highlightbackground="grey",
                                             highlightthickness=2)
        consultas_agendadas_um.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.3)

        # CONFIGURAÇÃO DO SUBFRAME DOIS
        consultas_agendadas_dois = tkinter.Frame(self.container_agendadas, bg=self.selectionbar_color,
                                               highlightbackground="grey",
                                               highlightthickness=2)
        consultas_agendadas_dois.place(relx=0.0, rely=0.4, relwidth=1, relheight=0.3)

        # INFORMAÇÕES DENTRO DO SUBFRAME UM
        label_nome_um = tkinter.Label(consultas_agendadas_um, text="Nome do médico: " + 'Rodolfo' + '\t\t\t\t' +
                                                                 'Horário: ' + '14:30', foreground="black",
                                      bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_um.place(x=5, y=5)

        label_especialidade_um = tkinter.Label(consultas_agendadas_um, text="Especialização: " + 'Ginecologista'
                                                                          + '\t\t\t' + 'Localização: ' + 'Belo Horizonte',
                                               foreground="black",
                                               bg=self.selectionbar_color, font=self.fonte_menor)
        label_especialidade_um.place(x=5, y=30)

        # INFORMAÇÕES DENTRO DO SUBFRAME DOIS
        label_nome_dois = tkinter.Label(consultas_agendadas_dois, text="Nome do médico: " + 'Rodolfo' + '\t\t\t\t' +
                                                                     'Horário: ' + '14:30', foreground="black",
                                        bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_dois.place(x=5, y=5)

        label_especialidade_dois = tkinter.Label(consultas_agendadas_dois, text="Especialização: " + 'Ginecologista'
                                                                              + '\t\t\t' + 'Localização: ' + 'Belo Horizonte',
                                                 foreground="black",
                                                 bg=self.selectionbar_color, font=self.fonte_menor)
        label_especialidade_dois.place(x=5, y=30)

        # BOTAO PROXIMO
        botao_prox = tkinter.Button(
            self.container_agendadas,
            text=">",
            command=self.apertoubotaoproxagenda,
            bg=self.selectionbar_color
        )
        botao_prox.place(x=280, y=150)

    # FRAME RESPONSÁVEL PELAS CONSULTAS EM ANÁLISE
    def consultasemanalise(self):
        # TÍTULO
        label_analise = tkinter.Label(self.secondary_window, text="Consultas em análise", foreground="black",
                                      bg=self.sidebar_color, font=self.fonte_menor)
        label_analise.place(x=25, y=215)

        # CONFIGURAÇÃO DO SUBFRAME UM
        consultas_analise_um = tkinter.Frame(self.container_analise, bg=self.selectionbar_color,
                                             highlightbackground="grey",
                                             highlightthickness=2)
        consultas_analise_um.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.3)

        # INFORMAÇÕES DENTRO DO SUBFRAME UM
        label_nome_um = tkinter.Label(consultas_analise_um, text="Nome do médico: " + 'Rodolfo' + '\t\t\t\t' +
                                                                 'Horário: ' + '14:30', foreground="black",
                                      bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_um.place(x=5, y=5)

        label_especialidade_um = tkinter.Label(consultas_analise_um, text="Especialização: " + 'Ginecologista'
                                               + '\t\t\t' + 'Localização: '+'Belo Horizonte', foreground="black",
                                         bg=self.selectionbar_color, font=self.fonte_menor)
        label_especialidade_um.place(x=5, y=30)

        # CONFIGURAÇÃO DO SUBFRAME DOIS
        consultas_analise_dois = tkinter.Frame(self.container_analise, bg=self.selectionbar_color,
                                               highlightbackground="grey",
                                               highlightthickness=2
                                               )
        consultas_analise_dois.place(relx=0.0, rely=0.4, relwidth=1, relheight=0.3)

        # INFORMAÇÕES DENTRO DO SUBFRAME DOIS
        label_nome_dois = tkinter.Label(consultas_analise_dois, text="Nome do médico: " + 'Rodolfo' + '\t\t\t\t' +
                                                                 'Horário: ' + '14:30', foreground="black",
                                      bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_dois.place(x=5, y=5)

        label_especialidade_dois = tkinter.Label(consultas_analise_dois, text="Especialização: " + 'Ginecologista'
                                                                          + '\t\t\t' + 'Localização: ' + 'Belo Horizonte',
                                               foreground="black",
                                               bg=self.selectionbar_color, font=self.fonte_menor)
        label_especialidade_dois.place(x=5, y=30)

        # BOTAO PROXIMO
        botao_prox = tkinter.Button(
            self.container_analise,
            text=">",
            command=self.apertoubotaoproxanalise,
            bg=self.selectionbar_color
        )
        botao_prox.place(x=280, y=150)

    # VERIFICA SE APERTOU O BOTÃO PROXIMO, SE SIM CRIA UM BOTÃO ANTERIOR
    def apertoubotaoproxagenda(self):
        self.var_um += 1

        botao_ant = tkinter.Button(
            self.container_agendadas,
            text="<",
            bg=self.selectionbar_color
        )
        botao_ant.place(x=200, y=150)

    def apertoubotaoproxanalise(self):
        self.var_um += 1

        botao_ant = tkinter.Button(
            self.container_analise,
            text="<",
            bg=self.selectionbar_color
        )
        botao_ant.place(x=200, y=150)

