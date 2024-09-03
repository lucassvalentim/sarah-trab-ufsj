import tkinter
from tkinter import CENTER, FLAT

from datetime import datetime

from visao.JanelaPadrao import JanelaPadrao
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.ProfissionalSaudeDAO import ProfissionalSaudeDAO
from controle.ControleProblema import ControleProblema
from visao.visaoproblema import Visaoproblema
from persistencia.ProblemaDAO import ProblemaDAO
from modelo.Consulta import Consulta
from controle.ControlePaciente import ControlePaciente
from controle.ControleConsulta import ControleConsulta

class JanelaContainerPaciente(JanelaPadrao):
    def __init__(self, master, cpf, visaoproblema: Visaoproblema,
                 controleproblema: ControleProblema, controlePaciente : ControlePaciente,
                 controleProfissionalSaude:ControleProfissionalSaude, controleConsulta:ControleConsulta):
        super().__init__(master)

        self.controleProfissionalSaude = controleProfissionalSaude
        self.controlePaciente = controlePaciente
        self.controleConsulta = controleConsulta
        self.cpf = cpf
        # INICIALIZA OS ATRIBUTOS FIXOS DA TELA

        self.iterador = 1
        self.quantidade = 0

        self.nome = None
        self.idade = None
        self.especializacao = None
        self.crm = None
        self.formacao = None
        self.tempoatividade = None
        self.convenios = None
        self.valorconsulta = None

        self.next_button = None
        self.anterior_button = None

        # INICIALIZANDO A CONFIGURAÇÃO DOS FRAMES RESPONSÁVEIS POR MOSTRAR OS CARDS DOS PACIENTES OU
        # MÉDICOS
        self.container = tkinter.Frame(self.master, bg=self.sidebar_color)
        self.container.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.6)

        self.quantidademedicos()

    def quantidademedicos(self):
        row = self.controleProfissionalSaude.carregar()
        for info in row:
            self.quantidade += 1
        return self.carregarinformacoes()

    def carregarinformacoes(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        row = self.controleProfissionalSaude.carregar()
        for info in row:
            if info.id == self.iterador:
                self.nome = info.nome
                self.idade = info.idade
                self.especializacao = info.especializacao
                self.crm = info.crm
                self.formacao = info.formacao
                self.tempoatividade = info.tempoAtividade
                self.convenios = info.convenios
                self.valorconsulta = info.precoConsulta
                print(f'id {info.id} e iterador {self.iterador}')
                break

        self.telamedico()

    # FUNÇÃO RESPONSÁVEL POR MOSTRAR AS INFORMAÇÕES DO MÉDICO PARA O PACIENTE
    def telamedico(self):

        # NOME CLIENTE
        if self.nome is None:
            self.nome = "Nome não disponível"
        img_name = tkinter.Label(self.container, text='Nome: ' + self.nome, bg=self.sidebar_color,
                                 font=self.fonte_menor)
        img_name.place(x=60, y=25, anchor="w")

        # CARACTERISTICAS CLIENTE
        self.idade = str(self.idade)
        idade_usuario = tkinter.Label(self.container, text='Idade: ' + self.idade, bg=self.sidebar_color,
                                      font=self.fonte_menor)
        idade_usuario.place(x=60, y=50, anchor="w")

        if self.especializacao is None:
            self.especializacao = "Especialização indisponível"
        especializacao_usuario = tkinter.Label(self.container, text='Especializacao: ' + self.especializacao,
                                               bg=self.sidebar_color,
                                               font=self.fonte_menor)
        especializacao_usuario.place(x=60, y=75, anchor="w")

        if self.crm is None:
            self.crm = "CRM indisponível"
        crm_usuario = tkinter.Label(self.container, text='CRM: ' + self.crm, bg=self.sidebar_color,
                                    font=self.fonte_menor)
        crm_usuario.place(x=60, y=100, anchor="w")

        if self.formacao is None:
            self.formacao = "Formação indisponível"
        formacao_usuario = tkinter.Label(self.container, text='Formação: ' + self.formacao, bg=self.sidebar_color,
                                         font=self.fonte_menor)
        formacao_usuario.place(x=60, y=125, anchor="w")

        if self.tempoatividade is None:
            self.tempoatividade = "Tempo atividade indisponível"
        tempo_usuario = tkinter.Label(self.container, text='Tempo de Atividade: ' + self.tempoatividade,
                                      bg=self.sidebar_color,
                                      font=self.fonte_menor)
        tempo_usuario.place(x=60, y=150, anchor="w")

        if self.convenios is None:
            self.convenios = "Convênio indisponível"
        convenios_usuario = tkinter.Label(self.container, text='Convênios: ' + self.convenios, bg=self.sidebar_color,
                                          font=self.fonte_menor)
        convenios_usuario.place(x=60, y=175, anchor="w")

        if self.valorconsulta is None:
            self.valorconsulta = "Valor de consulta indisponível"
        else:
            self.valorconsulta = str(self.valorconsulta)

        valor_usuario = tkinter.Label(self.container, text='Valor da consuta: ' + self.valorconsulta,
                                      bg=self.sidebar_color,
                                      font=self.fonte_menor)
        valor_usuario.place(x=60, y=200, anchor="w")

        # BOTÃO CURTIR
        curtir_button = tkinter.Button(self.container, text='Agendar', height=1, width=5, bg=self.selectionbar_color,
                                       command=self.botaoagendarpressionado)
        curtir_button.place(x=250, y=270)

        if self.quantidade > 1 and self.iterador < self.quantidade:
            # BOTÃO PROXIMO
            print('entrou no botao prox pressionado')
            self.next_button = tkinter.Button(self.container, text='Próximo', height=1, width=5,
                                              bg=self.selectionbar_color,
                                              command=self.botaoproxpressionado)
            self.next_button.place(x=470, y=270)


    def botaoproxpressionado(self):

        # SELF.VAR SERVE PARA TROCAR DE TELAS QUANDO CLICADO EM PRÓXIMO
        # TODO: implementar lógica para troca de telas
        self.iterador += 1
        self.carregarinformacoes()

        if self.iterador > 1:
            self.anterior_button = tkinter.Button(self.container, text='Anterior', height=1, width=5,
                                             bg=self.selectionbar_color,
                                             command=self.botaoanteriorpressionado)
            self.anterior_button.place(x=50, y=270)

    def botaoanteriorpressionado(self):

        self.iterador -= 1
        self.carregarinformacoes()
        if self.iterador == 1:
            if self.anterior_button is not None:
                self.anterior_button.destroy()
        else:
            self.anterior_button = tkinter.Button(self.container, text='Anterior', height=1, width=5,
                                             bg=self.selectionbar_color,
                                             command=self.botaoanteriorpressionado)
            self.anterior_button.place(x=50, y=270)

    def botaoagendarpressionado(self):
        secondary_window = tkinter.Toplevel()
        secondary_window.resizable(0, 0)
        secondary_window.title("Agendamento")
        secondary_window.config(width=300, height=220, bg=self.sidebar_color)

        # Label e campo de entrada para o dia
        label_dia = tkinter.Label(secondary_window, text="Dia:", bg=self.sidebar_color, font=self.fonte_menor)
        label_dia.place(x=20, y=20, anchor="w")
        entry_dia = tkinter.Entry(secondary_window)
        entry_dia.place(x=100, y=20, anchor="w")

        # Label e campo de entrada para o horário
        label_horario = tkinter.Label(secondary_window, text="Horário:", bg=self.sidebar_color, font=self.fonte_menor)
        label_horario.place(x=20, y=60, anchor="w")
        entry_horario = tkinter.Entry(secondary_window)
        entry_horario.place(x=100, y=60, anchor="w")

        def confirmar_agendamento():
            dia = entry_dia.get()  # Captura o valor digitado no campo "dia"
            horario = entry_horario.get()  # Captura o valor digitado no campo "horário"

            # Concatena a data e o horário e converte para datetime
            data_horario_str = f"{dia} {horario}"
            data_horario = datetime.now()
            try:
                data_horario = datetime.strptime(data_horario_str, "%d/%m/%Y %H:%M")
                print(f"Data e Horário: {data_horario}")
                # Aqui você pode adicionar lógica para salvar ou processar o objeto datetime
            except ValueError:
                print("Formato de data ou horário inválido!")

            profissional = self.controleProfissionalSaude.pesquisar(id=self.iterador)
            paciente = self.controlePaciente.pesquisar(cpf=self.cpf)
            consulta = Consulta(
                id=0,
                profissional=profissional,
                paciente=paciente,
                valor=profissional.precoConsulta,
                data_horario=data_horario
            )

            self.controleConsulta.inserir(consulta)
            secondary_window.destroy()


        # Botão para confirmar o agendamento
        button_confirmar = tkinter.Button(
            secondary_window,
            text="Confirmar",
            font=self.fonte_menor,
            command=confirmar_agendamento,
            bg=self.selectionbar_color
        )
        button_confirmar.place(x=100, y=100, anchor="w")

        # Botão para destruir a janela
        button_close = tkinter.Button(
            secondary_window,
            text="Cancelar",
            font=self.fonte_menor,
            command=secondary_window.destroy,
            bg=self.selectionbar_color
        )
        button_close.place(x=100, y=140, anchor="w")

