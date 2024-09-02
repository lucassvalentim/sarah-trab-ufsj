import tkinter
from tkinter import *
from visao.JanelaPadrao import JanelaPadrao
from visao.visaopaciente import Visaopaciente
from controle.ControlePaciente import ControlePaciente
from persistencia.PersistenciaPaciente import PersistenciaPaciente


class JanelaContainerMedico(JanelaPadrao):
    def __init__(self, master, persistenciapaciente: PersistenciaPaciente,
                 controlepaciente: ControlePaciente, visaopaciente: Visaopaciente, ):
        super().__init__(master)

        self.iterador = 1
        self.quantidade = 0
        self.visaopaciente = visaopaciente
        self.persistenciapaciente = persistenciapaciente
        self.controlepaciente = controlepaciente

        self.nome = None
        self.idade = None
        self.sintomas = None

        self.next_button = None
        self.anterior_button = None
        # INICIALIZA OS ATRIBUTOS FIXOS DA TELA

        # INICIALIZANDO A CONFIGURAÇÃO DOS FRAMES RESPONSÁVEIS POR MOSTRAR OS CARDS DOS PACIENTES OU
        # MÉDICOS
        self.container = tkinter.Frame(self.master, bg=self.sidebar_color)
        self.container.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.6)

        self.quantidademedicos()

    def quantidademedicos(self):
        row = self.persistenciapaciente.carregar_pacientes()
        for info in row:
            self.quantidade += 1
        return self.carregarinformacoes()

    def carregarinformacoes(self):
        row = self.persistenciapaciente.carregar_pacientes()
        for info in row:
            if info.id == self.iterador:
                self.nome = info.nome
                self.idade = info.idade
                self.sintomas = info.sintomas
                print(f'id {info.id} e iterador {self.iterador}')
                break

        self.telapaciente()

    # FUNÇÃO RESPONSÁVEL POR MOSTRAR AS INFORMAÇÕES DO PACIENTE PARA O MÉDICO
    def telapaciente(self):

        # NOME MEDICO
        img_name = tkinter.Label(self.container, text='Nome: ' + self.nome, bg=self.sidebar_color, font=self.fonte_menor)
        img_name.place(x=60, y=25, anchor="w")

        self.idade = str(self.idade)
        # CARACTERISTICAS MEDICO
        idade_usuario = tkinter.Label(self.container, text='Idade: ' + self.idade, bg=self.sidebar_color,
                                      font=self.fonte_menor)
        idade_usuario.place(x=60, y=50, anchor="w")

        sintomas_usuario = tkinter.Label(self.container, text='Sintomas: ' + self.sintomas, bg=self.sidebar_color,
                                         font=self.fonte_menor)
        sintomas_usuario.place(x=60, y=75, anchor="w")

        # BOTÃO ACEITAR A CONSULTA
        botao_aceitar = tkinter.Button(self.container, text='Aceitar', height=1, width=5, bg=self.selectionbar_color)
        botao_aceitar.place(x=250, y=270)

        if self.quantidade > 1 and self.iterador < self.quantidade:
            # BOTÃO PROXIMO
            print('entrou no botao prox pressionado')
            self.next_button = tkinter.Button(self.container, text='Próximo', height=1, width=5, bg=self.selectionbar_color,
                                         command=self.botaoproxpressionado)
            self.next_button.place(x=470, y=270)
        else:
            self.next_button.destroy()

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
            self.anterior_button.destroy()
        else:
            self.anterior_button = tkinter.Button(self.container, text='Anterior', height=1, width=5,
                                             bg=self.selectionbar_color,
                                             command=self.botaoanteriorpressionado)
            self.anterior_button.place(x=50, y=270)



