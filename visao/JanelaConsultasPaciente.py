import tkinter
from visao.JanelaPadrao import JanelaPadrao
from controle.ControlePaciente import ControlePaciente
from controle.ControleConsulta import ControleConsulta
class JanelaConsultasPaciente(JanelaPadrao):
    def __init__(self, master, cpf, controlePaciente: ControlePaciente, controleConsulta: ControleConsulta):
        super().__init__(master)

        self.var_um = 0

        self.cpf_valor = cpf
        self.controlePaciente = controlePaciente
        self.controleConsulta = controleConsulta
        # INICIALIZANDO OS ATRIBUTOS DA TELA
        self.secondary_window = tkinter.Toplevel()
        self.secondary_window.resizable(0, 0)
        self.secondary_window.title("Consultas")
        self.secondary_window.config(width=600, height=450, bg=self.sidebar_color)

        # INICIALIZANDO A CONFIGURAÇÃO DOS CONTAINERS COM AS INFORMAÇÕES
        self.container_agendadas = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_agendadas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

        self.container_analise = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_analise.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)

        self.telapaciente()

    def telapaciente(self):
        self.consultasagendaspacientes()
        # self.consultasemanalisepacientes()

    def consultasagendaspacientes(self):
        row = self.controlePaciente.carregar()
        id = 0
        for info in row:
            if self.cpf_valor == info.cpf:
                id = info.id
                break

        consulta = self.controleConsulta.carregar_por_paciente(paciente_id=id)[0]
        nome = consulta.profissional.nome
        date_time = consulta.data_horario
        especializacao = consulta.profissional.especializacao
        localizacao = consulta.profissional.localidade

        # TÍTULO
        label_agendadas = tkinter.Label(self.secondary_window, text="Consultas Agendadas", foreground="black",
                                        bg=self.sidebar_color, font=self.fonte_menor)
        label_agendadas.place(x=25, y=3)

        # CONFIGURAÇÃO DO SUBFRAME UM
        consultas_agendadas_um = tkinter.Frame(self.container_agendadas, bg=self.selectionbar_color,
                                               highlightbackground="grey",
                                               highlightthickness=2)
        consultas_agendadas_um.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.3)

        # INFORMAÇÕES DENTRO DO SUBFRAME UM
        label_nome_um = tkinter.Label(consultas_agendadas_um, text="Nome do médico: " + nome + '\t\t\t\t' +
                                                                   'Data: ' + date_time.strftime("%d/%m/%Y %H:%M"), foreground="black",
                                      bg=self.selectionbar_color, font=self.fonte_menor)
        label_nome_um.place(x=5, y=5)

        label_especialidade_um = tkinter.Label(consultas_agendadas_um, text="Especialização: " + especializacao
                                                                            + '\t\t\t' + 'Localização: ' + localizacao,
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
        botao_prox.place(x=280, y=150)


    def apertoubotaoproxagenda(self):
        self.var_um += 1

        botao_ant = tkinter.Button(
            self.container_agendadas,
            text="<",
            bg=self.selectionbar_color
        )
        botao_ant.place(x=200, y=320)

