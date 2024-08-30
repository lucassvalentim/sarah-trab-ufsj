import tkinter
from tkinter import *
from visao.JanelaPadrao import JanelaPadrao


class JanelaContainerPaciente(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)

        # INICIALIZA OS ATRIBUTOS FIXOS DA TELA

        # INICIALIZANDO A CONFIGURAÇÃO DOS FRAMES RESPONSÁVEIS POR MOSTRAR OS CARDS DOS PACIENTES OU
        # MÉDICOS
        self.container = tkinter.Frame(self.master, bg=self.sidebar_color)
        self.container.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.6)

        self.telamedico()

    # FUNÇÃO RESPONSÁVEL POR MOSTRAR AS INFORMAÇÕES DO MÉDICO PARA O PACIENTE
    def telamedico(self):
        # IMAGEM CLIENTE
        img_user = tkinter.PhotoImage(file='assets/flor.png')
        self.master.iconphoto(True, img_user)

        nome_user = img_user.subsample(1)
        logo = tkinter.Label(self.container, image=nome_user, bg=self.img_color, anchor=CENTER)
        logo.place(x=10, y=20)

        # NOME CLIENTE
        img_name = tkinter.Label(self.container, text='Dr. Jośe da Silva', bg=self.sidebar_color, font=self.fonte_menor)
        img_name.place(x=220, y=25, anchor="w")

        # CARACTERISTICAS CLIENTE
        idade_usuario = tkinter.Label(self.container, text='Idade: ' + '50', bg=self.sidebar_color,
                                      font=self.fonte_menor)
        idade_usuario.place(x=220, y=50, anchor="w")

        especializacao_usuario = tkinter.Label(self.container, text='Cirurgião', bg=self.sidebar_color,
                                               font=self.fonte_menor)
        especializacao_usuario.place(x=220, y=75, anchor="w")

        crm_usuario = tkinter.Label(self.container, text='CRM: ' + '5555', bg=self.sidebar_color,
                                    font=self.fonte_menor)
        crm_usuario.place(x=220, y=100, anchor="w")

        formacao_usuario = tkinter.Label(self.container, text='Formação: ' + 'UFSJ', bg=self.sidebar_color,
                                         font=self.fonte_menor)
        formacao_usuario.place(x=220, y=125, anchor="w")

        tempo_usuario = tkinter.Label(self.container, text='Tempo de Atividade: ' + '6 anos', bg=self.sidebar_color,
                                      font=self.fonte_menor)
        tempo_usuario.place(x=220, y=150, anchor="w")

        convenios = ['IPSEMG', 'UNIMED', 'ITAU']

        string_convenios = ", ".join(map(str, convenios))

        convenios_usuario = tkinter.Label(self.container, text='Convênios: ' + string_convenios, bg=self.sidebar_color,
                                          font=self.fonte_menor)
        convenios_usuario.place(x=220, y=175, anchor="w")

        valor_usuario = tkinter.Label(self.container, text='Valor da consuta: ' + '5000', bg=self.sidebar_color,
                                      font=self.fonte_menor)
        valor_usuario.place(x=220, y=200, anchor="w")

        # BOTÃO CURTIR
        curtir_button = tkinter.Button(self.container, text='Agendar', height=1, width=5, bg=self.selectionbar_color)
        curtir_button.place(x=250, y=270)

        # BOTÃO PROXIMO
        next_button = tkinter.Button(self.container, text='Próximo', height=1, width=5, bg=self.selectionbar_color,
                                     command=self.botaoproxpressionado)
        next_button.place(x=470, y=270)

    def botaoproxpressionado(self):

        # SELF.VAR SERVE PARA TROCAR DE TELAS QUANDO CLICADO EM PRÓXIMO
        # TODO: implementar lógica para troca de telas

        anterior_button = tkinter.Button(self.container, text='Anterior', height=1, width=5,
                                             bg=self.selectionbar_color,
                                             command=self.botaoproxpressionado)
        anterior_button.place(x=50, y=270)




